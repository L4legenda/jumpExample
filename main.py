import pygame

sc = pygame.display.set_mode((600, 400))

playerx = 40
playery = 400 - 64

isJumpUp = False
isJumpDown = False
startY = 0
maxJump = 100

game = True
while game:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            game = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_a]:
        playerx -= 2
    if keys[pygame.K_d]:
        playerx += 2
    if keys[pygame.K_SPACE]:
        if not isJumpUp and not isJumpDown:
            startY = playery
        isJumpUp = True

    if isJumpUp:
        playery -= 2

    if isJumpDown:
        playery += 2

    if isJumpUp and playery <= startY - maxJump:
        isJumpUp = False
        isJumpDown = True

    if isJumpDown and playery >= startY:
        isJumpDown = False


    sc.fill((255, 255, 255))

    pygame.draw.rect(sc, (0, 255, 0), (playerx, playery, 64, 64))

    pygame.display.update()
    pygame.time.delay(20)
