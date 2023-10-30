
# Import pygame
import pygame
 
# Initialise pygame
pygame.init()

pygame.display.set_caption('Maze Hunter')

Icon = pygame.image.load('/home/danieldfb/Repositório - NOVO/semestre4/EDL/RatChallenge/MazeGame/images/rat.png')

pygame.display.set_icon(Icon)

 
# Set window size
size = width,height = 600, 600
screen = pygame.display.set_mode(size)

#background screen color
color = (0, 0, 0)
 
# Clock
clock = pygame.time.Clock()
 
# Load image
ratImage = pygame.image.load('/home/danieldfb/Repositório - NOVO/semestre4/EDL/RatChallenge/MazeGame/images/rat.png')
cheeseImage = pygame.image.load('/home/danieldfb/Repositório - NOVO/semestre4/EDL/RatChallenge/MazeGame/images/cheese.png')
 
# Set the size for the image
RAT_IMAGE_SIZE = (40, 40)

CHEESE_IMAGE_SIZE = (40, 40)
 
# Scale the image to your needed size
ratImage = pygame.transform.scale(ratImage, RAT_IMAGE_SIZE)

cheeseImage = pygame.transform.scale(cheeseImage, CHEESE_IMAGE_SIZE)
 
posRatX = 0
posRatY = 0
# Set a default position
RAT_POSITION = (posRatX,posRatY)

posCheeseX = 500
posCheeseY = 500
# Set a default position
CHEESE_POSITION = (posCheeseX,posCheeseY)
 
# Prepare loop condition
running = True

print(size)

pygame.time.wait(1000)

# Event loop
while running:
    
    pygame.draw.rect(screen, (0, 0, 255), 
                 [20, 20, 560, 560], 5)
    
    pygame.draw.line(screen, (0, 0, 255), 
                 [100, 300], 
                 [500, 300], 5)
    
    pygame.draw.line(screen, (0, 0, 255), 
                 [300, 30], 
                 [300, 570], 5)

    pygame.display.update()
    
    pygame.time.wait(10)
    
    posRatX = posRatX + 1
    posRatY = posRatY + 1
    
    if posRatX == 600:
        posRatX = 0
    
    if posRatY == 600:
        posRatY = 0
    
    RAT_POSITION = (posRatX,posRatY)
    
    CHEESE_POSITION = (posCheeseX,posCheeseY)
 
    # Close window event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    # if(color == "black"):
    #     color = "blue"
         
    # else:
    #     color = "black"
 
    
    # Changing surface color
    screen.fill(color)
    # pygame.display.flip()
    
    # Show the image
    screen.blit(ratImage, RAT_POSITION)
    
    screen.blit(cheeseImage, CHEESE_POSITION)
 
    # Part of event loop
    # pygame.display.flip()
    # clock.tick(30)
