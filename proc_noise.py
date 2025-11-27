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



def convolution(source, width, height):
    conv_noise = []

    for i in range(width*height-1):
        #top side
        if i < width:
            #top right corner
            if i == width - 1:
                total = 0
                for j in range(0, 1):
                    for k in range(-1, 0):
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

            else:
                total = 0
                for j in range(0, 1):
                    for k in range(-1, 1):
                        total += source[j*height+i+k]
                total /= 6
                conv_noise.append(total)

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

            else:
                total = 0
                for j in range(-1, 1):
                    for k in range(0, 1):
                        total += source[j*height+i+k]
                total /= 6
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


Noise1 = ran_noise_generation(108, 72)
Noise2 = waterfall_noise_generation(108, 72, 154)


Noise3 = biggify(ran_noise_generation(11, 11), 11, 3)

Noise4_3 = convolution(biggify(ran_noise_generation(11, 11), 11, 3),33, 33)


Noise3 = biggify(ran_noise_generation(11, 11), 11, 3)
