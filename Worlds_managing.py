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



nodes_1080_720 = []

for i in range(0,1080, 10):
    for j in range(0,720, 10):
        nodes_1080_720.append(node(i,j,0,"none"))
