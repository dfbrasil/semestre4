import pygame

# Tamanho do labirinto (n x m)
n = 10
m = 10

# Matriz representando o labirinto (0 para espaço vazio, 1 para caminho)
maze = [
    [0, 0, 1, 1, 1, 0, 1, 1, 1, 0],
    [0, 1, 0, 1, 0, 0, 0, 0, 1, 0],
    [0, 1, 0, 1, 0, 1, 1, 1, 1, 1],
    [0, 1, 0, 1, 0, 1, 0, 0, 0, 0],
    [0, 1, 1, 1, 0, 1, 0, 1, 1, 0],
    [0, 0, 0, 0, 0, 1, 0, 0, 1, 0],
    [1, 1, 1, 1, 1, 1, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
    [1, 1, 1, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 1, 1, 1, 1, 1, 1, 1, 1]
]

# Inicialize o pygame
pygame.init()

# Tamanho da tela
size = width, height = 600, 600
screen = pygame.display.set_mode(size)

# Tamanho de cada célula
cell_size = width // n

# Event loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    for i in range(n):
        for j in range(m):
            x = j * cell_size
            y = i * cell_size
            if maze[i][j] == 0:
                # Se for 0, desenhe um espaço vazio
                pygame.draw.rect(screen, (255, 255, 255), (x, y, cell_size, cell_size))
            elif maze[i][j] == 1:
                # Se for 1, desenhe "|"
                font = pygame.font.Font(None, 36)
                text = font.render("|", True, (0, 0, 0))
                screen.blit(text, (x + cell_size // 2, y + cell_size // 2))

    pygame.display.flip()

# Encerre o pygame
pygame.quit()
