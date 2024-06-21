import pygame
import sys

pygame.init()

window_width = 800
window_height = 500
window_size = (window_width, window_height)

class Edward(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        sprite_sheet = pygame.image.load("eddamce.png")
        self.frames = []  # Store all frames from the sprite sheet
        self.current_frame_index = 0  # Index of the current frame
        self.load_frames(sprite_sheet, 64, 64)  # Load frames from the sprite sheet
        self.image = self.frames[self.current_frame_index]  # Set initial image
        self.rect = self.image.get_rect()
        self.rect.bottomleft = (74, window_height - 50)
        self.frame_delay = 20  # Adjust frame delay here
        self.frame_counter = 0

    def load_frames(self, sheet, frame_width, frame_height):
        for x in range(0, sheet.get_width(), frame_width):
            frame = self.get_image_from_sheet(sheet, x, 0, frame_width, frame_height)
            self.frames.append(frame)

    def get_image_from_sheet(self, sheet, x, y, width, height):
        image = pygame.Surface((width, height))
        image.blit(sheet, (0, 0), (x, y, width, height))
        image.set_colorkey((0, 0, 0))
        return image

    def update(self):
        self.frame_counter += 1
        if self.frame_counter >= self.frame_delay:
            self.frame_counter = 0
            # Change dancing frame (example: cycle through frames)
            self.current_frame_index = (self.current_frame_index + 1) % len(self.frames)
            self.image = self.frames[self.current_frame_index]

# Sprite
player = Edward()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

# Load background image
try:
    background_image = pygame.image.load('bg.png')
except pygame.error:
    background_image = pygame.Surface((window_width, window_height))
    background_image.fill((255, 0, 0))

# Initialize fonts
pygame.font.init()
font = pygame.font.SysFont(None, 36)

# Initialize screen
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("Ghaizar Bautista World")

# Button colors
button_color = (100, 100, 100)
hover_color = (150, 150, 150)

# Button dimensions
button_width = 250
button_height = 50

# Function to create buttons
def create_button(text, x, y, action):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x < mouse[0] < x + button_width and y < mouse[1] < y + button_height:
        pygame.draw.rect(screen, hover_color, (x, y, button_width, button_height))
        if click[0] == 1:
            if action == "start":
                start_game()
            elif action == "instructions":
                show_instructions()
            elif action == "controls":
                show_controls()
            elif action == "exit":
                pygame.quit()
                sys.exit()
    else:
        pygame.draw.rect(screen, button_color, (x, y, button_width, button_height))

    text_surface = font.render(text, True, (255, 255, 255))
    text_rect = text_surface.get_rect(center=(x + button_width / 2, y + button_height / 2))
    screen.blit(text_surface, text_rect)

# Function to start the game
def start_game():
    # Initialize game variables (player health, enemy health, etc.)
    player_health = 100
    enemy_health = 100
    player_turn = True

    # Main game loop
    while player_health > 0 and enemy_health > 0:
        # Handle events (e.g., key presses for choosing skill level)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                # Handle key presses for choosing skill level
                if event.key == pygame.K_1:
                    skill_level = 1
                    # Perform player action based on skill level
                    # Update enemy health accordingly
                elif event.key == pygame.K_2:
                    skill_level = 2
                    # Perform player action based on skill level
                    # Update enemy health accordingly
                elif event.key == pygame.K_3:
                    skill_level = 3
                    # Perform player action based on skill level
                    # Update enemy health accordingly

        # Perform enemy action
        # Update player health accordingly

        # Check win/lose conditions
        if player_health <= 0:
            print("You lose!")
            # Perform actions for losing the game (e.g., display game over screen)
        elif enemy_health <= 0:
            print("You win!")
            # Perform actions for winning the game (e.g., display victory screen)

        # Update game display (e.g., show player health, enemy health, etc.)
        pygame.display.update()


# Function to show instructions
def show_instructions():
    # Clear the screen
    screen.fill((0, 0, 0))

    # Text for instructions
    instructions_text = [
        "Instructions:",
        "1. You are the hero fighting against a monster.",
        "2. Each turn, you can choose a skill level from 1 to 3.",
        "3. Your skills have different damage ranges.",
        "4. The monster will attack you back.",
        "5. Your health and the monster's health are displayed.",
        "6. The game ends when either you or the monster's health reaches 0."
    ]

    # Render and display instructions text
    y_offset = 50
    for line in instructions_text:
        text_surface = font.render(line, True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=(window_width / 2, y_offset))
        screen.blit(text_surface, text_rect)
        y_offset += 30

    pygame.display.update()

# Function to show controller/hotkeys
def show_controls():
    # Clear the screen
    screen.fill((0, 0, 0))

    # Text for controller/hotkeys
    controls_text = [
        "Controller/Hotkeys:",
        "1. Choose skill level: 1, 2, or 3 - Use number keys 1, 2, 3",
        "2. Confirm selection: Enter key",
        "3. Exit game: Esc key"
    ]

    # Render and display controller/hotkeys text
    y_offset = 50
    for line in controls_text:
        text_surface = font.render(line, True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=(window_width / 2, y_offset))
        screen.blit(text_surface, text_rect)
        y_offset += 30

    pygame.display.update()

# Main menu loop
def main_menu():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.blit(background_image, (0, 0))
        all_sprites.update()  # Update sprite animation
        all_sprites.draw(screen)

        # Create buttons
        create_button("Start Game", 300, 150, "start")
        create_button("Instructions", 300, 225, "instructions")
        create_button("Controller/Hotkeys", 300, 300, "controls")
        create_button("Exit", 300, 375, "exit")

        # Handle button actions
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if click[0] == 1:
            if 300 < mouse[0] < 550 and 225 < mouse[1] < 275:
                show_instructions()
            elif 300 < mouse[0] < 550 and 300 < mouse[1] < 350:
                show_controls()

        pygame.display.update()

# Start the main menu
main_menu()
