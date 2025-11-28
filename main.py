import pygame
import worlds_managing
import os



worlds_dir = "/Worlds"


# Screen dimensions
SCREEN_WIDTH = 1080
SCREEN_HEIGHT = 720



def show_map(map, mode = 'altitude'):
    if mode == 'altitude':
        for n in map:
            a = int(max(min((n.altitude) + 128, 255),0))
            pygame.draw.rect(screen, (a, a, a), (n.x, n.y, 10, 10))

    if mode == 'temp':
        for n in map:
            a = int(n.altitude)
            r = max(0, min(255, 128 + a))
            g = 0
            b = max(0, min(255, 127 - a))
            pygame.draw.rect(screen, (r, g, b), (n.x, n.y, 10, 10))

    if mode == 'biome':
        for n in map:
            if n.biome == 'mountain':
                pygame.draw.rect(screen, (200, 200, 200), (n.x, n.y, 10, 10))
            if n.biome == 'beach':
                pygame.draw.rect(screen, (50,100,30), (n.x, n.y, 10, 10))
            if n.biome == 'ocean':
                pygame.draw.rect(screen, (0, 0, 255), (n.x, n.y, 10, 10))
            if n.biome == 'plains':
                pygame.draw.rect(screen, (0, 255, 0), (n.x, n.y, 10, 10))
            else:
                pygame.draw.rect(screen, (255,255,255), (n.x, n.y, 10, 10))

    





current_world = worlds_managing.load_world("Worlds/testworld2.txt")
current_view = "temp"


print("select world to visualize:")
for file in os.listdir("Worlds"):
    if file.endswith(".txt"):
        print(file)
world_name = input("world name: ")
current_world = worlds_managing.load_world("Worlds/" + world_name + ".txt")





# Initialize Pygame
pygame.init()



# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Procedural Terrain")

# Clock for FPS
clock = pygame.time.Clock()
FPS = 60

# Main game loop
running = True
while running:
    clock.tick(FPS)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                    current_view = "altitude"
            elif event.key == pygame.K_2:
                    current_view = "temp"
            elif event.key == pygame.K_3:
                    current_view = "biome"




        
    
    # Fill screen with black
    screen.fill((0, 0, 0))
    show_map(current_world, current_view)
    
    # Update display
    pygame.display.flip()

pygame.quit()
