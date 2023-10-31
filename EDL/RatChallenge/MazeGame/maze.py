
# Import pygame
import pygame

n = 10
m = 10

maze = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 0, 1, 0, 0, 0, 0, 1, 1],
    [1, 1, 0, 1, 0, 1, 1, 1, 1, 1],
    [1, 1, 0, 0, 0, 1, 0, 0, 0, 1],
    [1, 1, 1, 1, 0, 1, 0, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 0, 1, 1],
    [1, 0, 0, 0, 0, 1, 1, 0, 1, 1],
    [1, 1, 1, 0, 0, 1, 1, 0, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]
 
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
pixels = 12

# Event loop
while running:
     
    # Filling the background with 
    # white color 
    screen.fill((255, 255, 255)) 
  
    # Display the player sprite at x 
    # and y coordinates 
    screen.blit(ratImage, (posRatX, posRatY))
    
    screen.blit(cheeseImage, (posCheeseX, posCheeseY))
  
    # iterate over the list of Event objects 
    # that was returned by pygame.event.get() 
    # method. 
    for event in pygame.event.get(): 
  
        # Closing the screen and program if the 
        # type of the event is QUIT 
        if event.type == pygame.QUIT: 
            run = False
            pygame.quit() 
            quit() 
  
        # Checking event key if the type 
        # of the event is KEYDOWN i.e. 
        # keyboard button is pressed 
        if event.type == pygame.KEYDOWN: 
  
            # Decreasing the x coordinate 
            # if the button pressed is 
            # Left arrow key 
            if event.key == pygame.K_LEFT: 
                posRatX -= pixels 
  
            # Increasing the posRatX coordinate 
            # if the button pressed is 
            # Right arrow key 
            if event.key == pygame.K_RIGHT: 
                posRatX += pixels 
  
            # Decreasing the y coordinate 
            # if the button pressed is 
            # Up arrow key 
            if event.key == pygame.K_UP: 
                posRatY -= pixels 
  
            # Increasing the y coordinate 
            # if the button pressed is 
            # Down arrow key 
            if event.key == pygame.K_DOWN: 
                posRatY += pixels 
  
        # Draws the surface object to the screen. 
    pygame.display.update() 

    # pygame.display.update()
    
    # pygame.time.wait(10)
    
    # posRatX = posRatX + 1
    # posRatY = posRatY + 1
    
    # if posRatX == 600:
    #     posRatX = 0
    
    # if posRatY == 600:
    #     posRatY = 0
    
    # RAT_POSITION = (posRatX,posRatY)
    
    CHEESE_POSITION = (posCheeseX,posCheeseY)
 
    # # Close screen event
    # for event in pygame.event.get():
    #     if event.type == pygame.QUIT:
    #         running = False
            
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
