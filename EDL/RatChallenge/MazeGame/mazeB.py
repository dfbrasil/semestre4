import pygame
import random

# Constantes
WIDTH = 800
HEIGHT = 600
LIMITE_TEMPO = 10

# Inicializa o Pygame
pygame.init()

# Cria a tela
tela = pygame.display.set_mode((WIDTH, HEIGHT))

# Carrega as imagens
parede = pygame.image.load('/home/danieldfb/Repositório - NOVO/semestre4/EDL/RatChallenge/MazeGame/images/wall.png')
rato = pygame.image.load('/home/danieldfb/Repositório - NOVO/semestre4/EDL/RatChallenge/MazeGame/images/rat.png')
queijo = pygame.image.load('/home/danieldfb/Repositório - NOVO/semestre4/EDL/RatChallenge/MazeGame/images/cheese.png')

# Cria o labirinto
labirinto = []
for i in range(HEIGHT):
    linha = []
    for j in range(WIDTH):
        if i % 2 == 0 and j % 2 == 0:
            linha.append(parede)
        else:
            linha.append(None)
    labirinto.append(linha)

# Posiciona o rato no início do labirinto
rato_x = 0
rato_y = 0

# Pilha para armazenar os passos do rato
pilha = []

# Lista para armazenar os passos já dados pelo rato
passos_dados = []

# Contador do tempo
tempo = 0

direcoes = [(0, 1), (0, -1), (1, 0), (-1, 0)]

# Loop principal
while True:
    # Limpa a tela
    tela.fill((0, 0, 0))

    # Desenha o labirinto
    for i in range(HEIGHT):
        for j in range(WIDTH):
            if labirinto[i][j] is not None:
                tela.blit(labirinto[i][j], (j * 50, i * 50))

    # Desenha o rato
    tela.blit(rato, (rato_x * 50, rato_y * 50))

    # Verifica se o rato encontrou o queijo
    if labirinto[rato_y][rato_x] == queijo:
        print("O rato encontrou o queijo!")
        break

    # Verifica se o tempo limite foi atingido
    # if tempo >= LIMITE_TEMPO:
    #     print("O rato não encontrou o queijo a tempo!")
    #     break

    # Verifica se o rato está em uma parede
    if labirinto[rato_y][rato_x] is not None:
        # O rato está em uma parede, então ele deve retornar pelo caminho da pilha
        if len(pilha) > 0:
            # Pega o último passo da pilha
            passo = pilha.pop()

            # Atualiza a posição do rato
            rato_x = passo[0]
            rato_y = passo[1]

    # Verifica o próximo passo possível do rato
    passo_possivel = False
    for i in range(4):
        nova_x = rato_x + direcoes[i][0]
        nova_y = rato_y + direcoes[i][1]

        # Verifica se o passo é possível
        if 0 <= nova_x < WIDTH and 0 <= nova_y < HEIGHT and labirinto[nova_y][nova_x] is None:
            # Verifica se o passo já foi dado
            if (nova_x, nova_y) not in passos_dados:
                # O passo é possível e não foi dado antes
                passo_possivel = True
                passo = (nova_x, nova_y)
                break

    # Se houver um passo possível, o rato avança
    if passo_possivel:
        # Empilha o passo atual
        pilha.append((rato_x, rato_y))

        # Atualiza a posição do rato
        rato_x = passo[0]
        rato_y = passo[1]
        passos_dados.append((rato_x, rato_y))

    # Atualiza o contador do tempo
    tempo += 1

    # Atualiza a tela
    pygame.display.update()

    # Verifica se o usuário fechou a janela
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit
