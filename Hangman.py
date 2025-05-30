import pygame
import math
import random
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions and colors
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PURPLE = (128, 0, 128)
FPS = 60

# Create the screen
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hangman Game")

# Load images
images = [pygame.image.load(f"hangman{str(i)}.png") for i in range(7)]

# Fonts
LETTER_FONT = pygame.font.SysFont('comicsans', 40)
WORD_FONT = pygame.font.SysFont('comicsans', 40)
TITLE_FONT = pygame.font.SysFont('comicsans', 70)
BUTTON_FONT = pygame.font.SysFont('comicsans', 40)
SCORE_FONT = pygame.font.SysFont('comicsans', 40)

# Global button rectangles
new_game_rect = pygame.Rect(WIDTH/2 - 100, 0, 200, 50)
quit_game_rect = pygame.Rect(WIDTH/2 - 100, 0, 200, 50)
easy_rect = pygame.Rect(0, 200, 0, 50)
normal_rect = pygame.Rect(0, 200, 0, 50)
hard_rect = pygame.Rect(0, 200, 0, 50)
hint_rect = pygame.Rect(WIDTH - 200, HEIGHT - 50, 200, 50)

# Game variables
hangman_status = 0
words = [
    "BIRD", "BOOK", "LAMP", "TREE", "LAKE", "CLOUD", "HOUSE", "APPLE", "CHAIR", "TABLE",
    "MUSIC", "HAPPY", "BEACH", "RIVER", "LIGHT", "SMILE", "DREAM", "OCEAN", "COLOR", "SLEEP",
    "FLOWER", "PIANO", "PHONE", "HORSE", "EARTH", "DANCE", "PEACE", "SUNNY", "FRUIT", "GRAPE",
    "PARTY", "HEART", "POWER", "LAUGH", "FOREST", "GUITAR", "COOKIE", "COFFEE", "CAMERA", "SUNSET", "FRIEND",
    "MOUNTAIN", "JOURNEY", "SUMMER", "WINTER", "MORNING", "EVENING", "DIAMOND", "FREEDOM", "BUTTERFLY", "WHISPER",
    "CANDLE", "RAINBOW", "SILENCE", "FORTUNE", "GARDEN", "HARMONY", "BALLOON", "CHOCOLATE", "INSPIRE", "MEDITATE",
    "MIRACLE", "PARADISE", "PASSION", "SERENITY", "TRANQUIL", "DISCOVER", "ETERNITY", "INFINITY", "REFLECTION", "BLOSSOM",
    "BREATHE", "DELIGHT", "HEAVENLY", "ILLUMINATE", "MOONLIGHT", "NOSTALGIA", "OPTIMISM", "RADIANCE", "SPARKLE", "TWILIGHT",
    "WONDERFUL", "ADVENTURE", "BRILLIANT", "CELEBRATE", "WHOLESOME", "EFFERVESCENT", "FASCINATE", "MAGNIFICENT", "VIBRANT", "WHIMSICAL"
]

word = ""
guessed = set()
selected_difficulty = None
score = 0  # Add a variable for score

def select_difficulty():
    global selected_difficulty, easy_rect, normal_rect, hard_rect

    difficulty_rects = {
        "EASY": easy_rect,
        "NORMAL": normal_rect,
        "HARD": hard_rect
    }

    # Calculate the width of each button text
    easy_text_width = BUTTON_FONT.size("EASY")[0]
    normal_text_width = BUTTON_FONT.size("NORMAL")[0]
    hard_text_width = BUTTON_FONT.size("HARD")[0]

    # Calculate the total width required for spacing
    total_width = max(easy_text_width, normal_text_width, hard_text_width) + 40  # Added 40 for extra spacing

    # Calculate the initial y-coordinate for the buttons
    y_coordinate = (HEIGHT - len(difficulty_rects) * 50) / 2

    # Set the y-coordinates and width for each button rect
    for difficulty in difficulty_rects:
        text_width = BUTTON_FONT.size(difficulty)[0]
        difficulty_rects[difficulty].y = y_coordinate
        difficulty_rects[difficulty].x = (WIDTH - text_width) / 2
        difficulty_rects[difficulty].width = text_width + 20  # Added 20 for padding
        y_coordinate += 50 + 20  # Added 20 for vertical spacing

    while selected_difficulty is None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                for difficulty, rect in difficulty_rects.items():
                    if rect.collidepoint(mouse_x, mouse_y):
                        selected_difficulty = difficulty

        win.fill(WHITE)

        # Draw buttons in purple
        for difficulty, rect in difficulty_rects.items():
            pygame.draw.rect(win, PURPLE, rect)
            text = BUTTON_FONT.render(difficulty, 1, BLACK)
            win.blit(text, (rect.centerx - text.get_width() / 2, rect.centery - text.get_height() / 2))

        pygame.display.update()

def select_word():
    global word, selected_difficulty

    difficulty = {"EASY": (4, 6), "NORMAL": (7, 9), "HARD": (10, float('inf'))}
    min_length, max_length = difficulty[selected_difficulty]
    eligible_words = [w for w in words if min_length <= len(w) <= max_length]
    word = random.choice(eligible_words)

def draw():
    win.fill(WHITE)

    # Draw the title in purple
    text = TITLE_FONT.render("HANGMAN GAME", 1, PURPLE)
    win.blit(text, (WIDTH/2 - text.get_width()/2, 20))

    # Draw the word
    display_word = " ".join(letter if letter in guessed else "_" for letter in word)
    text = WORD_FONT.render(display_word, 1, BLACK)
    win.blit(text, (WIDTH/2 - text.get_width()/2, 300))

    # Draw the score in the center right
    score_text = SCORE_FONT.render(f"Score: {score}", 1, BLACK)
    score_y = HEIGHT // 2 - score_text.get_height() // 2  # Center the score table horizontally
    score_x = WIDTH - score_text.get_width() - 20  # Leave space on the right
    win.blit(score_text, (score_x, score_y))

    # Draw the buttons in purple
    for i, letter in enumerate("ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
        x = 50 + (i % 13) * 50
        y = 450 + (i // 13) * 50
        pygame.draw.circle(win, PURPLE, (x, y), 20, 3)
        text = LETTER_FONT.render(letter, 1, BLACK)
        win.blit(text, (x - text.get_width()/2, y - text.get_height()/2))

    # Draw the hint button
    pygame.draw.rect(win, PURPLE, hint_rect)
    hint_text = BUTTON_FONT.render("HINT", 1, BLACK)
    win.blit(hint_text, (hint_rect.centerx - hint_text.get_width()/2, hint_rect.centery - hint_text.get_height()/2))

    win.blit(images[hangman_status], (150, 100))
    pygame.display.update()

def display_message(message):
    global new_game_rect, quit_game_rect

    pygame.time.delay(1000)
    win.fill(WHITE)
    lines = message.split('\n')

    # Calculate the vertical space required for messages and buttons
    total_height = sum(text.get_height() + 10 for text in [WORD_FONT.render(line, 1, BLACK) for line in lines])
    total_height += new_game_rect.height + quit_game_rect.height + 20
    # Calculate the starting y-coordinate to center the content
    y = (HEIGHT - total_height) / 2

    for line in lines:
        text = WORD_FONT.render(line, 1, BLACK)
        win.blit(text, (WIDTH/2 - text.get_width()/2, y))
        y += text.get_height() + 10
    # Display the score on the "New Game" screen
    score_text = SCORE_FONT.render(f"Score: {score}", 1, BLACK)
    score_y = y + 20
    win.blit(score_text, (WIDTH/2 - score_text.get_width()/2, score_y))
    # Update button positions
    new_game_rect.y = score_y + score_text.get_height() + 20
    quit_game_rect.y = new_game_rect.y + 65

    pygame.draw.rect(win, PURPLE, new_game_rect)
    pygame.draw.rect(win, PURPLE, quit_game_rect)

    new_game_text = BUTTON_FONT.render("New Game", 1, BLACK)
    quit_game_text = BUTTON_FONT.render("Quit Game", 1, BLACK)

    win.blit(new_game_text, (WIDTH/2 - new_game_text.get_width()/2, new_game_rect.y + 25 - new_game_text.get_height()/2))
    win.blit(quit_game_text, (WIDTH/2 - quit_game_text.get_width()/2, quit_game_rect.y + 25 - quit_game_text.get_height()/2))

    pygame.display.update()

def reset_game():
    global hangman_status, guessed, selected_difficulty
    hangman_status = 0
    guessed = set()
    selected_difficulty = None

def show_hint():
    global guessed

    # Find an unguessed letter
    unguessed_letters = [letter for letter in word if letter not in guessed]
    if unguessed_letters:
        hint_letter = random.choice(unguessed_letters)
        guessed.add(hint_letter)

def main():
    global hangman_status, guessed, new_game_rect, quit_game_rect, selected_difficulty, score

    clock = pygame.time.Clock()
    run = True

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                m_x, m_y = pygame.mouse.get_pos()
                
                # Check if hint button is clicked
                if hint_rect.collidepoint(m_x, m_y):
                    show_hint()
                else:
                    for i, letter in enumerate("ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
                        x = 50 + (i % 13) * 50
                        y = 450 + (i // 13) * 50
                        dis = math.sqrt((x - m_x) ** 2 + (y - m_y) ** 2)
                        if dis < 20:
                            guessed.add(letter)
                            if letter not in word:
                                hangman_status += 1
                                score -= 10  # Decrease the score on incorrect guesses
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False

        if selected_difficulty is None:
            select_difficulty()
            select_word()

        draw()

        won = all(letter in guessed for letter in word)
        lost = hangman_status == 6

        if won or lost:
            if won:
                score += 50  # Increase the score when you win
                display_message("YOU WON!")
            elif lost:
                display_message(f"YOU LOST!\nCorrect word: {word}.")

            waiting_for_input = True
            while waiting_for_input:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        run = False
                        waiting_for_input = False
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        m_x, m_y = pygame.mouse.get_pos()
                        if new_game_rect.collidepoint(m_x, m_y):
                            reset_game()
                            waiting_for_input = False
                        elif quit_game_rect.collidepoint(m_x, m_y):
                            run = False
                            waiting_for_input = False

    pygame.quit()
    sys.exit()

