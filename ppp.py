import pygame, math
pygame.init()
size = width, height = 201, 201
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
running = True
rc = False
v = 0
fps = 60
posis = [75, 105]

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                v += 50
            elif event.button == 3:
                v -= 50
    screen.fill((0, 0, 0))
    pygame.draw.circle(screen, pygame.Color('white'), (100, 100), 10)
    pygame.draw.polygon(screen, pygame.Color('white'),
                        [(int(100 + 70 * math.cos(math.radians(posis[0]))),
                          int(100 - 70 * math.sin(math.radians(posis[0])))),
                         (int(100 + 70 * math.cos(math.radians(posis[1]))),
                          int(100 - 70 * math.sin(math.radians(posis[1])))), (100, 100)])
    pygame.draw.polygon(screen, pygame.Color('white'),
                        [(int(100 + 70 * math.cos(math.radians(posis[0] + 120))),
                          int(100 - 70 * math.sin(math.radians(posis[0] + 120)))),
                         (int(100 + 70 * math.cos(math.radians(posis[1] + 120))),
                          int(100 - 70 * math.sin(math.radians(posis[1] + 120)))), (100, 100)])
    pygame.draw.polygon(screen, pygame.Color('white'),
                        [(int(100 + 70 * math.cos(math.radians(posis[0] + 240))),
                          int(100 - 70 * math.sin(math.radians(posis[0] + 240)))),
                         (int(100 + 70 * math.cos(math.radians(posis[1] + 240))),
                          int(100 - 70 * math.sin(math.radians(posis[1] + 240)))), (100, 100)])
    posis = [i % 360 + v / fps for i in posis]
    clock.tick(fps)
    pygame.display.flip()