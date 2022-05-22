import pygame
from sys import exit

def display_score():
    current_time = (pygame.time.get_ticks() - start_time) / 1000
    score_surface = test_font.render(str(current_time), False, (64,64,64))
    score_rect = score_surface.get_rect(center = (400,50))
    screen.blit(score_surface,score_rect)

pygame.init()
screen = pygame.display.set_mode((800, 400))
#set game window title
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()
test_font = pygame.font.Font('graphics/fonts/Pixeltype.ttf', 50)
game_active = True
start_time = 0

sky_surface = pygame.image.load('graphics/Sky.png').convert()
ground_surface = pygame.image.load('graphics/ground.png').convert()

#(text content, smoothing, color)
text_surface = test_font.render('My game', False, (64,64,64))
text_rect = text_surface.get_rect(center = (400, 50))

snail_surface = pygame.image.load('graphics/snail1.png').convert_alpha()
snail_rectangle = snail_surface.get_rect(midbottom = (850, 300))

player_surface = pygame.image.load('graphics/wizard_right.png').convert_alpha()
player_rectangle = player_surface.get_rect(midbottom = (80, 300))
player_gravity = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if game_active:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if player_rectangle.collidepoint(event.pos):
                    if player_rectangle.bottom >= 300:
                        player_gravity = -20
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if player_rectangle.bottom >= 300:
                        player_gravity = -20
        else:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_active = True
                    start_time = pygame.time.get_ticks()
    if game_active:
        screen.blit(sky_surface,(0, 0))
        screen.blit(ground_surface,(0, 300))
        display_score()
        # pygame.draw.rect(screen, '#c0e8ec', text_rect, 6)
        # pygame.draw.rect(screen, '#c0e8ec', text_rect)
        # pygame.draw.line(screen, 'Pink', (0, 0), pygame.mouse.get_pos())
        # screen.blit(text_surface,text_rect)
        snail_rectangle.left -= 4
        if snail_rectangle.left <= -90: snail_rectangle.left = 850
        screen.blit(snail_surface, snail_rectangle)

        # player
        player_gravity += 1
        player_rectangle.y += player_gravity
        if player_rectangle.bottom >= 300: player_rectangle.bottom = 300
        screen.blit(player_surface, player_rectangle)

        # collision
        if snail_rectangle.colliderect(player_rectangle):
            game_active = False
            snail_rectangle.left = 850

        #returns object containing all buttons and theit current state
        #keys = pygame.key.get_pressed()
        #if keys[pygame.K_SPACE]:
            #print('jump')

        #mouse_pos = pygame.mouse.get_pos()
        #if player_rectangle.collidepoint(mouse_pos):
            #print(pygame.mouse.get_pressed())
    else:
        screen.fill('Red')

    pygame.display.update()
    clock.tick(60)