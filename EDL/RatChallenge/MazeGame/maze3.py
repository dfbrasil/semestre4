
# Import pygame
import pygame
 
# Initialise pygame
pygame.init()

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

pygame.display.set_caption('Maze Hunter')

Icon = pygame.image.load('/home/danieldfb/Repositório - NOVO/semestre4/EDL/RatChallenge/MazeGame/images/rat.png')

pygame.display.set_icon(Icon)
 
size = width,height = 600, 600
screen = pygame.display.set_mode(size)
cell_size = width // n

#background screen color
color = (0, 0, 0)
 
ratImage = pygame.image.load('/home/danieldfb/Repositório - NOVO/semestre4/EDL/RatChallenge/MazeGame/images/rat.png')
cheeseImage = pygame.image.load('/home/danieldfb/Repositório - NOVO/semestre4/EDL/RatChallenge/MazeGame/images/cheese.png')
pathImage = pygame.image.load('/home/danieldfb/Repositório - NOVO/semestre4/EDL/RatChallenge/MazeGame/images/path.jpg')
wallImage = pygame.image.load('/home/danieldfb/Repositório - NOVO/semestre4/EDL/RatChallenge/MazeGame/images/wall.png')
 
RAT_IMAGE_SIZE = (40, 40)
CHEESE_IMAGE_SIZE = (40, 40)
PATH_IMAGE_SIZE = (50, 50)
WALL_IMAGE_SIZE = (50, 50)
 
# Scale the image to your needed size
ratImage = pygame.transform.scale(ratImage, RAT_IMAGE_SIZE)
cheeseImage = pygame.transform.scale(cheeseImage, CHEESE_IMAGE_SIZE)
pathImage = pygame.transform.scale(pathImage,PATH_IMAGE_SIZE)
wallImage = pygame.transform.scale(wallImage, WALL_IMAGE_SIZE)
 
posRatX = 0
posRatY = 0
RAT_POSITION = (posRatX,posRatY)

posCheeseX = 500
posCheeseY = 500
CHEESE_POSITION = (posCheeseX,posCheeseY)
 
running = True

print(size)

pygame.time.wait(1000)
pixels = 12

while running:
     
    # screen.fill((255, 255, 255)) 

    screen.blit(ratImage, (posRatX, posRatY))
    
    screen.blit(cheeseImage, (posCheeseX, posCheeseY))
    
    for i in range(n):
        for j in range(m):
            x = j * cell_size
            y = i * cell_size
            if maze[i][j] == 0:
                screen.blit( pathImage, (x, y))
            elif maze[i][j] == 1:
                screen.blit(wallImage, (x, y))
  
    for event in pygame.event.get(): 
  
        if event.type == pygame.QUIT: 
            run = False
            pygame.quit() 
            quit() 

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                if posRatX > 0:
                    posRatX -= pixels

            if event.key == pygame.K_RIGHT:
                if posRatX < width - RAT_IMAGE_SIZE[0]:
                    posRatX += pixels

            if event.key == pygame.K_UP:
                if posRatY > 0:
                    posRatY -= pixels

            if event.key == pygame.K_DOWN:
                if posRatY < height - RAT_IMAGE_SIZE[1]:
                    posRatY += pixels
  
    pygame.display.update() 
    
    CHEESE_POSITION = (posCheeseX,posCheeseY)
 
    screen.fill(color)

    screen.blit(ratImage, RAT_POSITION)
    
    screen.blit(cheeseImage, CHEESE_POSITION)
 

