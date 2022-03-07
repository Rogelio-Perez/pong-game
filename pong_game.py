import pygame

pygame.init()
black = (0, 0, 0)
white = (255, 255, 255)
screen_size = (800, 600)
screen = pygame.display.set_mode(screen_size)
clock = pygame.time.Clock()

player_width = 15
player_height = 90

player1_x_coor = 50
player1_y_coor = 300 - 45
player1_y_speed = 0

player2_x_coor = 750 - player_width
player2_y_coor = 300 - 45
player2_y_speed = 0

pelota_x = 400
pelota_y = 300
pelota_speed_x = 5
pelota_speed_y = 5

game_over = False

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                player1_y_speed = -5
            if event.key == pygame.K_s:
                player1_y_speed = 5
            if event.key == pygame.K_UP:
                player2_y_speed = -5
            if event.key == pygame.K_DOWN:
                player2_y_speed = 5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                player1_y_speed = 0
            if event.key == pygame.K_s:
                player1_y_speed = 0
            if event.key == pygame.K_UP:
                player2_y_speed = 0
            if event.key == pygame.K_DOWN:
                player2_y_speed = 0
    if pelota_y > 590 or pelota_y < 10:
        pelota_speed_y *= -1
    if pelota_x > 800:
        pelota_x = 400
        pelota_y = 300
        pelota_speed_x *= -1
        pelota_speed_y *= -1
    if pelota_x < 0:
        pelota_x = 400
        pelota_y = 300
        pelota_speed_x *= -1
        pelota_speed_y *= -1

    player1_y_coor += player1_y_speed
    player2_y_coor += player2_y_speed
    pelota_x += pelota_speed_x
    pelota_y += pelota_speed_y

    screen.fill(black)

    jugador1 = pygame.draw.rect(
        screen, white, (player1_x_coor, player1_y_coor, player_width, player_height))
    jugador2 = pygame.draw.rect(
        screen, white, (player2_x_coor, player2_y_coor, player_width, player_height))
    pelota = pygame.draw.circle(screen, white, (pelota_x, pelota_y), 10)

    if pelota.colliderect(jugador1) or pelota.colliderect(jugador2):
        pelota_speed_x *= -1

    if player1_y_coor > 510:
        player1_y_coor = 510
    if player2_y_coor > 510:
        player2_y_coor = 510
    if player1_y_coor < 0:
        player1_y_coor = 0
    if player2_y_coor < 0:
        player2_y_coor = 0

    pygame.display.flip()
    clock.tick(60)
pygame.quit()
