#deixar o caminho trilhado em vermelho até que o rato encontre o queijo.
#quando achar o queijo, fazer o pop na pilha para que o caminho seja percorrido de volta ao início pelo rato seja colorido, mas dessa vez com a cor verde.

import pygame
import time
from collections import deque

pygame.init()

directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

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
    h = len(maze)
    w = len(maze[0])
    return maze, h, w, posRatX, posRatY, posCheeseX, posCheeseY

maze, h, w, posRatX, posRatY, posCheeseX, posCheeseY = load_maze_from_file('maze_large.txt')

cell_size = min(1200 // w, 720 // h)
width = w * cell_size
height = h * cell_size

pygame.display.set_caption('Cheese Hunter')

Icon = pygame.image.load('/home/danieldfb/Repositório - NOVO/semestre4/EDL/RatChallenge/MazeGame/images/rat.png')
pygame.display.set_icon(Icon)

size = (width, height)
screen = pygame.display.set_mode(size)

# background screen color
color = (255, 255, 255)

ratImage = pygame.image.load('/home/danieldfb/Repositório - NOVO/semestre4/EDL/RatChallenge/MazeGame/images/rat.png')
cheeseImage = pygame.image.load('/home/danieldfb/Repositório - NOVO/semestre4/EDL/RatChallenge/MazeGame/images/cheese.png')
wallImage = pygame.image.load('/home/danieldfb/Repositório - NOVO/semestre4/EDL/RatChallenge/MazeGame/images/wall.png')

RAT_IMAGE_SIZE = (cell_size, cell_size)
CHEESE_IMAGE_SIZE = (cell_size, cell_size)
WALL_IMAGE_SIZE = (cell_size, cell_size)

# Redimensione a imagem para o tamanho necessário
ratImage = pygame.transform.scale(ratImage, RAT_IMAGE_SIZE)
cheeseImage = pygame.transform.scale(cheeseImage, CHEESE_IMAGE_SIZE)
wallImage = pygame.transform.scale(wallImage, WALL_IMAGE_SIZE)

# Inicialize as posições iniciais
posRatX = posRatX * cell_size
posRatY = posRatY * cell_size
posCheeseX = posCheeseX * cell_size
posCheeseY = posCheeseY * cell_size

pygame.time.wait(100) # Tempo pra inicializar a aplicação (em milissegundos)
pixels = cell_size  # Tamanho do movimento baseado na célula

visited_cells = [[False] * w for _ in range(h)]

def mark_visited(maze, posRatX, posRatY):
    # Marca a célula como visitada e retorna True
    visited_cells[posRatY // cell_size][posRatX // cell_size] = True
    return visited_cells

def clear_previous_movement(maze, rat_positions):
    # Remove a marcação de células visitadas durante o movimento anterior
    if len(rat_positions) > 1:
        prev_x, prev_y, _ = rat_positions[-2]
        maze[prev_y // cell_size][prev_x // cell_size] = 0  # Marca a célula anterior como não visitada

def get_valid_moves(posRatX, posRatY):
    moves = []
    for dx, dy in directions:
        new_x = posRatX + dx * cell_size
        new_y = posRatY + dy * cell_size
        new_x_index = new_x // cell_size
        new_y_index = new_y // cell_size

        if (
            0 <= new_x < width - RAT_IMAGE_SIZE[0]
            and 0 <= new_y < height - RAT_IMAGE_SIZE[1]
            and maze[new_y_index][new_x_index] in (0, 3)
            and not visited_cells[new_y_index][new_x_index]
        ):
            moves.append(((new_x, new_y), (dx, dy)))

    return moves

last_move_time = time.time()

# Crie uma pilha vazia para armazenar as posições do rato
rat_positions = deque()

# Crie uma lista para armazenar as coordenadas corretas do caminho do rato
correct_path = []

# Inicialize com uma direção padrão
last_direction = (1, 0)

found_cheese = False  # Variável de controle
message_display_time = None

font = pygame.font.Font(None, 36)  # Defina a fonte e o tamanho
text_color = 'red'  # Cor do texto

running = True

while running:
    # Limpe o fundo antes de desenhar
    screen.fill(color)

    for i in range(h):
        for j in range(w):
            x = j * cell_size
            y = i * cell_size
            if maze[i][j] == 1:
                screen.blit(wallImage, (x, y))

    current_time = time.time()

    if current_time - last_move_time > 0.05 and not found_cheese:
        valid_moves = get_valid_moves(posRatX, posRatY)

        if valid_moves:
            next_move, next_direction = valid_moves[0]
            new_x, new_y = next_move

            # Adicione a nova posição à lista de coordenadas corretas
            correct_path.append((posRatX, posRatY))

            # Atualize a posição e a direção
            posRatX = new_x
            posRatY = new_y
            last_direction = next_direction

            # Adicione a nova posição e direção à pilha
            rat_positions.append((posRatX, posRatY, last_direction))

            # Marque a célula como visitada
            mark_visited(maze, posRatX, posRatY)
        else:
            if len(rat_positions) > 1:
                # Remova o penúltimo movimento da pilha
                rat_positions.pop()

                # Recupere a última direção válida
                last_x, last_y, last_direction = rat_positions[-1]

                # Atualize a posição do rato
                posRatX = last_x
                posRatY = last_y

                # Adicione a nova posição à lista de coordenadas corretas
                correct_path.append((posRatX, posRatY))

            # Marque a célula como visitada
            mark_visited(maze, posRatX, posRatY)

        last_move_time = current_time

    screen.blit(ratImage, (posRatX, posRatY))
    screen.blit(cheeseImage, (posCheeseX, posCheeseY))

    # Exibir uma mensagem se o queijo foi encontrado
    if (posRatX, posRatY) == (posCheeseX, posCheeseY) and not found_cheese:
        found_cheese = True
        message_display_time = pygame.time.get_ticks()

    if message_display_time is not None:
        current_ticks = pygame.time.get_ticks()
        if current_ticks - message_display_time < 10000:  # Exibir por 10 segundos
            message = font.render("Rato encontrou o queijo!", True, text_color)
            screen.blit(message, (0, 0))
            for x, y in correct_path:
                pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(x, y, cell_size, cell_size))
            for x, y, _ in rat_positions:
                pygame.draw.rect(screen, (0, 0, 255), pygame.Rect(x, y, cell_size, cell_size))
                
            file_path = '/home/danieldfb/Repositório - NOVO/semestre4/EDL/RatChallenge/MazeGame/right_way.txt'
            with open(file_path, 'w') as file:
                for x, y in correct_path:
                    file.write(f"{x},{y}\n")
        else:
            message_display_time = None  # Ocultar a mensagem após 10 segundos
            
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            quit()
    
    pygame.display.update()
