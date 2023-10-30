
# Import pygame
import pygame
 
# Initialise pygame
pygame.init()

pygame.display.set_caption('Maze Hunter')

Icon = pygame.image.load('MazeGame/images/rat.png')

pygame.display.set_icon(Icon)

 
# Set window size
size = width,height = 600, 600
screen = pygame.display.set_mode(size)

#background screen color
color = (0, 0, 0)
 
# Clock
clock = pygame.time.Clock()
 
# Load image
image = pygame.image.load('rat.png')
 
# Set the size for the image
DEFAULT_IMAGE_SIZE = (40, 40)
 
# Scale the image to your needed size
image = pygame.transform.scale(image, DEFAULT_IMAGE_SIZE)
 
posX = 0
posY = 0
# Set a default position
DEFAULT_IMAGE_POSITION = (posX,posY)
 
# Prepare loop condition
running = True

print(size)

pygame.time.wait(1000)
 
# Event loop
while running:
    
    pygame.time.wait(100)
    
    posX = posX + 1
    posY = posY + 1
    
    if posX == 600:
        posX = 0
    
    if posY == 600:
        posY = 0
    
    DEFAULT_IMAGE_POSITION = (posX,posY)
 
    # Close window event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
 
    
    # Changing surface color
    screen.fill(color)
    # pygame.display.flip()
    
    # Show the image
    screen.blit(image, DEFAULT_IMAGE_POSITION)
 
    # Part of event loop
    pygame.display.flip()
    clock.tick(30)
