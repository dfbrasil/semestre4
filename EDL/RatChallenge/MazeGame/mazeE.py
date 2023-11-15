#importação de bibliotecas
import pygame
import time
from collections import deque

pygame.init()

# Definição das direções possíveis para o movimento do rato (Direita, Esqueda, Cima, Baixo respectivamente)
directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

#função para carregar o labirinto a partir de um txt.
def load_maze_from_file(filename):
    maze = []
    posRatX, posRatY = 0, 0
    posCheeseX, posCheeseY = 0, 0

    #Lê o arquivo linha a linha e preenche a matriz 'maze' de acordo com as condicionais muro, caminho, queijo e rato
    with open(filename, 'r') as file:
        for i, line in enumerate(file):
            row = []
            for j, char in enumerate(line.strip()):
                if char == '0':
                    row.append(0)
                elif char == '1':
                    row.append(1)
                elif char == 'm':
                    row.append('m')
                    posRatX, posRatY = j, i
                elif char == 'c':
                    row.append('c')
                    posCheeseX, posCheeseY = j, i
            maze.append(row)
    h = len(maze)
    w = len(maze[0])
    return maze, h, w, posRatX, posRatY, posCheeseX, posCheeseY

#carrega as variáveis e o labirinto à partir do arquivo
maze, h, w, posRatX, posRatY, posCheeseX, posCheeseY = load_maze_from_file('maze.txt')

#redimensionamento das células baseado na resolução da tela
cell_size = min(1200 // w, 720 // h)
width = w * cell_size
height = h * cell_size

# Configurações da janela
Icon = pygame.image.load('/home/danieldfb/Repositório - NOVO/semestre4/EDL/RatChallenge/MazeGame/images/rat.png')
pygame.display.set_icon(Icon)
size = (width, height)
screen = pygame.display.set_mode(size)

# Cor de fundo da tela
color = (255, 255, 255)

# Carregar as imagens do rato, queijo e parede
ratImage = pygame.image.load('/home/danieldfb/Repositório - NOVO/semestre4/EDL/RatChallenge/MazeGame/images/rat.png')
cheeseImage = pygame.image.load('/home/danieldfb/Repositório - NOVO/semestre4/EDL/RatChallenge/MazeGame/images/cheese.png')
wallImage = pygame.image.load('/home/danieldfb/Repositório - NOVO/semestre4/EDL/RatChallenge/MazeGame/images/wall.png')

# Define os tamanhos das imagens - altura e largura
RAT_IMAGE_SIZE = (cell_size, cell_size)
CHEESE_IMAGE_SIZE = (cell_size, cell_size)
WALL_IMAGE_SIZE = (cell_size, cell_size)

# Redimensione a imagem para o tamanho necessário
ratImage = pygame.transform.scale(ratImage, RAT_IMAGE_SIZE)
cheeseImage = pygame.transform.scale(cheeseImage, CHEESE_IMAGE_SIZE)
wallImage = pygame.transform.scale(wallImage, WALL_IMAGE_SIZE)

# Inicializa as posições iniciais do rato e do queijo
posRatX = posRatX * cell_size
posRatY = posRatY * cell_size
posCheeseX = posCheeseX * cell_size
posCheeseY = posCheeseY * cell_size

# Tempo em pra inicializar a aplicação
pygame.time.wait(100) 

# Tamanho do movimento baseado na célula
pixels = cell_size

# Inicializa a matriz de células visitadas
visited_cells = [[False] * w for _ in range(h)]

# Marca uma célula como visitada e retorna True
def mark_visited(posRatX, posRatY): #valores em pixels
    # Marca a célula como visitada e retorna True
    visited_cells[posRatY // cell_size][posRatX // cell_size] = True
    return visited_cells

# Remove a marcação de células visitadas durante o movimento anterior
def clear_previous_movement(maze, rat_positions):
    # Remove a marcação de células visitadas durante o movimento anterior
    if len(rat_positions) > 1:
        prev_x, prev_y, _ = rat_positions[-2]
        maze[prev_y // cell_size][prev_x // cell_size] = 0  # Marca a célula anterior como não visitada

# Obtém os movimentos válidos para o rato
def get_valid_moves(posRatX, posRatY):
    moves = []
    for dx, dy in directions:
        new_x = posRatX + dx * cell_size
        new_y = posRatY + dy * cell_size
        new_x_index = new_x // cell_size
        new_y_index = new_y // cell_size

        if (
            maze[new_y_index][new_x_index] in (0, 'c')
            and not visited_cells[new_y_index][new_x_index]
        ):
            moves.append(((new_x, new_y), (dx, dy)))

    return moves

# Inicializa o tempo do último movimento
last_move_time = time.time()

# Crie uma pilha vazia para armazenar as posições do rato
rat_positions = deque()

# Crie uma lista para armazenar as coordenadas corretas do caminho do rato
correct_path = []

# Inicialize com uma direção padrão
last_direction = (1, 0)

# Variável de controle para indicar se o queijo foi encontrado
found_cheese = False

# Tempo de exibição dos caminhos
path_display_time = None

# Loop principal da aplicação
running = True
while running:
    # Limpa o fundo em cada movimento do rato
    screen.fill(color)

    # Desenha as paredes do labirinto
    for i in range(h):
        for j in range(w):
            x = j * cell_size
            y = i * cell_size
            if maze[i][j] == 1:
                screen.blit(wallImage, (x, y))

    current_time = time.time()
    
    # Realiza um movimento do rato a cada 0.05 segundos
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
            mark_visited(posRatX, posRatY)
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
            mark_visited(posRatX, posRatY)

        last_move_time = current_time

    # Desenha o rato e o queijo na tela
    screen.blit(ratImage, (posRatX, posRatY))
    screen.blit(cheeseImage, (posCheeseX, posCheeseY))

    # Exibir uma mensagem se o queijo foi encontrado
    if (posRatX, posRatY) == (posCheeseX, posCheeseY) and not found_cheese:
        found_cheese = True
        path_display_time = pygame.time.get_ticks()
        pygame.display.set_caption('Cheese Hunter - Rato encontrou o queijo!')

    # Exibe a trilha correta do rato e salva em um arquivo
    if path_display_time is not None:
        current_ticks = pygame.time.get_ticks()
        if current_ticks - path_display_time < 10000:  # Exibir as trilhas por 10 segundos
            for x, y in correct_path:
                pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(x, y, cell_size, cell_size))
            for x, y, _ in rat_positions:
                pygame.draw.rect(screen, (0, 0, 255), pygame.Rect(x, y, cell_size, cell_size))
                
            file_path = '/home/danieldfb/Repositório - NOVO/semestre4/EDL/RatChallenge/MazeGame/right_way.txt'
            with open(file_path, 'w') as file:
                for x, y in correct_path:
                    file.write(f"{x},{y}\n")
        else:
            path_display_time = None
    
    # Exibe mensagem enquanto o queijo não é encontrado
    if found_cheese == False:
        current_ticks = pygame.time.get_ticks()
        pygame.display.set_caption('Cheese Hunter - Rato NÃO encontrou o queijo!')

    # Captura eventos do pygame
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            quit()
    
    # Atualiza a tela
    pygame.display.update()
