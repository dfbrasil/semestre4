import pygame
import time
from collections import deque


pygame.init()

def load_maze_from_file(filename):
    maze = []
    posRatX, posRatY = 0, 0
    posCheeseX, posCheeseY = 0, 0

    with open(filename, 'r') as file:
        for i, line in enumerate(file):
            row = []
            for j, char in enumerate(line.strip()):
                if char == '0':
                    row.append(0)
                elif char == '1':
                    row.append(1)
                elif char == 'm':
                    row.append(2)
                    posRatX, posRatY = j, i
                elif char == 'c':
                    row.append(3)
                    posCheeseX, posCheeseY = j, i
            maze.append(row)
    n = len(maze)
    m = len(maze[0])
    return maze, n, m, posRatX, posRatY, posCheeseX, posCheeseY

maze, n, m, posRatX, posRatY, posCheeseX, posCheeseY = load_maze_from_file('maze.txt')

cell_size = min(800 // m, 600 // n)
width = m * cell_size
height = n * cell_size

pygame.display.set_caption('Maze Hunter')

Icon = pygame.image.load('/home/danieldfb/Repositório - NOVO/semestre4/EDL/RatChallenge/MazeGame/images/rat.png')
pygame.display.set_icon(Icon)

size = (width, height)
screen = pygame.display.set_mode(size)

# background screen color
color = (0, 0, 0)

ratImage = pygame.image.load('/home/danieldfb/Repositório - NOVO/semestre4/EDL/RatChallenge/MazeGame/images/rat.png')
cheeseImage = pygame.image.load('/home/danieldfb/Repositório - NOVO/semestre4/EDL/RatChallenge/MazeGame/images/cheese.png')
pathImage = pygame.image.load('/home/danieldfb/Repositório - NOVO/semestre4/EDL/RatChallenge/MazeGame/images/path.jpg')
wallImage = pygame.image.load('/home/danieldfb/Repositório - NOVO/semestre4/EDL/RatChallenge/MazeGame/images/wall.png')

RAT_IMAGE_SIZE = (40, 40)
CHEESE_IMAGE_SIZE = (40, 40)
PATH_IMAGE_SIZE = (50, 50)
WALL_IMAGE_SIZE = (50, 50)

# Redimensione a imagem para o tamanho necessário
ratImage = pygame.transform.scale(ratImage, RAT_IMAGE_SIZE)
cheeseImage = pygame.transform.scale(cheeseImage, CHEESE_IMAGE_SIZE)
pathImage = pygame.transform.scale(pathImage, PATH_IMAGE_SIZE)
wallImage = pygame.transform.scale(wallImage, WALL_IMAGE_SIZE)

# Inicialize as posições iniciais
posRatX = posRatX * cell_size
posRatY = posRatY * cell_size
posCheeseX = posCheeseX * cell_size
posCheeseY = posCheeseY * cell_size

RAT_POSITION = (posRatX, posRatY)
CHEESE_POSITION = (posCheeseX, posCheeseY)

running = True

pygame.time.wait(1000)
pixels = cell_size  # Tamanho do movimento baseado na célula

def move_rat(maze, posRatX, posRatY):
    # Lógica para mover o rato automaticamente
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    
    for dx, dy in directions:
        new_x = posRatX + dx * cell_size
        new_y = posRatY + dy * cell_size
        if 0 <= new_x < width - RAT_IMAGE_SIZE[0] and 0 <= new_y < height - RAT_IMAGE_SIZE[1] and maze[new_y // cell_size][new_x // cell_size] == 0:
            return new_x, new_y  # Movimento possível
    
    return posRatX, posRatY  # Não foi possível mover

last_move_time = time.time()

# Crie uma pilha vazia para armazenar as posições do rato
rat_positions = deque()

while running:
    for i in range(n):
        for j in range(m):
            x = j * cell_size
            y = i * cell_size
            if maze[i][j] == 0:
                screen.blit(pathImage, (x, y))
            elif maze[i][j] == 1:
                screen.blit(wallImage, (x, y))
    
    current_time = time.time()
    
    rat_positions.append((posRatX, posRatY))
    
    if current_time - last_move_time > 1:  # 1 segundo
        posRatX, posRatY = move_rat(maze, posRatX, posRatY)
        last_move_time = current_time

    screen.blit(ratImage, (posRatX, posRatY))
    screen.blit(cheeseImage, (posCheeseX, posCheeseY))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            quit()

    pygame.display.update()

    screen.fill(color)
