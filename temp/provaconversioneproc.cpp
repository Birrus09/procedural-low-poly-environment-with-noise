#include <vector>
#include <random>
#include <iostream>
#include <cmath>
#include <cassert>

// --------------------------------------------------
// Random helpers
// --------------------------------------------------
static std::mt19937 rng(std::random_device{}());

int rand_int(int min, int max)
{
    std::uniform_int_distribution<int> dist(min, max);
    return dist(rng);
}

// --------------------------------------------------
// Noise generators
// --------------------------------------------------
std::vector<int> ran_noise_generation(int width, int height)
{
    std::vector<int> noise;
    noise.reserve(width * height);

    for (int i = 0; i < width * height; ++i)
        noise.push_back(rand_int(-128, 127));

    return noise;
}

std::vector<int> waterfall_noise_generation(int width, int height, int intensity)
{
    std::vector<int> noise;
    noise.reserve(width * height);

    int fluctuation = rand_int(-intensity, intensity);

    for (int i = 0; i < width * height; ++i)
    {
        noise.push_back(rand_int(0, 1) + fluctuation);

        if (fluctuation < 0) fluctuation++;
        if (fluctuation > 0) fluctuation--;

        if (fluctuation == 0)
            fluctuation = rand_int(-intensity, intensity);
    }

    return noise;
}

// --------------------------------------------------
// Upscaling
// --------------------------------------------------
std::vector<int> biggify(const std::vector<int>& source, int width, int factor)
{
    std::vector<int> big_noise;
    int L = static_cast<int>(source.size());

    for (int i = 0; i < L; i += width)
    {
        for (int k = 0; k < factor; ++k)
        {
            for (int z = i; z < i + width; ++z)
            {
                int idx = std::min(z, L - 1);
                for (int n = 0; n < factor; ++n)
                    big_noise.push_back(source[idx]);
            }
        }
    }

    return big_noise;
}

// --------------------------------------------------
// Convolution
// --------------------------------------------------
std::vector<double> convolution(const std::vector<int>& source, int width, int height)
{
    std::vector<double> conv_noise;
    conv_noise.reserve(width * height);

    for (int i = 0; i < width * height - 1; ++i)
    {
        double total = 0.0;

        // Left side
        if (i % width == 0)
        {
            // Top-left
            if (i == 0)
            {
                total = source[i];
                conv_noise.push_back(total / 4.0);
                continue;
            }

            // Bottom-left
            if (i == width * (height - 1))
            {
                total = source[i - height];
                conv_noise.push_back(total / 4.0);
                continue;
            }
        }

        // Bottom side
        if (i > width * (height - 1))
        {
            // Bottom-right
            if (i == width * height - 1)
            {
                total = source[i - height - 1];
                conv_noise.push_back(total / 4.0);
                continue;
            }

            total = source[i - height - 1] + source[i - height];
            conv_noise.push_back(total / 6.0);
            continue;
        }

        // Right side
        if (i % width == width - 1)
        {
            // Top-right
            if (i == width - 1)
            {
                total = source[i - 1];
                conv_noise.push_back(total / 4.0);
                continue;
            }

            total = source[i - height - 1] + source[i - 1];
            conv_noise.push_back(total / 6.0);
            continue;
        }

        // Center
        for (int j = -1; j <= 1; ++j)
        {
            for (int k = -1; k <= 1; ++k)
                total += source[i + j * height + k];
        }

        conv_noise.push_back(total / 9.0);
    }

    return conv_noise;
}

// --------------------------------------------------
// Sine noise
// --------------------------------------------------
std::vector<double> DoubleSineWave(int width, int height, double frequency, double offset)
{
    std::vector<double> sineNoise;
    sineNoise.reserve(width * height);

    double x = 1.0 + offset;

    for (int i = 0; i < width; ++i)
    {
        x -= 0.1 * frequency;
        double y = 1.0;

        for (int j = 0; j < height; ++j)
        {
            y -= 0.1 * frequency;
            sineNoise.push_back((std::sin(x) + std::sin(y) - 0.5) * 254.0);
        }
    }

    return sineNoise;
}

// --------------------------------------------------
// Gating
// --------------------------------------------------
std::vector<int> gatenoise(const std::vector<int>& source, int threshold, bool invert = false)
{
    std::vector<int> gated_noise;
    gated_noise.reserve(source.size());

    for (int n : source)
    {
        int v;
        if (invert)
        {
            v = (n > threshold) ? threshold : n;
        }
        else
        {
            v = (n < threshold) ? -128 : n;
        }
        gated_noise.push_back(v);
    }

    return gated_noise;
}

// --------------------------------------------------
// Summing
// --------------------------------------------------
std::vector<double> sumnoise(const std::vector<double>& source1,
                            const std::vector<double>& source2,
                            double weight1 = 0.5)
{
    std::vector<double> summed_noise;
    summed_noise.reserve(source1.size());

    double weight2 = 1.0 - weight1;

    for (size_t i = 0; i < source1.size(); ++i)
        summed_noise.push_back(source1[i] * weight1 + source2[i] * weight2);

    return summed_noise;
}
void print_sample(const std::vector<int>& v, int count = 10)
{
    for (int i = 0; i < count && i < (int)v.size(); ++i)
        std::cout << v[i] << " ";
    std::cout << "\n";
}

void print_sample_d(const std::vector<double>& v, int count = 10)
{
    for (int i = 0; i < count && i < (int)v.size(); ++i)
        std::cout << v[i] << " ";
    std::cout << "\n";
}

int main()
{
    const int width = 8;
    const int height = 8;

    std::cout << "=== TEST ran_noise_generation ===\n";
    auto noise = ran_noise_generation(width, height);
    assert(noise.size() == width * height);
    print_sample(noise);

    std::cout << "\n=== TEST waterfall_noise_generation ===\n";
    auto waterfall = waterfall_noise_generation(width, height, 5);
    assert(waterfall.size() == width * height);
    print_sample(waterfall);

    std::cout << "\n=== TEST biggify ===\n";
    auto big = biggify(noise, width, 2);
    assert(big.size() == width * height * 4);
    print_sample(big);

    std::cout << "\n=== TEST convolution ===\n";
    auto conv = convolution(noise, width, height);
    assert(!conv.empty());
    print_sample_d(conv);

    std::cout << "\n=== TEST DoubleSineWave ===\n";
    auto sine = DoubleSineWave(width, height, 1.0, 0.0);
    assert(sine.size() == width * height);
    print_sample_d(sine);

    std::cout << "\n=== TEST gatenoise ===\n";
    auto gated = gatenoise(noise, 0);
    assert(gated.size() == noise.size());
    print_sample(gated);

    std::cout << "\n=== TEST sumnoise ===\n";
    auto summed = sumnoise(conv, sine, 0.7);
    assert(summed.size() == conv.size());
    print_sample_d(summed);

    std::cout << "\nTUTTI I TEST PASSATI ✔\n";
    return 0;
}
