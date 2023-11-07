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

maze, n, m, posRatX, posRatY, posCheeseX, posCheeseY = load_maze_from_file('maze2.txt')

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

pygame.time.wait(100)
pixels = cell_size  # Tamanho do movimento baseado na célula

def move_rat(maze, posRatX, posRatY, last_direction):
    # Lógica para mover o rato automaticamente
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    possible_moves = []
    
    for dx, dy in directions:
        new_x = posRatX + dx * cell_size
        new_y = posRatY + dy * cell_size
        
        # Verifique se o movimento é válido (dentro dos limites e não é uma parede)
        if (0 <= new_x < width - RAT_IMAGE_SIZE[0]
            and 0 <= new_y < height - RAT_IMAGE_SIZE[1]
            and maze[new_y // cell_size][new_x // cell_size] in (0, 3)):  # Permita 'c' (cheese) e '0' (vazio)
            
            new_coord = (new_x, new_y)
            new_direction = (dx, dy)
            
            # Verifique se o movimento não foi feito anteriormente (coordenada e direção)
            if (new_coord, new_direction) not in posicoes_rato:
                possible_moves.append((new_coord, new_direction))
    
    if possible_moves:
        # Embaralhe a lista de movimentos possíveis
        import random
        random.shuffle(possible_moves)
        
        # Escolha o primeiro movimento disponível
        new_coord, new_direction = possible_moves[0]
        new_x, new_y = new_coord
        return new_x, new_y, new_direction  # Movimento possível, retornando a nova coordenada e direção
    
    if len(posicoes_rato) > 1:
        # Remove a posição e a direção atuais da pilha
        posicoes_rato.pop()
        posRatX, posRatY, last_direction = posicoes_rato.pop()
        return posRatX, posRatY, last_direction  # Retorna à posição e direção anterior
    
    return posRatX, posRatY, last_direction


last_move_time = time.time()

# Crie uma pilha vazia para armazenar as posições do rato
posicoes_rato = deque()

# Inicialize com uma direção padrão
last_direction = (1, 0)
posicoes_rato.append((posRatX, posRatY, last_direction))

found_cheese = False  # Variável de controle
message_display_time = None

font = pygame.font.Font(None, 36)  # Defina a fonte e o tamanho
text_color = 'red'  # Cor do texto

while running:
    # Limpe o fundo antes de desenhar
    screen.fill(color)

    for i in range(n):
        for j in range(m):
            x = j * cell_size
            y = i * cell_size
            if maze[i][j] == 0:
                screen.blit(pathImage, (x, y))
            elif maze[i][j] == 1:
                screen.blit(wallImage, (x, y))

    current_time = time.time()

    if current_time - last_move_time > 0.05 and not found_cheese:  # 0.1 segundo
        posRatX, posRatY, last_direction = move_rat(maze, posRatX, posRatY, last_direction)
        
        # Adicione a nova posição e direção à pilha
        posicoes_rato.append((posRatX, posRatY, last_direction))
        
        last_move_time = current_time

    screen.blit(ratImage, (posRatX, posRatY))
    screen.blit(cheeseImage, (posCheeseX, posCheeseY))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            quit()

 # Exibir uma mensagem se o queijo foi encontrado
    if (posRatX, posRatY) == (posCheeseX, posCheeseY) and not found_cheese:
        found_cheese = True
        message_display_time = pygame.time.get_ticks()

    if message_display_time is not None:
        current_ticks = pygame.time.get_ticks()
        if current_ticks - message_display_time < 10000:  # Exibir por 10 segundos
            message = font.render("Rato encontrou o queijo!", True, text_color)
            screen.blit(message, (10, 10))
        else:
            message_display_time = None  # Ocultar a mensagem após 10 segundos

    pygame.display.update()
