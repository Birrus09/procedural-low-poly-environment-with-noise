import worlds_managing
import proc_noise


Worldsine = []
worlds_managing.populate(Worldsine, 108, 72)
worlds_managing.gen_terrain(Worldsine, proc_noise.Noise5)
worlds_managing.save_world(Worldsine, "Worlds/worldsine.txt")
