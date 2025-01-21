import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 600, 600
LINE_WIDTH = 5
TILE_SIZE = WIDTH // 3
BG_COLOR = (255, 255, 255)  # White
LINE_COLOR = (0, 0, 0)  # Black
X_COLOR = (0, 0, 255)  # Blue
O_COLOR = (255, 0, 0)  # Red
FONT_SIZE = 100

# Setup screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Toe")
screen.fill(BG_COLOR)

# Font for drawing Xs and Os
font = pygame.font.Font(None, FONT_SIZE)

# Game variables
board = [["" for _ in range(3)] for _ in range(3)]  # 3x3 grid
current_player = "X"
game_over = False
winner = None

# Function to draw grid lines
def draw_grid():
    for i in range(1, 3):
        # Vertical lines
        pygame.draw.line(screen, LINE_COLOR, (i * TILE_SIZE, 0), (i * TILE_SIZE, HEIGHT), LINE_WIDTH)
        # Horizontal lines
        pygame.draw.line(screen, LINE_COLOR, (0, i * TILE_SIZE), (WIDTH, i * TILE_SIZE), LINE_WIDTH)

# Function to draw X or O
def draw_mark():
    for row in range(3):
        for col in range(3):
            if board[row][col] == "X":
                text_surface = font.render("X", True, X_COLOR)
            elif board[row][col] == "O":
                text_surface = font.render("O", True, O_COLOR)
            else:
                continue
            text_rect = text_surface.get_rect(center=(col * TILE_SIZE + TILE_SIZE // 2, row * TILE_SIZE + TILE_SIZE // 2))
            screen.blit(text_surface, text_rect)

# Function to check for a winner
def check_winner():
    global game_over, winner

    # Check rows and columns
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != "":
            winner = board[i][0]
            game_over = True
        if board[0][i] == board[1][i] == board[2][i] != "":
            winner = board[0][i]
            game_over = True

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != "":
        winner = board[0][0]
        game_over = True
    if board[0][2] == board[1][1] == board[2][0] != "":
        winner = board[0][2]
        game_over = True

    # Check for a draw
    if not any("" in row for row in board) and not game_over:
        game_over = True
        winner = "Draw"

# Function to restart the game
def restart_game():
    global board, current_player, game_over, winner
    board = [["" for _ in range(3)] for _ in range(3)]
    current_player = "X"
    game_over = False
    winner = None
    screen.fill(BG_COLOR)
    draw_grid()

# Draw the initial grid
draw_grid()

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            x, y = event.pos
            row, col = y // TILE_SIZE, x // TILE_SIZE

            if board[row][col] == "":
                board[row][col] = current_player
                current_player = "O" if current_player == "X" else "X"
                check_winner()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:  # Press 'R' to restart
                restart_game()

    # Update screen
    screen.fill(BG_COLOR)
    draw_grid()
    draw_mark()

    # Display winner
    if game_over:
        result_text = f"{winner} Wins!" if winner != "Draw" else "It's a Draw!"
        text_surface = font.render(result_text, True, (0, 255, 0))
        text_rect = text_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        screen.blit(text_surface, text_rect)

    pygame.display.flip()
