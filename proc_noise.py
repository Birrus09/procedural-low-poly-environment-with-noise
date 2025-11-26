import random




def ran_noise_generation(width, height):
    noise = []
    for i in range(width * height):
        noise.append(random.randint(-128, 127))
    return noise


def waterfall_noise_generation(width, height, clump_size):
    noise = []
    fluctuation = random.randint(-clump_size,clump_size)
    for i in range(width * height):
        noise.append(random.randint(0,1) + fluctuation)
        if fluctuation < 0:
            fluctuation += 1
        if fluctuation > 0:
            fluctuation -= 1
        if fluctuation == 0:
            fluctuation = random.randint(-clump_size,clump_size)

    return noise


def biggify(source, width, factor):
    big_noise = []
    L = len(source)
    for i in range(0, L, width):
        for k in range(factor):
            for z in range(i, i + width):
                idx = min(z, L - 1)
                for n in range(factor):
                    big_noise.append(source[idx])
    return big_noise


Noise1 = ran_noise_generation(108, 72)
Noise2 = waterfall_noise_generation(108, 72, 154)


Noise3 = biggify(ran_noise_generation(11, 11), 11, 3)
