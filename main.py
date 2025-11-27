import pygame
import proc_noise
import worlds_managing
import os


worlds_dir = "/Worlds"


# Screen dimensions
SCREEN_WIDTH = 1080
SCREEN_HEIGHT = 720



worlds_managing.gen_terrain(worlds_managing.nodes_1080_720, proc_noise.Noise1)


def show_map(map):
    for n in map:
        a = int(n.altitude)
        r = max(0, min(255, 128 + a))
        g = 0
        b = max(0, min(255, 127 - a))
        pygame.draw.rect(screen, (r, g, b), (n.x, n.y, 10, 10))





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
    
    # Fill screen with black
    screen.fill((0, 0, 0))
    show_map(worlds_managing.nodes_1080_720)
    
    # Update display
    pygame.display.flip()

pygame.quit()
