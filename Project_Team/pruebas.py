import pygame
SCREEN_SIZE = (1000, 560)
NEGRO = (50, 50, 50)
AMARILLO = (255, 255, 0)
player_height = 104
player_width = 59
pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("Project Team")
clock = pygame.time.Clock()
font = pygame.font.Font(pygame.font.get_default_font(), 24)
player_image = pygame.image.load("assets/personajes/alejo_1.png")
player_x = 300
player_y = 190
player_speed = 0
player_aceleracion = 0.2
plataforma = pygame.image.load("assets/plataforma.png")
plataformas = [
    pygame.Rect(100, 300, 64, 64),
    pygame.Rect(164, 300, 64, 64),
    pygame.Rect(228, 300, 64, 64),
    pygame.Rect(292, 300, 64, 64),
    pygame.Rect(356, 300, 64, 64),
    pygame.Rect(420, 300, 64, 64),
    pygame.Rect(100, 236, 64, 64),
    pygame.Rect(420, 236, 64, 64),
]
coin = pygame.image.load("assets/objetos/moneda_0.png")
coins = [
    pygame.Rect(110, 185, 46, 46),
    pygame.Rect(430, 185, 46, 46)
]
score = 0
enemy = pygame.image.load("assets/personajes/esbirros_1.png")
enemies = [
    pygame.Rect(170, 240, 64, 61),
]
vidas = 3
vida_image = pygame.image.load("assets/vida.png")
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    new_player_x = player_x
    new_player_y = player_y
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_a]:
        new_player_x -= 2
    if teclas[pygame.K_d]:
        new_player_x += 2
    if teclas[pygame.K_w] and player_on_ground:
        player_speed = -7
    new_player_rect = pygame.Rect(new_player_x, player_y, player_width, player_height)
    x_colision = False
    for p in plataformas:
        if p.colliderect(new_player_rect):
            x_colision = True
            break
    if x_colision == False:
        player_x = new_player_x
    player_speed += player_aceleracion
    new_player_y += player_speed
    new_player_rect = pygame.Rect(player_x, new_player_y, player_width, player_height)
    y_colision = False
    player_on_ground = False
    for p in plataformas:
        if p.colliderect(new_player_rect):
            y_colision = True
            player_speed = 0
            if p[1] > new_player_y:
                player_y = p[1] - player_height
                player_on_ground = True
            break
    if y_colision == False:
        player_y = new_player_y
    player_rect = pygame.Rect(player_x, player_y, player_width, player_height)
    for c in coins:
        if c.colliderect(player_rect):
            coins.remove(c)
            score +=1
    for e in enemies:
        if e.colliderect(player_rect):
            player_x = 300
            player_y = 190
            player_speed = 0
            vidas -=1
    screen.fill(NEGRO)
    for p in plataformas:
        screen.blit(plataforma, (p.x, p.y))
    for c in coins:
        screen.blit(coin, (c.x, c.y))
    for e in enemies:
        screen.blit(enemy, (e.x, e.y))
    screen.blit(player_image, (player_x, player_y))
    score_text = font.render("score: " + str(score), True, AMARILLO,NEGRO)
    score_text_rectangle = score_text.get_rect()
    score_text_rectangle.topleft = (10,10)
    screen.blit(score_text, score_text_rectangle)
    for l in range(vidas):
        screen.blit(vida_image, (10 + (l*50), 45))
    pygame.display.flip()
    clock.tick(60)
pygame.quit()