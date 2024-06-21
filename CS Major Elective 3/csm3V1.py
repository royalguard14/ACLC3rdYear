'''Create a Windows Form with your name as the title
and insert a background image using Pygame'''

import pygame
import sys

pygame.init()

window_width = 800
window_height = 500
window_size = (window_width, window_height)

try:
    background_image = pygame.image.load('bg.png')
except pygame.error:
    background_image = pygame.Surface((window_width, window_height))
    background_image.fill((255, 0, 0))

screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("Ghaizar Bautista World")  

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.blit(background_image, (0, 0))
    pygame.display.flip()

pygame.quit()
sys.exit()
