import random
import math


def ran_noise_generation(width, height):
    noise = []
    for i in range(width * height):
        noise.append(random.randint(-128, 127))
    return noise


def waterfall_noise_generation(width, height, intensity):
    noise = []
    fluctuation = random.randint(-intensity,intensity)
    for i in range(width * height):
        noise.append(random.randint(0,1) + fluctuation)
        if fluctuation < 0:
            fluctuation += 1
        if fluctuation > 0:
            fluctuation -= 1
        if fluctuation == 0:
            fluctuation = random.randint(-intensity,intensity)

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



def convolution(source, width, height):
    conv_noise = []

    for i in range(width*height-1):


        #left side
        if i % width == 0:
            #bottom left corner
            if i == width * (height - 1):
                total = 0
                for j in range(-1, 0):
                    for k in range(0, 1):
                        total += source[j*height+i+k]
                total /= 4
                conv_noise.append(total)

            #top left corner
            if i == 0:
                total = 0
                for j in range(0, 1):
                    for k in range(0, 1):
                        total += source[j*height+i+k]
                total /= 4
                conv_noise.append(total)

        #bottom side
        if i > width * (height - 1):
            
            #bottom right corner
            if i == (width*height-1):
                total = 0
                for j in range(-1, 0):
                    for k in range(-1, 0):
                        total += source[j*height+i+k]
                total /= 4
                conv_noise.append(total)

            #bottom left corner
            if i == width * (height - 1):
                total = 0
                for j in range(-1, 0):
                    for k in range(0, 1):
                        total += source[j*height+i+k]
                total /= 4
                conv_noise.append(total)

            else:
                total = 0
                for j in range(-1, 0):
                    for k in range(-1, 1):
                        total += source[j*height+i+k]
                total /= 6
                conv_noise.append(total)


        #right side
        if i % width == width - 1:
            #top right
            if i == width - 1:
                total = 0
                for j in range(0, 1):
                    for k in range(-1, 0):
                        total += source[j*height+i+k]
                    total /= 4
                    conv_noise.append(total)
            #bottom right corner
            if i == (width*height-1):
                total = 0
                for j in range(-1, 0):
                    for k in range(-1, 0):
                        total += source[j*height+i+k]
                total /= 4
                conv_noise.append(total)

            else:
                total = 0
                for j in range(-1, 1):
                    for k in range(-1, 0):
                        total += source[j*height+i+k]
                total /= 6
                conv_noise.append(total)

        else:
            total = 0
            for j in range(-1, 1):
                for k in range(-1, 1):
                    total += source[j*height+i+k]
            total /= 9
            conv_noise.append(total)    

    return conv_noise    


def DoubleSineWave(width, height, frequency, offset):
    SineNoise = []
    x = 1 + offset
    for i in range(width):
        x -= 0.1 * frequency
        y = 1
        for j in range(height):

            y -= 0.1 * frequency
            SineNoise.append((math.sin(x)+math.sin(y)-0.5)*254)

    return SineNoise



def gatenoise(source, treshold, invert = False ):
    gated_noise = []
    for n in source:
        if invert:
            if n > treshold:
                v = treshold
            else:
                v = n

        else: 
            if n < treshold:
                v = -128
            else:
                v = n
        gated_noise.append(v)
    return gated_noise

def sumnoise(source1, source2, weight1=0.5):

    summed_noise = []
    weight2 = 1 - weight1

    for i in range(len(source1)):
        summed_noise.append((source1[i])*weight1 + (source2[i])*weight2)
    return summed_noise


Noise1 = ran_noise_generation(108, 72)



Noise2 = waterfall_noise_generation(108, 72, 154)


Noise3 = biggify(ran_noise_generation(11, 11), 11, 3)

Noise5 = DoubleSineWave(108, 72, 4, 0.1)

Noise4_3 = convolution(biggify(ran_noise_generation(11, 11), 11, 3),33, 33)
Noise4_3_2 = convolution(convolution(biggify(ran_noise_generation(11, 11), 11, 3),33, 33), 33, 33)
Noise4_1 = convolution(ran_noise_generation(108, 72),108, 72)
Noise4_1_2 = convolution(convolution(ran_noise_generation(108, 72),108, 72), 108, 72)
Noise4_5 = convolution(convolution(Noise5, 108, 72), 108, 72)


Noise4_2_2 = convolution(biggify(waterfall_noise_generation(54, 36, 81), 54, 2), 108, 72)


