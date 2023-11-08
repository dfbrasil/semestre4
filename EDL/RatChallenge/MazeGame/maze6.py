import pygame
import time

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

pygame.display.set_caption('Cheese Hunter')

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

def can_move(x, y):
    return 0 <= x < m and 0 <= y < n and maze[y][x] != 1

def move_rat(maze, posRatX, posRatY, path_stack):
    # Direções possíveis em ordem de prioridade
    directions = [(1, 0), (-1, 0), (0, -1), (0, 1)]
    for dx, dy in directions:
        new_x = posRatX // cell_size + dx
        new_y = posRatY // cell_size + dy
        if can_move(new_x, new_y) and (new_x, new_y) not in path_stack:
            path_stack.append((new_x, new_y))
            return new_x * cell_size, new_y * cell_size

    if len(path_stack) > 1:
        # Se não houver movimentos possíveis, volte um passo na pilha
        path_stack.pop()  # Remove a posição atual
        prev_x, prev_y = path_stack.pop()  # Volte para a posição anterior
        return prev_x * cell_size, prev_y * cell_size
    else:
        return posRatX, posRatY

path_stack = [(posRatX // cell_size, posRatY // cell_size)]
last_move_time = time.time()
found_cheese = False

font = pygame.font.Font(None, 36)  # Defina a fonte e o tamanho
text_color = 'red'  # Cor do texto

message_display_time = None

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

    if current_time - last_move_time > 0.1 and not found_cheese:  # 0.1 segundo
        posRatX, posRatY = move_rat(maze, posRatX, posRatY, path_stack)
        last_move_time = current_time

    screen.blit(cheeseImage, (posCheeseX, posCheeseY))
    screen.blit(ratImage, (posRatX, posRatY))

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
