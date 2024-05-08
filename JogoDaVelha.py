import random
import pygame
import sys

# Inicialização do pygame
pygame.init()

# Definição de constantes
SCREEN_WIDTH = 300
SCREEN_HEIGHT = 300
LINE_COLOR = (0, 0, 0)
BG_COLOR = (255, 255, 255)
LINE_WIDTH = 4
FONT_SIZE = 30
LINE_COLOR_WIN = (255, 0, 0)

# Carregar efeitos sonoros
move_sound = pygame.mixer.Sound("move_sound.wav.mp3")
win_sound = pygame.mixer.Sound("win_sound.wav.mp3")

# Função para desenhar o tabuleiro
def draw_board(screen, board, winner_cells):
    for row in range(3):
        for col in range(3):
            pygame.draw.rect(screen, LINE_COLOR, (col*100, row*100, 100, 100), LINE_WIDTH)
            font = pygame.font.SysFont(None, FONT_SIZE)
            text = font.render(board[row][col], True, LINE_COLOR)
            screen.blit(text, (col*100 + 35, row*100 + 35))
    
    if winner_cells:
        start_row, start_col = winner_cells[0]
        end_row, end_col = winner_cells[2]
        pygame.draw.line(screen, LINE_COLOR_WIN, (start_col*100 + 50, start_row*100 + 50), (end_col*100 + 50, end_row*100 + 50), 5)

# Função para verificar o vencedor
def check_winner(board, player):
    for i in range(3):
        if all(board[i][j] == player for j in range(3)):
            return [(i, 0), (i, 1), (i, 2)]
        
        if all(board[j][i] == player for j in range(3)):
            return [(0, i), (1, i), (2, i)]
    
    if all(board[i][i] == player for i in range(3)):
        return [(0, 0), (1, 1), (2, 2)]
    
    if all(board[i][2-i] == player for i in range(3)):
        return [(0, 2), (1, 1), (2, 0)]
    
    return None

# Função para verificar empate
def check_draw(board):
    for row in board:
        if " " in row:
            return False
    return True

# Função principal do jogo
def main():
    # Load background music
    pygame.mixer.music.load("background_music.mp3")
    pygame.mixer.music.play(-1)  # Play music in a loop

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Jogo da Velha")
    
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ['X', 'O']
    player = random.choice(players)

    winner_cells = None

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN and not winner_cells:
                col = event.pos[0] // 100
                row = event.pos[1] // 100

                if board[row][col] == " ":
                    board[row][col] = player
                    move_sound.play()

                    player = players[1] if player == players[0] else players[0]

                    winner_cells = check_winner(board, player)

                    if winner_cells:
                        print(f"Parabéns! O jogador '{player}' venceu!")
                        win_sound.play()
                        pygame.time.wait(2000)

                    if check_draw(board):
                        print("Empate! Ambos são mestres do jogo!")
                        pygame.quit()
                        sys.exit()

        screen.fill(BG_COLOR)
        draw_board(screen, board, winner_cells)
        pygame.display.flip()


if __name__ == "__main__":
    main()
