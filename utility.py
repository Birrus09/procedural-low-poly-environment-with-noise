import worlds_managing
import proc_noise


Worldsine = []
worlds_managing.populate(Worldsine, 108, 72)
worlds_managing.gen_terrain(Worldsine, proc_noise.Noise5)
worlds_managing.save_world(Worldsine, "Worlds/worldsine.txt")

while True:
    print("Options: 1) create world, 2) see worlds directory, 3) see available noises, 4) craft noise, 5) quit")
    choice = int(input("command: "))
    if choice == 1:
        width = int(input("width: "))
        height = int(input("height: "))
        world_dir = input("world name: ")
        world_dir = "Worlds/" + world_dir + ".txt"
        world_noise = input("noise: ")
        new_world = []
        worlds_managing.populate(new_world, width, height)
        worlds_managing.gen_terrain(new_world, getattr(proc_noise, world_noise))
        worlds_managing.save_world(new_world, world_dir)
        print("world created!")
    elif choice == 2:
        print("Worlds directory:")
        print("")
        for file in os.listdir("Worlds"):
            if file.endswith(".txt"):
                print(file)
    elif choice == 3:
        print("Available noises:")
        for attr in dir(proc_noise):
            if not attr.startswith("__"):
                print(attr)
    elif choice == 4:
        while True:
            print("1) save custom noise, 2) craft noise,  3) back")
            subchoice = int(input("command: "))
            if subchoice == 1:
                noise_file = input("noise file name: ")
                noise_file = "Noises/" + noise_file + ".txt"
                with open(noise_file, "w") as f:
                    for val in gen_noise:
                        f.write(f"{val}\n")
                    print("noise saved!")
                
            elif subchoice == 2:
                while True:
                    print("1) function generation, 2) function transformation, 3) back")
                    craftchoice = int(input("command: "))
                    if craftchoice == 1:
                        while True:
                            print("generative functions: 1) ran_noise_generation, 2) waterfall_noise_generation, 3) DoubleSineWave, 4) back")
                            genchoice = int(input("command: "))
                            if genchoice == 1:
                                par1 = int(input("width: "))
                                par2 = int(input("height: "))
                                gen_noise = proc_noise.ran_noise_generation(par1, par2)
                                print("noise generated.")
                            elif genchoice == 2:
                                par1 = int(input("width: "))
                                par2 = int(input("height: "))
                                par3 = int(input("intensity: "))
                                gen_noise = proc_noise.waterfall_noise_generation(par1, par2, par3)
                                print("noise generated.")
                            elif genchoice == 3:
                                par1 = int(input("width: "))
                                par2 = int(input("height: "))
                                par3 = int(input("frequency: "))
                                par4 = float(input("offset: "))
                                gen_noise = proc_noise.DoubleSineWave(par1, par2, par3, par4)
                                print("noise generated.")
                            else:
                                break
                    elif craftchoice == 2:
                        while True:
                            print("transformative functions: 1) biggify, 2) convolution (smoothify), 3) back")
                            transchoice = int(input("command: "))
                            if transchoice == 1:
                                par1 = int(input("scale factor: "))
                                par2 = int(input("original width: "))
                                gen_noise = proc_noise.biggify(gen_noise, par2, par1)
                                print("noise transformed.")
                            elif transchoice == 2:
                                par1 = int(input("original width: "))
                                par2 = int(input("original height: "))
                                gen_noise = proc_noise.convolution(gen_noise, par1, par2)
                                print("noise transformed.")
                            else:
                                break
                    else:
                        break
            else: 
                break
    else:
        break
