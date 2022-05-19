import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800, 400))
#set game window title
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()
test_font = pygame.font.Font('graphics/fonts/Pixeltype.ttf', 50)

sky_surface = pygame.image.load('graphics/Sky.png').convert()
ground_surface = pygame.image.load('graphics/ground.png').convert()
#(text content, smoothing, color)
text_surface = test_font.render('My game', False, 'Black')

snail_surface = pygame.image.load('graphics/snail1.png').convert_alpha()
snail_rectangle = snail_surface.get_rect(midbottom = (850, 300))

player_surface = pygame.image.load('graphics/player_walk_1.png').convert_alpha()
player_rectangle = player_surface.get_rect(midbottom = (80, 300))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(sky_surface,(0, 0))
    screen.blit(ground_surface,(0, 300))
    screen.blit(text_surface,(300, 50))
    snail_rectangle.left -= 4
    if snail_rectangle.left <= -90: snail_rectangle.left = 850
    screen.blit(snail_surface, snail_rectangle)
    screen.blit(player_surface, player_rectangle)

    pygame.display.update()
    clock.tick(60)