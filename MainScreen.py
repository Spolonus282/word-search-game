# import and initialize
import pygame, Utilities, Input
from pygame.locals import *
pygame.init()
DISPSURF = ''
Play = ''
Dict = ''
How2 = ''
Exit = ''
Stat = ''
Back = ''
Help = ''
Mplr = ''
Nums = ''
Left = ''
Rght = ''
xSize = 800
ySize = 700
File = ''
Pending = ''
Pend = ''
file2 = ''
BLACK     = (  0,   0,   0)
WHITE     = (255, 255, 255)
RED       = (255,   0,   0)
GREEN     = (  0, 255,   0)
BLUE      = (  0,   0, 128)
YELLOWISH = (238, 221, 130)
BROWNED   = (245, 222, 179)
GRAY      = (220, 220, 220)
font = 'freesansbold.ttf'

def mainScreen(ShowScore, UserRect):
    'Display the main screen'
    checkClick = []
    getMouse = pygame.mouse.get_pos()
    getClick = pygame.mouse.get_pressed()[0]
    # Play button
    PlayImage0 = Play[0].get_rect()
    PlayImage1 = Play[1].get_rect()
    PlayHold0 = [Play[0], PlayImage0]
    PlayHold1 = [Play[1], PlayImage1]
    if ShowScore:
        PlayImage0.center = (xSize/2 + 150, ySize/2 + 75)
        PlayImage1.center = (xSize/2 + 150, ySize/2 + 75)
    else:
        PlayImage0.center = (xSize/2 + 150, ySize/2)
        PlayImage1.center = (xSize/2 + 150, ySize/2)
    resetPlay = PlayImage0.copy()
    # Add the dictionary button
    DictImage0 = Dict[0].get_rect()
    DictImage1 = Dict[1].get_rect()
    DictHold0 = [Dict[0], DictImage0]
    DictHold1 = [Dict[1], DictImage1]
    DictImage0.center = (100, 50)
    DictImage1.center = (100, 50)
    resetDict = DictImage0.copy()
    # Add the help button
    HelpImage0 = Help[0].get_rect()
    HelpImage1 = Help[1].get_rect()
    HelpHold0 = [Help[0], HelpImage0]
    HelpHold1 = [Help[1], HelpImage1]
    HelpImage0.center = (75, 650)
    HelpImage1.center = (75, 650)
    resetHelp = HelpImage0.copy()
    # Add the log out button
    ExitImage0 = Exit[0].get_rect()
    ExitImage1 = Exit[1].get_rect()
    ExitHold0 = [Exit[0], ExitImage0]
    ExitHold1 = [Exit[1], ExitImage1]
    ExitImage0.center = (700, 75)
    ExitImage1.center = (700, 75)
    resetExit = ExitImage0.copy()
    # Add the stats button
    StatImage0 = Stat[0].get_rect()
    StatImage1 = Stat[1].get_rect()
    StatHold0 = [Stat[0], StatImage0]
    StatHold1 = [Stat[1], StatImage1]
    StatImage0.center = (700, 650)
    StatImage1.center = (700, 650)
    resetStat = StatImage0.copy()
    # Add the multiplayer button
    MplrImage0 = Mplr[0].get_rect()
    MplrImage1 = Mplr[1].get_rect()
    MplrHold0 = [Mplr[0], MplrImage0]
    MplrHold1 = [Mplr[1], MplrImage1]
    if ShowScore:
        MplrImage0.center = (xSize/2 - 150, ySize/2 + 75)
        MplrImage1.center = (xSize/2 - 150, ySize/2 + 75)
    else:
        MplrImage0.center = (xSize/2 - 150, ySize/2)
        MplrImage1.center = (xSize/2 - 150, ySize/2)
    resetMplr = MplrImage0.copy()
    if PlayImage0.left < getMouse[0] < PlayImage0.right and PlayImage0.top < getMouse[1] < PlayImage0.bottom:
        Utilities.Update([PlayHold1, DictHold0, HelpHold0, ExitHold0, StatHold0, MplrHold0], True, [resetPlay, resetDict, resetHelp, resetExit, resetStat, resetMplr])
        checkClick = [True]
    elif DictImage0.left < getMouse[0] < DictImage0.right and DictImage0.top < getMouse[1] < DictImage0.bottom:
        Utilities.Update([PlayHold0, DictHold1, HelpHold0, ExitHold0, StatHold0, MplrHold0], True, [resetPlay, resetDict, resetHelp, resetExit, resetStat, resetMplr])
        checkClick = [False, True]
    elif HelpImage0.left < getMouse[0] < HelpImage0.right and HelpImage0.top < getMouse[1] < HelpImage0.bottom:
        Utilities.Update([PlayHold0, DictHold0, HelpHold1, ExitHold0, StatHold0, MplrHold0], True, [resetPlay, resetDict, resetHelp, resetExit, resetStat, resetMplr])
        checkClick = [False, False, True]
    elif ExitImage0.left < getMouse[0] < ExitImage0.right and ExitImage0.top < getMouse[1] < ExitImage0.bottom:
        Utilities.Update([PlayHold0, DictHold0, HelpHold0, ExitHold1, StatHold0, MplrHold0], True, [resetPlay, resetDict, resetHelp, resetExit, resetStat, resetMplr])
        checkClick = [False, False, False, True]
    elif StatImage0.left < getMouse[0] < StatImage0.right and StatImage0.top < getMouse[1] < StatImage0.bottom:
        Utilities.Update([PlayHold0, DictHold0, HelpHold0, ExitHold0, StatHold1, MplrHold0], True, [resetPlay, resetDict, resetHelp, resetExit, resetStat, resetMplr])
        checkClick = [False, False, False, False, True]
    elif MplrImage0.left < getMouse[0] < MplrImage0.right and MplrImage0.top < getMouse[1] < MplrImage0.bottom:
        Utilities.Update([PlayHold0, DictHold0, HelpHold0, ExitHold0, StatHold0, MplrHold1], True, [resetPlay, resetDict, resetHelp, resetExit, resetStat, resetMplr])
        checkClick = [False, False, False, False, False, True]
    else:
        Utilities.Update([PlayHold0, DictHold0, HelpHold0, ExitHold0, StatHold0, MplrHold0], True, [resetPlay, resetDict, resetHelp, resetExit, resetStat, resetMplr])
        checkClick = []
    if getClick == 1 and any(checkClick):
        Utilities.Update([], True, [resetPlay, resetDict, resetHelp, resetExit, resetStat, resetMplr])
        if checkClick[0]:
            return 'start'
        elif checkClick[1]:
            return 'dict'
        elif checkClick[2]:
            return 'help'
        elif checkClick[3]:
            Utilities.Update([], True, UserRect)
            return 'exit'
        elif checkClick[4]:
            return 'stats'
        elif checkClick[5]:
            return 'multiplayer'

def Tutorial():
    'Run the tutorial'
    Mouse = pygame.mouse.get_pos()
    ClickCheck = pygame.mouse.get_pressed()[0]
    How2Image0 = How2[0].get_rect()
    How2Image1 = How2[1].get_rect()
    How2Hold0 = [How2[0], How2Image0]
    How2Hold1 = [How2[1], How2Image1]
    How2Image0.bottomleft = (0, 600)
    How2Image1.bottomleft = (0, 600)
    resetHow2 = How2Image0.copy()
    if 596 < Mouse[0] < 773 and 422 < Mouse[1] < 555:
        Utilities.Update([How2Hold1], True, resetHow2)
        if ClickCheck == 1:
            Utilities.Update([], True, resetHow2)
            return True
    else:
        Utilities.Update([How2Hold0], True, resetHow2)
    return False

def Statistics(Players):
    'Display player stats'
    c = 100
    a = len(Players)
    if a > 12:
        a = 12
    d = list(Players)
    y = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
    for x in range(a):
        if y[0] == -1 or Players[d[x]].high > Players[y[0]].high:
            y.insert(0, d[x])
        elif y[1] == -1 or Players[d[x]].high > Players[y[1]].high:
            y.insert(1, d[x])
        elif y[2] == -1 or Players[d[x]].high > Players[y[2]].high:
            y.insert(2, d[x])
        elif y[3] == -1 or Players[d[x]].high > Players[y[3]].high:
            y.insert(3, d[x])
        elif y[4] == -1 or Players[d[x]].high > Players[y[4]].high:
            y.insert(4, d[x])
        elif y[5] == -1 or Players[d[x]].high > Players[y[5]].high:
            y.insert(5, d[x])
        elif y[6] == -1 or Players[d[x]].high > Players[y[6]].high:
            y.insert(6, d[x])
        elif y[7] == -1 or Players[d[x]].high > Players[y[7]].high:
            y.insert(7, d[x])
        elif y[8] == -1 or Players[d[x]].high > Players[y[8]].high:
            y.insert(8, d[x])
        elif y[9] == -1 or Players[d[x]].high > Players[y[9]].high:
            y[9] = d[x]
    while -1 in y:
        y.remove(-1)
    d = y
    PlayersObjs = []
    if a <= 4:
        for b in range(a):
            if Players[d[b]].bestWord == '':
                Players[d[b]].bestWord = 'None'
            PlayersObjs.append([])
            PlayersObjs[b].append(Input.DispText(str(b + 1) + ': ' + ''.join([d[b], ':']), font, 20, BLUE, BROWNED, True, 'center', (xSize/2 - 25, c)))
            c += 25
            PlayersObjs[b].append(Input.DispText('High Score: ' + str(Players[d[b]].high), font, 16, BLUE, BROWNED, True, 'center', (xSize/2, c)))
            c += 25
            PlayersObjs[b].append(Input.DispText('Best Word: ' + Players[d[b]].bestWord, font, 16, BLUE, BROWNED, True, 'center', (xSize/2, c)))
            c += 25
            PlayersObjs[b].append(Input.DispText('Word Score: ' + str(Players[d[b]].bestScore), font, 16, BLUE, BROWNED, True, 'center', (xSize/2, c)))
            c += 50
    elif a > 4:
        if a <= 8:
            for b in range(4):
                if Players[d[b]].bestWord == '':
                    Players[d[b]].bestWord = 'None'
                PlayersObjs.append([])
                PlayersObjs[b].append(Input.DispText(str(b + 1) + ': ' + ''.join([d[b], ':']), font, 20, BLUE, BROWNED, True, 'center', (200 - 25, c)))
                c += 25
                PlayersObjs[b].append(Input.DispText('High Score: ' + str(Players[d[b]].high), font, 16, BLUE, BROWNED, True, 'center', (200, c)))
                c += 25
                PlayersObjs[b].append(Input.DispText('Best Word: ' + Players[d[b]].bestWord, font, 16, BLUE, BROWNED, True, 'center', (200, c)))
                c += 25
                PlayersObjs[b].append(Input.DispText('Word Score: ' + str(Players[d[b]].bestScore), font, 16, BLUE, BROWNED, True, 'center', (200, c)))
                c += 50
            c = 100
            for f in range(4, a):
                PlayersObjs.append([])
                PlayersObjs[f].append(Input.DispText(str(f + 1) + ': ' + ''.join([d[f], ':']), font, 20, BLUE, BROWNED, True, 'center', (600 - 25, c)))
                c += 25
                PlayersObjs[f].append(Input.DispText('High Score: ' + str(Players[d[f]].high), font, 16, BLUE, BROWNED, True, 'center', (600, c)))
                c += 25
                PlayersObjs[f].append(Input.DispText('Best Word: ' + Players[d[f]].bestWord, font, 16, BLUE, BROWNED, True, 'center', (600, c)))
                c += 25
                PlayersObjs[f].append(Input.DispText('Word Score: ' + str(Players[d[f]].bestScore), font, 16, BLUE, BROWNED, True, 'center', (600, c)))
                c += 50
        elif a > 8:
            for b in range(4):
                if Players[d[b]].bestWord == '':
                    Players[d[b]].bestWord = 'None'
                PlayersObjs.append([])
                PlayersObjs[b].append(Input.DispText(str(b + 1) + ': ' + ''.join([d[b], ':']), font, 20, BLUE, BROWNED, True, 'center', (200 - 25, c)))
                c += 25
                PlayersObjs[b].append(Input.DispText('High Score: ' + str(Players[d[b]].high), font, 16, BLUE, BROWNED, True, 'center', (200, c)))
                c += 25
                PlayersObjs[b].append(Input.DispText('Best Word: ' + Players[d[b]].bestWord, font, 16, BLUE, BROWNED, True, 'center', (200, c)))
                c += 25
                PlayersObjs[b].append(Input.DispText('Word Score: ' + str(Players[d[b]].bestScore), font, 16, BLUE, BROWNED, True, 'center', (200, c)))
                c += 50
            c = 100
            for f in range(4, 8):
                PlayersObjs.append([])
                PlayersObjs[f].append(Input.DispText(str(f + 1) + ': ' + ''.join([d[f], ':']), font, 20, BLUE, BROWNED, True, 'center', (xSize/2, c)))
                c += 25
                PlayersObjs[f].append(Input.DispText('High Score: ' + str(Players[d[f]].high), font, 16, BLUE, BROWNED, True, 'center', (xSize/2, c)))
                c += 25
                PlayersObjs[f].append(Input.DispText('Best Word: ' + Players[d[f]].bestWord, font, 16, BLUE, BROWNED, True, 'center', (xSize/2, c)))
                c += 25
                PlayersObjs[f].append(Input.DispText('Word Score: ' + str(Players[d[f]].bestScore), font, 16, BLUE, BROWNED, True, 'center', (xSize/2, c)))
                c += 50
            c = 100
            if a <= 12:
                for g in range(8, a):
                    PlayersObjs.append([])
                    PlayersObjs[g].append(Input.DispText(str(g + 1) + ': ' + ''.join([d[g], ':']), font, 20, BLUE, BROWNED, True, 'center', (600 - 25, c)))
                    c += 25
                    PlayersObjs[g].append(Input.DispText('High Score: ' + str(Players[d[g]].high), font, 16, BLUE, BROWNED, True, 'center', (600, c)))
                    c += 25
                    PlayersObjs[g].append(Input.DispText('Best Word: ' + Players[d[g]].bestWord, font, 16, BLUE, BROWNED, True, 'center', (600, c)))
                    c += 25
                    PlayersObjs[g].append(Input.DispText('Word Score: ' + str(Players[d[g]].bestScore), font, 16, BLUE, BROWNED, True, 'center', (600, c)))
                    c += 50
            elif a > 12:
                for g in range(8, 12):
                    PlayersObjs.append([])
                    PlayersObjs[g].append(Input.DispText(str(g + 1) + ': ' + ''.join([d[g], ':']), font, 20, BLUE, BROWNED, True, 'center', (600 - 25, c)))
                    c += 25
                    PlayersObjs[g].append(Input.DispText('High Score: ' + str(Players[d[g]].high), font, 16, BLUE, BROWNED, True, 'center', (600, c)))
                    c += 25
                    PlayersObjs[g].append(Input.DispText('Best Word: ' + Players[d[g]].bestWord, font, 16, BLUE, BROWNED, True, 'center', (600, c)))
                    c += 25
                    PlayersObjs[g].append(Input.DispText('Word Score: ' + str(Players[d[g]].bestScore), font, 16, BLUE, BROWNED, True, 'center', (600, c)))
                    c += 50
    for e in range(a):
        Utilities.Update(PlayersObjs[e])
    while True:
        Mouse = pygame.mouse.get_pos()
        Click = pygame.mouse.get_pressed()[0]
        # Back Button
        BackImage0 = Back[0].get_rect()
        BackImage1 = Back[1].get_rect()
        BackHold0 = [Back[0], BackImage0]
        BackHold1 = [Back[1], BackImage1]
        BackImage0.center = (xSize/2, 625)
        BackImage1.center = (xSize/2, 625)
        resetBack = BackImage0.copy()
        if BackImage0.left < Mouse[0] < BackImage0.right and BackImage0.top < Mouse[1] < BackImage0.bottom:
            Utilities.Update([BackHold1], True, resetBack)
            checkClick = True
        else:
            Utilities.Update([BackHold0], True, resetBack)
            checkClick = False
        if checkClick and Click == 1:
            return

def GetPlayers():
    ChangeLeft = False
    ChangeRght = True
    checkClick = []
    Gray1 = True
    Gray3 = True
    Old0 = False
    Old1 = False
    Old2 = False
    Old3 = False
    Selected0 = False
    Selected1 = False
    Selected2 = False
    Selected3 = False
    NumOn = 0
    #Input Boxes
    wipeError = Rect(300, ySize/2 - 80, 200, 20)
    input3 = Rect(550, ySize/2 + 175, 200, 50)
    text0 = Rect(50, ySize/2 - 175, 200, 50).copy()
    text0.inflate_ip(-6,-6)
    text1 = Rect(50, ySize/2 + 175, 200, 50).copy()
    text1.inflate_ip(-6,-6)
    text2 = Rect(550, ySize/2 - 175, 200, 50).copy()
    text2.inflate_ip(-6,-6)
    text3 = Rect(550, ySize/2 + 175, 200, 50).copy()
    text3.inflate_ip(-6,-6)
    #Left Arrow
    LeftImage0 = Left[0].get_rect()
    LeftImage1 = Left[1].get_rect()
    LeftImage2 = Left[2].get_rect()
    LeftHold0 = [Left[0], LeftImage0]
    LeftHold1 = [Left[1], LeftImage1]
    LeftHold2 = [Left[2], LeftImage2]
    LeftImage0.center = (xSize/2 - 100, ySize/2)
    LeftImage1.center = (xSize/2 - 100, ySize/2)
    LeftImage2.center = (xSize/2 - 100, ySize/2)
    resetLeft = LeftImage0.copy()
    #Rght Arrow
    RghtImage0 = Rght[0].get_rect()
    RghtImage1 = Rght[1].get_rect()
    RghtImage2 = Rght[2].get_rect()
    RghtHold0 = [Rght[0], RghtImage0]
    RghtHold1 = [Rght[1], RghtImage1]
    RghtHold2 = [Rght[2], RghtImage2]
    RghtImage0.center = (xSize/2 + 100, ySize/2)
    RghtImage1.center = (xSize/2 + 100, ySize/2)
    RghtImage2.center = (xSize/2 + 100, ySize/2)
    resetRght = RghtImage0.copy()
    #Big Nums
    NumsImage0 = Nums[0].get_rect()
    NumsImage1 = Nums[1].get_rect()
    NumsImage2 = Nums[2].get_rect()
    NumsHold0 = [Nums[0], NumsImage0]
    NumsHold1 = [Nums[1], NumsImage1]
    NumsHold2 = [Nums[2], NumsImage2]
    NumsImage0.center = (xSize/2, ySize/2)
    NumsImage1.center = (xSize/2, ySize/2)
    NumsImage2.center = (xSize/2, ySize/2)
    resetNums = NumsImage0.copy()
    # Play button
    PlayImage0 = Play[0].get_rect()
    PlayImage1 = Play[1].get_rect()
    PlayHold0 = [Play[0], PlayImage0]
    PlayHold1 = [Play[1], PlayImage1]
    PlayImage0.center = (xSize/2, ySize/2 - 150)
    PlayImage1.center = (xSize/2, ySize/2 - 150)
    resetPlay = PlayImage0.copy()
    # Back Button
    BackImage0 = Back[0].get_rect()
    BackImage1 = Back[1].get_rect()
    BackHold0 = [Back[0], BackImage0]
    BackHold1 = [Back[1], BackImage1]
    BackImage0.center = (xSize/2, 625)
    BackImage1.center = (xSize/2, 625)
    resetBack = BackImage0.copy()
    pygame.draw.rect(DISPSURF, BLACK, (50, ySize/2 - 175, 200, 50), 3)
    pygame.draw.rect(DISPSURF, BLACK, (50, ySize/2 + 175, 200, 50), 3)
    pygame.draw.rect(DISPSURF, BLACK, (550, ySize/2 - 175, 200, 50), 3)
    pygame.draw.rect(DISPSURF, BLACK, (550, ySize/2 + 175, 200, 50), 3)
    InfoObj = [Input.DispText('# of Players', font, 20, BLUE, BROWNED, True, 'center', (xSize/2, ySize/2 + 85)),
               Input.DispText('This game does not count toward any individual statistics.', font, 20, BLUE, BROWNED, True, 'center', (xSize/2, ySize/2 + 115))]
    Utilities.Update(InfoObj)
    Name0 = file2[0]
    Name1 = ''
    Name2 = ''
    Name3 = ''
    WordObj0 = Input.DispText(Name0, font, 20, BLUE, BROWNED, True, 'center', text0.center)
    Utilities.Update([WordObj0], True, text0)
    while True:
        while True:
            checkClick = []
            Mouse = pygame.mouse.get_pos()
            Click = pygame.mouse.get_pressed()[0]
            if Selected0:
                pygame.draw.rect(DISPSURF, BLACK, (50, ySize/2 - 175, 200, 50), 5)
                Utilities.Update()
                Word0 = [False, Name0]
                while Word0[0] != 'return' and Click != 1:
                    Click = pygame.mouse.get_pressed()[0]
                    Word0 = Input.Typed(Word0[1], Word0[0], 8, [File, [Pending, Pend], file2])
                    Name0 = ''.join(Word0[1])
                    WordObj0 = Input.DispText(Name0, font, 20, BLUE, BROWNED, True, 'center', text0.center)
                    Utilities.Update([WordObj0], True, text0)
                Selected0 = False
                Old0 = True
            elif not Selected0:
                if Old0:
                    pygame.draw.rect(DISPSURF, BROWNED, (50, ySize/2 - 175, 200, 50), 5)
                    pygame.draw.rect(DISPSURF, BLACK, (50, ySize/2 - 175, 200, 50), 3)
                    Utilities.Update()
                Old0 = False
            if Gray1:
                pygame.draw.rect(DISPSURF, BLACK, (50, ySize/2 + 175, 200, 50), 5)
                pygame.draw.rect(DISPSURF, GRAY, (50, ySize/2 + 175, 200, 50), 3)
                Utilities.Update()
                Old1 = True
            elif Selected1:
                pygame.draw.rect(DISPSURF, BLACK, (50, ySize/2 + 175, 200, 50), 5)
                Utilities.Update()
                Word1 = [False, Name1]
                while Word1[0] != 'return' and Click != 1:
                    Click = pygame.mouse.get_pressed()[0]
                    Word1 = Input.Typed(Word1[1], Word1[0], 8, [File, [Pending, Pend], file2])
                    Name1 = ''.join(Word1[1])
                    WordObj1 = Input.DispText(Name1, font, 20, BLUE, BROWNED, True, 'center', text1.center)
                    Utilities.Update([WordObj1], True, text1)
                Selected1 = False
                Old1 = True
            elif not Selected1:
                if Old1:
                    pygame.draw.rect(DISPSURF, BROWNED, (50, ySize/2 + 175, 200, 50), 5)
                    pygame.draw.rect(DISPSURF, BLACK, (50, ySize/2 + 175, 200, 50), 3)
                    Utilities.Update()
                Old1 = False
            if Selected2:
                pygame.draw.rect(DISPSURF, BLACK, (550, ySize/2 - 175, 200, 50), 5)
                Utilities.Update()
                Word2 = [False, Name2]
                while Word2[0] != 'return' and Click != 1:
                    Click = pygame.mouse.get_pressed()[0]
                    Word2 = Input.Typed(Word2[1], Word2[0], 8, [File, [Pending, Pend], file2])
                    Name2 = ''.join(Word2[1])
                    WordObj2 = Input.DispText(Name2, font, 20, BLUE, BROWNED, True, 'center', text2.center)
                    Utilities.Update([WordObj2], True, text2)
                Selected2 = False
                Old2 = True
            elif not Selected2:
                if Old2:
                    pygame.draw.rect(DISPSURF, BROWNED, (550, ySize/2 - 175, 200, 50), 5)
                    pygame.draw.rect(DISPSURF, BLACK, (550, ySize/2 - 175, 200, 50), 3)
                    Utilities.Update()
                Old2 = False
            if Gray3:
                pygame.draw.rect(DISPSURF, BLACK, (550, ySize/2 + 175, 200, 50), 5)
                pygame.draw.rect(DISPSURF, GRAY, (550, ySize/2 + 175, 200, 50), 3)
                Utilities.Update()
                Old3 = True
            elif Selected3:
                pygame.draw.rect(DISPSURF, BLACK, (550, ySize/2 + 175, 200, 50), 5)
                Utilities.Update()
                Word3 = [False, Name3]
                while Word3[0] != 'return' and Click != 1:
                    Click = pygame.mouse.get_pressed()[0]
                    Word3 = Input.Typed(Word3[1], Word3[0], 8, [File, [Pending, Pend], file2])
                    Name3 = ''.join(Word3[1])
                    WordObj3 = Input.DispText(Name3, font, 20, BLUE, BROWNED, True, 'center', text3.center)
                    Utilities.Update([WordObj3], True, text3)
                Selected3 = False
                Old3 = True
            elif not Selected3:
                if Old3:
                    pygame.draw.rect(DISPSURF, BROWNED, (550, ySize/2 + 175, 200, 50), 5)
                    pygame.draw.rect(DISPSURF, BLACK, (550, ySize/2 + 175, 200, 50), 3)
                    Utilities.Update()
                Old3 = False
            if PlayImage0.left < Mouse[0] < PlayImage0.right and PlayImage0.top < Mouse[1] < PlayImage0.bottom:
                Utilities.Update([PlayHold1], True, resetPlay)
                checkClick = [False, False, True]
            else:
                Utilities.Update([PlayHold0], True, resetPlay)
            if BackImage0.left < Mouse[0] < BackImage0.right and BackImage0.top < Mouse[1] < BackImage0.bottom:
                Utilities.Update([BackHold1], True, resetBack)
                checkClick = [False, False, False, True]
            else:
                Utilities.Update([BackHold0], True, resetBack)
            if not ChangeLeft:
                Utilities.Update([LeftHold2], True, resetLeft)
            elif LeftImage0.left < Mouse[0] < LeftImage0.right and LeftImage0.top < Mouse[1] < LeftImage0.bottom and ChangeLeft:
                Utilities.Update([LeftHold1], True, [resetLeft])
                checkClick = [True]
            elif ChangeLeft and not (LeftImage0.left < Mouse[0] < LeftImage0.right and LeftImage0.top < Mouse[1] < LeftImage0.bottom):
                Utilities.Update([LeftHold0], True, resetLeft)

            if not ChangeRght:
                Utilities.Update([RghtHold2], True, resetRght)
            elif RghtImage0.left < Mouse[0] < RghtImage0.right and RghtImage0.top < Mouse[1] < RghtImage0.bottom and ChangeRght:
                Utilities.Update([RghtHold1], True, [resetRght])
                checkClick = [False, True]
            elif ChangeRght and not (RghtImage0.left < Mouse[0] < RghtImage0.right and RghtImage0.top < Mouse[1] < RghtImage0.bottom):
                Utilities.Update([RghtHold0], True, resetRght)
            if any(checkClick) and Click == 1:
                if checkClick[0]:
                    NumOn -= 1
                    if NumOn == 0:
                        ChangeLeft = False
                    else:
                        ChangeLeft = True
                elif checkClick[1]:
                    NumOn += 1
                    if NumOn == 2:
                        ChangeRght = False
                    else:
                        ChangeRght = True
                elif checkClick[2]:
                    break
                elif checkClick[3]:
                    return False
                if NumOn == 0:
                    Utilities.Update([NumsHold0], True, resetNums)
                    Utilities.Sleep(0.05)
                    Gray1 = True
                    Gray3 = True
                elif NumOn == 1:
                    Utilities.Update([NumsHold1], True, resetNums)
                    Utilities.Sleep(0.05)
                    Gray1 = False
                    Gray3 = True
                elif NumOn == 2:
                    Utilities.Update([NumsHold2], True, resetNums)
                    Utilities.Sleep(0.05)
                    Gray1 = False
                    Gray3 = False
            elif Click == 1:
                if Rect(50, ySize/2 - 175, 200, 50).left < Mouse[0] < Rect(50, ySize/2 - 175, 200, 50).right and Rect(50, ySize/2 - 175, 200, 50).top < Mouse[1] < Rect(50, ySize/2 - 175, 200, 50).bottom:
                    Selected0 = True
                    Selected1 = False
                    Selected2 = False
                    Selected3 = False
                elif Rect(50, ySize/2 + 175, 200, 50).left < Mouse[0] < Rect(50, ySize/2 + 175, 200, 50).right and Rect(50, ySize/2 + 175, 200, 50).top < Mouse[1] < Rect(50, ySize/2 + 175, 200, 50).bottom and not Gray1:
                    Selected0 = False
                    Selected1 = True
                    Selected2 = False
                    Selected3 = False
                elif Rect(550, ySize/2 - 175, 200, 50).left < Mouse[0] < Rect(550, ySize/2 - 175, 200, 50).right and Rect(550, ySize/2 - 175, 200, 50).top < Mouse[1] < Rect(550, ySize/2 - 175, 200, 50).bottom:
                    Selected0 = False
                    Selected1 = False
                    Selected2 = True
                    Selected3 = False
                elif Rect(550, ySize/2 + 175, 200, 50).left < Mouse[0] < Rect(550, ySize/2 + 175, 200, 50).right and Rect(550, ySize/2 + 175, 200, 50).top < Mouse[1] < Rect(550, ySize/2 + 175, 200, 50).bottom and not Gray3:
                    Selected0 = False
                    Selected1 = False
                    Selected2 = False
                    Selected3 = True
                else:
                    Selected0 = False
                    Selected1 = False
                    Selected2 = False
                    Selected3 = False
            if NumOn != 0:
                ChangeLeft = True
            if NumOn != 2:
                ChangeRght = True
            if NumOn == 0:
                Utilities.Update([NumsHold0], True, resetNums)
            elif NumOn == 1:
                Utilities.Update([NumsHold1], True, resetNums)
            elif NumOn == 2:
                Utilities.Update([NumsHold2], True, resetNums)
        error = ''
        if not ChangeLeft:
            if Name0 == '' or Name2 == '':
                if Name0 == '' and not Name2 == '':
                    error = 'Player one cannot be empty!'
                elif not Name0 == '' and Name2 == '':
                    error = 'Player two cannot be empty!'
                elif Name0 == '' and Name2 == '':
                    error = 'People actually need to play!'
            else:
                return [Name0, Name2]
        elif not ChangeRght:
            if Name0 == '' or Name1 == '' or Name2 == '' or Name3 == '':
                error = []
                if Name0 == '':
                    error.append('one')
                if Name2 == '':
                    error.append('two')
                if Name1 == '':
                    error.append('three')
                if Name3 == '':
                    error.append('four')
                if len(error) == 1:
                    error = 'Player %s cannot be empty!' %error[0]
                elif len(error) == 2:
                    error = 'Players %s and %s cannot be empty!' %(error[0],error[1])
                elif len(error) == 3:
                    error = 'Players %s, %s, and %s cannot be empty!' %(error[0],error[1],error[2])
                elif len(error) == 4:
                    error = 'People actually need to play!'
            else:
                return [Name0, Name2, Name1, Name3]
        else:
            if Name0 == '' or Name1 == '' or Name2 == '':
                error = []
                if Name0 == '':
                    error.append('one')
                if Name2 == '':
                    error.append('two')
                if Name1 == '':
                    error.append('three')
                if len(error) == 1:
                    error = 'Player %s cannot be empty!' %error[0]
                elif len(error) == 2:
                    error = 'Players %s and %s cannot be empty!' %(error[0],error[1])
                elif len(error) == 3:
                    error = 'People actually need to play!'
            else:
                return [Name0, Name2, Name1]
        errorObj = Input.DispText(error, font, 20, RED, BROWNED, True, 'center', (xSize/2, ySize/2 - 70))
        Utilities.Update([errorObj], True, wipeError)
