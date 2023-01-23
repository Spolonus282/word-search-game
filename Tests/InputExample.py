import pygame, sys, NewInput
from pygame.locals import *

pygame.init()
DISP = pygame.display.set_mode((400, 400))
pygame.display.set_caption('Input Example')
clock = pygame.time.Clock()

WHITE = (255, 255, 255)
BLUE  = (0,   0,   128)

keys   = 'Input:'

DISP.fill(WHITE)

while True:
    Objs = NewInput.DispText(keys, 12, BLUE, WHITE, 'center', (200, 200))
    keys = NewInput.Typed(keys, 10)
    if keys == 'return':
        pygame.quit()
        sys.exit()
    DISP.fill(WHITE)
    DISP.blit(Objs[0], Objs[1])
    pygame.display.update()
    clock.tick(30)
    for e in pygame.event.get():
        if e.type == QUIT:
            pygame.quit()
            sys.exit()
