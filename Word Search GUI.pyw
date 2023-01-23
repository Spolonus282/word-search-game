''' =========== Word Search ============
*** Created by Sam Polonus
*** This game is free-to-use and edit.
*** Created on February 23, 2017.
*** No other sources were used.
'''

# Import and initialize
import pygame, PlayersGui, Check, Input, Utilities, Game, Dictionary, MainScreen, MultiGame
from pygame.locals import *
File = open('Docs/Dictionary.txt','a+')
Pending = open('Docs/Pending.txt','r')
Pending.seek(0)
Pend = Pending.read().split(',')
Pending = open('Docs/Pending.txt', 'w+')
pygame.init()

# Initialize clock
Clock = pygame.time.Clock()

# Load up images
Play = [pygame.image.load('Images/PlayButton0.png'), pygame.image.load('Images/PlayButton1.png')]
Dict = [pygame.image.load('Images/DictButton0.png'), pygame.image.load('Images/DictButton1.png')]
Help = [pygame.image.load('Images/HelpButton0.png'), pygame.image.load('Images/HelpButton1.png')]
How2 = [pygame.image.load('Images/TutorialScreen0.png'), pygame.image.load('Images/TutorialScreen1.png')]
Back = [pygame.image.load('Images/Back0.png'), pygame.image.load('Images/Back1.png')]
Exit = [pygame.image.load('Images/LogOut0.png'), pygame.image.load('Images/LogOut1.png')]
Stat = [pygame.image.load('Images/StatsButton0.png'), pygame.image.load('Images/StatsButton1.png')]
Mplr = [pygame.image.load('Images/MPlrButton0.png'), pygame.image.load('Images/MPlrButton1.png')]
Nums = [pygame.image.load('Images/Choice2.png'), pygame.image.load('Images/Choice3.png'), pygame.image.load('Images/Choice4.png')]
Left = [pygame.image.load('Images/LeftArrow0.png'), pygame.image.load('Images/LeftArrow1.png'), pygame.image.load('Images/LeftArrow2.png')]
Rght = [pygame.image.load('Images/RightArrow0.png'), pygame.image.load('Images/RightArrow1.png'), pygame.image.load('Images/RightArrow2.png')]

# Load up icon
iconSurf = pygame.image.load('Images/GUIicon.png')
pygame.display.set_icon(iconSurf)

# Any globals
TestTime = 180
font = 'freesansbold.ttf'

# Color globals
BLACK     = (  0,   0,   0)
WHITE     = (255, 255, 255)
RED       = (255,   0,   0)
GREEN     = (  0, 255,   0)
BLUE      = (  0,   0, 128)
YELLOWISH = (238, 221, 130)
BROWNED   = (245, 222, 179)

# Init surface and create surface globals
xSize = 800
ySize = 700
DISPSURF = pygame.display.set_mode((xSize, ySize))
pygame.display.set_caption('Word Search')

# Send globals to modules
MainScreen.Help = Help
MainScreen.Back = Back
MainScreen.Dict = Dict
MainScreen.How2 = How2
MainScreen.Play = Play
MainScreen.Stat = Stat
MainScreen.Exit = Exit
MainScreen.Mplr = Mplr
MainScreen.Left = Left
MainScreen.Rght = Rght
MainScreen.Nums = Nums
Dictionary.Back = Back
Utilities.DISPSURF = DISPSURF
PlayersGui.DISPSURF = DISPSURF
Dictionary.DISPSURF = DISPSURF
MainScreen.DISPSURF = DISPSURF
Utilities.File = File
Dictionary.File = File
Game.File = File
MultiGame.File = File
PlayersGui.File = File
MainScreen.File = File
Utilities.Pending = Pending
PlayersGui.Pending = Pending
Game.Pending = Pending
MultiGame.Pending = Pending
Dictionary.Pending = Pending
MainScreen.Pending = Pending
Utilities.Pend = Pend
Dictionary.Pend = Pend
Game.Pend = Pend
MultiGame.Pend = Pend
PlayersGui.Pend = Pend
MainScreen.Pend = Pend

# Main game loop
Utilities.Update([], True)
pygame.draw.polygon(DISPSURF, GREEN, ((200, 350), (400, 175), (600, 350), (400, 525)))
TopObj = Input.DispText('Word Search', font, 48, BLUE, BROWNED, True, 'center', (xSize/2, 30))
Utilities.Update([TopObj])
TopRect = TopObj[1].copy()
TopRect.inflate_ip(30, 15)
pygame.draw.ellipse(DISPSURF, BLACK, TopRect, 2)
Objs = Input.DispText('Welcome to Word Search!', font, 32, BLUE, BROWNED, True, 'center', (xSize/2, ySize/6))
Utilities.Update([Objs])
Player = PlayersGui.AddPlayer()
file2 = Player[:-1]
Utilities.file2 = file2
Dictionary.file2 = file2
Game.file2 = file2
MultiGame.file2 = file2
MainScreen.file2 = file2
dispScore = False
File.seek(0)
Worded = File.read().split(',')
pygame.draw.polygon(DISPSURF, GREEN, ((200, 350), (400, 175), (600, 350), (400, 525)))
while True:
    while '' in Pend:
        del Pend[Pend.index('')]
    Utilities.Pend = Pend
    Game.Pend = Pend
    MultiGame.Pend = Pend
    Dictionary.Pend = Pend
    PlayersGui.Pend = Pend
    MainScreen.Pend = Pend
    startCheck = ''
    startCheck = MainScreen.mainScreen(dispScore, Player[4])
    if startCheck == 'dict':
        Utilities.Update([], True, (0, 75, xSize, ySize - 40))
        if file2[0] in ['Sam', 'test']:
            Wording = Dictionary.adminAccept(Pend)
            Pend = Wording[0]
            Worded = Wording[1]
            if not Wording[2]:
                Utilities.Update([], True, (0, 75, xSize, ySize - 40))
                Pend += Dictionary.AddWords()
            while '' in Pend:
                del Pend[Pend.index('')]
        else:
            Pend += Dictionary.AddWords()
        Utilities.Pend = Pend
        Game.Pend = Pend
        MultiGame.Pend = Pend
        Dictionary.Pend = Pend
        PlayersGui.Pend = Pend
        MainScreen.Pend = Pend
        Utilities.Update([], True, (0, 75, xSize, ySize - 40))
        dispScore = False
        pygame.draw.polygon(DISPSURF, GREEN, ((200, 350), (400, 175), (600, 350), (400, 525)))
    elif startCheck == 'start':
        Utilities.Update([], True, (0, 75, xSize, ySize - 40))
        Board = Game.CalcBoard()
        pygame.draw.rect(DISPSURF, BLACK, (217, 117, 370, 370), 5)
        Send = Game.GatherWords(Board, Worded, Player[3],
                                Rect(0, 0, 300, 120),
                                lambda: pygame.draw.rect(DISPSURF, BLACK,
                                                         (40, 570, 170, 75), 3),
                                Rect(40, 570, 170, 75),
                                lambda: pygame.draw.rect(DISPSURF, BLACK,
                                                         (565, 570, 170, 75), 3))
        BgRect = Rect(0, ySize/6 - 25, xSize, ySize/5 + 225)
        pygame.draw.rect(DISPSURF, BLACK, BgRect, 10)
        Game.GetScore(Send[0], Send[1], Player, BgRect)
        dispScore = True
    elif startCheck == 'multiplayer':
        Utilities.Update([], True, (0, 75, xSize, ySize - 40))
        GoToGame = MainScreen.GetPlayers()
        Utilities.Update([], True, (0, 75, xSize, ySize - 40))
        if not isinstance(GoToGame, bool):
            Board = Game.CalcBoard()
            pygame.draw.rect(DISPSURF, BLACK, (217, 117, 370, 370), 5)
            Send = MultiGame.GatherWords(Board, Worded, Player[3],
                                         [Rect(40, 570, 170, 75),
                                          Rect(567, 572, 166, 71),
                                          Rect(42, 132, 166, 71),
                                          Rect(607, 132, 166, 71),
                                          Rect(0, 0, 300, 120)],
                                         [lambda: pygame.draw.rect(DISPSURF, BLACK,(40, 570, 170, 75), 3),
                                          lambda: pygame.draw.rect(DISPSURF, BLACK,(565, 570, 170, 75), 3),
                                          lambda: pygame.draw.rect(DISPSURF, BLACK, (40, 130, 170, 75), 3),
                                          lambda: pygame.draw.rect(DISPSURF, BLACK, (605, 130, 170, 75), 3)],
                                         GoToGame)
            BgRect = Rect(0, ySize/6 - 25, xSize, ySize/5 + 225)
            pygame.draw.rect(DISPSURF, BLACK, BgRect, 10)
            MultiGame.GetScore(Send[0], Send[1], GoToGame, BgRect)
            dispScore = True
        else:
            dispScore = False
            pygame.draw.polygon(DISPSURF, GREEN, ((200, 350), (400, 175), (600, 350), (400, 525)))
            Utilities.Update()
    elif startCheck == 'help':
        Utilities.Update([], True, (0, 75, xSize, ySize - 40))
        Click = False
        while not Click:
            Click = MainScreen.Tutorial()
        dispScore = False
        pygame.draw.polygon(DISPSURF, GREEN, ((200, 350), (400, 175), (600, 350), (400, 525)))
    elif startCheck == 'exit':
        Utilities.Update([], True, (0, 75, xSize, ySize - 40))
        a = file2[1]
        b = file2[0]
        loadWordX = a[b].bestWord
        loadHighX = str(a[b].high)
        loadScoreX = str(a[b].bestScore)
        loadX = ','.join([loadWordX, loadHighX, loadScoreX])
        file2[2].write(loadX)
        file2[2].close()
        Utilities.file2 = ''
        Game.file2 = ''
        MultiGame.file2 = ''
        Dictionary.file2 = ''
        MainScreen.file2 = ''
        Objs = Input.DispText('Welcome to Word Search!', font, 32, BLUE, BROWNED, True, 'center', (xSize/2, ySize/6))
        Utilities.Update([Objs])
        Player = PlayersGui.AddPlayer(Player[1])
        TopObj = Input.DispText('Word Search', font, 48, BLUE, BROWNED, True, 'center', (xSize/2, 30))
        Utilities.Update([TopObj])
        TopRect = TopObj[1].copy()
        TopRect.inflate_ip(30, 15)
        pygame.draw.ellipse(DISPSURF, BLACK, TopRect, 2)
        file2 = Player[:-1]
        Utilities.file2 = file2
        Dictionary.file2 = file2
        Game.file2 = file2
        MultiGame.file2 = file2
        MainScreen.file2 = file2
        Utilities.Update([], True, (0, 75, xSize, ySize - 40))
        dispScore = False
        pygame.draw.polygon(DISPSURF, GREEN, ((200, 350), (400, 175), (600, 350), (400, 525)))
    elif startCheck == 'stats':
        Utilities.Update([], True, (0, 75, xSize, ySize - 40))
        MainScreen.Statistics(Player[1])
        Utilities.Update([], True, (0, 75, xSize, ySize - 40))
        dispScore = False
        pygame.draw.polygon(DISPSURF, GREEN, ((200, 350), (400, 175), (600, 350), (400, 525)))
