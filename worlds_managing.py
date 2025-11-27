class node():
    def __init__(self, x, y, altitude, biome):
        self.x = x
        self.y = y
        self.altitude = altitude
        self.biome = biome



def gen_terrain(map_nodes, noise):
    if len(noise) >= len(map_nodes):
        for i in range(len(map_nodes)):
            map_nodes[i].altitude = noise[i]
    else:
        print("World too big!")



def save_world(world, file):
    with open(file, "w") as f:
        for n in world:
            f.write(f"{n.x},{n.y},{n.altitude},{n.biome}\n")
    pass



def load_world(world_dir):
    destination_vector = []
    with open(world_dir, "r") as file:
        dump = file.readlines()
    for i in dump:
        x, y, altitude, biome = i.strip().split(",")
        destination_vector.append(node(int(x), int(y), float(altitude), biome))

    return destination_vector

def populate(nodes_map, x, y):
    for i in range(0, x, 10):
        for j in range(0, y, 10):
            nodes_map.append(node(i,j,0,"none"))

'''

#how WaterWorld was created

gen_terrain(nodes_1080_720, proc_noise.Noise2)


save_world(nodes_1080_720, "Worlds/WaterWorld.txt")
'''
