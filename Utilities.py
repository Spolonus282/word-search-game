# import and initialize globals
import math, time, pygame, sys, Input
from pygame.locals import *
pygame.init()
Clock = pygame.time.Clock()
font = 'freesansbold.ttf'
xSize = 800
ySize = 700

# Color globals
BLACK     = (  0,   0,   0)
WHITE     = (255, 255, 255)
RED       = (255,   0,   0)
GREEN     = (  0, 255,   0)
BLUE      = (  0,   0, 128)
YELLOWISH = (238, 221, 130)
BROWNED   = (245, 222, 179)

# Globals to edit
DISPSURF = ''
File = ''
file2 = ''
Pending = ''
Pend = ''

def checkTimer(init, TestTime):
    'check for timeup, then display timer'
    c = TestTime - (time.clock() - init)
    e = [math.floor(c/60), math.floor(c % 60)]
    if e[1] == 0:
        e[1] = '00'
    elif e[1] < 10:
        f = str(e[1])
        e[1] = '0'
        e[1] += f
    elif e[0] < 0:
        e[0] = 0
        e[1] = '00'
    e[1] = str(e[1])
    e[0] = str(e[0])
    d = ':'.join(e)
    b = Input.DispText(d, font, 32, BLUE, BROWNED, True, 'center', (xSize/2, 625))
    if time.clock() - init >= TestTime:
        return [True, b]
    return [False, b]

def Lower(letters):
    'letters -> lowercase letters'
    b = []
    for a in letters:
        b.append(a.lower())
    if isinstance(letters, str):
        return ''.join(b)
    else:
        return b

def Sleep(Time):
    wait = time.clock()
    PastTime = 0.0
    while Time >= PastTime:
        Update([])
        PastTime = time.clock() - wait

def Update(Surfaces = [], Wipe = False, WipeArea = None, Color = BROWNED):
    'Update Screen'
    if Wipe:
        if isinstance(WipeArea, list):
            for c in WipeArea:
                DISPSURF.fill(Color, c)
        else:
            DISPSURF.fill(Color, WipeArea)
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            try:
                a = file2[1]
                b = file2[0]
                loadWord = a[b].bestWord
                loadHigh = str(a[b].high)
                loadScore = str(a[b].bestScore)
                load = ','.join([loadWord, loadHigh, loadScore])
                file2[2].write(load)
                file2[2].close()
            except NameError:
                File
            File.close()
            Pending.write(','.join(Pend))
            Pending.close()
            pygame.quit()
            sys.exit()
    for b in Surfaces:
        DISPSURF.blit(b[0], b[1])
    pygame.display.update()
    Clock.tick(75)
