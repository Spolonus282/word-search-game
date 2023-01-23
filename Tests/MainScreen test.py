import random, time, PlayersGui, Check, pygame, sys, Input, os.path, math
from pygame.locals import *
from PlayersGui import Players
File = open('Words.txt','a+')
pygame.init()

Clock = pygame.time.Clock()

iconSurf = pygame.image.load('GUIicon.png')
pygame.display.set_icon(iconSurf)

TestTime = 180
font = 'freesansbold.ttf'

BLACK     = (  0,   0,   0)
WHITE     = (255, 255, 255)
RED       = (255,   0,   0)
GREEN     = (  0, 255,   0)
BLUE      = (  0,   0, 128)
YELLOWISH = (238, 221, 130)

xSize = 800
ySize = 700
DISPSURF = pygame.display.set_mode((xSize, ySize))
pygame.display.set_caption('Word Search')

def Update(Surfaces, Wipe = False, WipeArea = None, Color = WHITE):
    global xSize, ySize, DISPSURF
    if Wipe:
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
            pygame.quit()
            sys.exit()
    for b in Surfaces:
        DISPSURF.blit(b[0], b[1])
    pygame.display.update()

def mainScreen():
    checkClick = False
    getMouse = pygame.mouse.get_pos()
    getClick = pygame.mouse.get_pressed()[0]
    PlayButton = Rect(xSize/2 - 25, ySize/2 - 25, 100, 50)
    resetRect = Rect(xSize/2 - 25, ySize/2 - 25, 110, 60)
    resetRect.center = (xSize/2, ySize/2)
    PlayButton.center = (xSize/2, ySize/2)
    PlayText = Input.DispText('Play!', font, 32, GREEN, YELLOWISH, True, 'center', (xSize/2, ySize/2))
    Update([PlayText], True, PlayButton, YELLOWISH)
    if PlayButton.left < getMouse[0] < PlayButton.right and PlayButton.top < getMouse[1] < PlayButton.bottom:
        PlayButton.size = (105, 55)
        PlayButton.center = (xSize/2, ySize/2)
        checkClick = True
    else:
        PlayButton.size = (100, 50)
        PlayButton.center = (xSize/2, ySize/2)
        checkClick = False
        DISPSURF.fill(WHITE, resetRect)
    Update([PlayText], True, PlayButton, YELLOWISH)
    if getClick == 1 and checkClick:
        return 'start'

DISPSURF.fill(WHITE)
Update([Input.DispText('yo', font, 32, BLUE, WHITE, True, 'topleft', (0,0))])
while True:
    startCheck = mainScreen()
    if startCheck == 'start':
        break
pygame.quit()
sys.exit()
