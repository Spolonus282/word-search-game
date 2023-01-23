# import and initialize
import pygame, NewInput, Utilities
from pygame.locals import *
pygame.init()
DISPSURF = ''
File = ''
file2 = ''
Pending = ''
Pend = ''
Back = ''
xSize = 800
ySize = 700
font = 'freesansbold.ttf'
BLACK     = (  0,   0,   0)
WHITE     = (255, 255, 255)
RED       = (255,   0,   0)
GREEN     = (  0, 255,   0)
BLUE      = (  0,   0, 128)
YELLOWISH = (238, 221, 130)
BROWNED   = (245, 222, 179)

def AddWords():
    'Add words to be looked over'
    gs = False
    go = True
    Confirm = True
    AskObj = NewInput.DispText('Add words to Dictionary', 32, BLUE, YELLOWISH, 'center', (xSize/2, ySize/5 + 150))
    Utilities.Update([AskObj])
    clearRect = Rect(4, ySize/6 + 50, xSize - 8, ySize/5 + 220)
    pygame.draw.rect(DISPSURF, BLACK, (0, ySize/6 + 48, xSize, ySize/5 + 225), 10)
    # Back Button
    BackImage0 = Back[0].get_rect()
    BackImage1 = Back[1].get_rect()
    BackHold0 = [Back[0], BackImage0]
    BackHold1 = [Back[1], BackImage1]
    BackImage0.center = (xSize/2, 625)
    BackImage1.center = (xSize/2, 625)
    resetBack = BackImage0.copy()
    while True:
        Mouse = pygame.mouse.get_pos()
        Click = pygame.mouse.get_pressed()[0]
        if BackImage0.left < Mouse[0] < BackImage0.right and BackImage0.top < Mouse[1] < BackImage0.bottom:
            gs = True
            checkClick = True
        else:
            gs = False
            checkClick = False
        if gs and not go:
            Utilities.Update([BackHold1], True, resetBack)
            go = True
        elif not gs and go:
            Utilities.Update([BackHold0], True, resetBack)
            go = False
        if checkClick and Click == 1:
            break
        Utilities.Update([AskObj], True, clearRect, YELLOWISH)
        newWord = ''
        get = newWord
        go = False
        while isinstance(get, str):
            Mouse = pygame.mouse.get_pos()
            Click = pygame.mouse.get_pressed()[0]
            if BackImage0.left < Mouse[0] < BackImage0.right and BackImage0.top < Mouse[1] < BackImage0.bottom:
                gs = True
                checkClick = True
            else:
                gs = False
                checkClick = False
            if checkClick and Click == 1:
                Pending.seek(0)
                return Pending.read().split(',')
            if gs and not go:
                Utilities.Update([BackHold1], True, resetBack)
                go = True
            elif not gs and go:
                Utilities.Update([BackHold0], True, resetBack)
                go = False
            wordObj = NewInput.DispText(newWord, 20, BLUE, YELLOWISH, 'center', (xSize/2, ySize/5 + 200))
            get = NewInput.Typed(get, 16)
            Utilities.Update([wordObj, AskObj], True, clearRect, YELLOWISH)
            if isinstance(get, int):
                continue
            newWord = 'Input word: ' + get
            added = get
        if len(str(added)) < 3:
            shortObj = NewInput.DispText('Word too short!', 20, BLUE, YELLOWISH, 'center', (xSize/2, ySize/5 + 200))
            Utilities.Update([shortObj, AskObj], True, clearRect, YELLOWISH)
        else:
            Pend.append(added)
            addObj = NewInput.DispText('Added!', 20, BLUE, YELLOWISH, 'center', (xSize/2, ySize/5 + 200))
            Utilities.Update([addObj, AskObj], True, clearRect, YELLOWISH)
        Utilities.Sleep(1.5)
    Pending.seek(0)
    return Pend

def adminAccept(Pend):
    'Accept or reject words'
    for a in Pend:
        gs = False
        go = True
        Confirm = True
        AskObj = [NewInput.DispText('Accept or Reject', 32, BLUE, YELLOWISH, 'center', (xSize/2, ySize/5 + 150)), NewInput.DispText(a, 20, BLUE, YELLOWISH, 'center', (xSize/2, ySize/5 + 200))]
        Utilities.Update(AskObj)
        clearRect = Rect(4, ySize/6 + 50, xSize - 8, ySize/5 + 220)
        pygame.draw.rect(DISPSURF, BLACK, (0, ySize/6 + 48, xSize, ySize/5 + 225), 10)
        # Back Button
        BackImage0 = Back[0].get_rect()
        BackImage1 = Back[1].get_rect()
        BackHold0 = [Back[0], BackImage0]
        BackHold1 = [Back[1], BackImage1]
        BackImage0.center = (xSize/2, 625)
        BackImage1.center = (xSize/2, 625)
        resetBack = BackImage0.copy()
        while True:
            Mouse = pygame.mouse.get_pos()
            Click = pygame.mouse.get_pressed()[0]
            if BackImage0.left < Mouse[0] < BackImage0.right and BackImage0.top < Mouse[1] < BackImage0.bottom:
                gs = True
                checkClick = True
            else:
                gs = False
                checkClick = False
            if gs and not go:
                Utilities.Update([BackHold1], True, resetBack)
                go = True
            elif not gs and go:
                Utilities.Update([BackHold0], True, resetBack)
                go = False
            if checkClick and Click == 1:
                Pending.seek(0)
                File.seek(0)
                return [Pend, File.read().split(','), True]
            Utilities.Update(AskObj, True, clearRect, YELLOWISH)
            newWord = ''
            get = newWord
            go = False
            while isinstance(get, str):
                Mouse = pygame.mouse.get_pos()
                Click = pygame.mouse.get_pressed()[0]
                if BackImage0.left < Mouse[0] < BackImage0.right and BackImage0.top < Mouse[1] < BackImage0.bottom:
                    gs = True
                    checkClick = True
                else:
                    gs = False
                    checkClick = False
                if checkClick and Click == 1:
                    File.seek(0)
                    return [Pend, File.read().split(','), True]
                if gs and not go:
                    Utilities.Update([BackHold1], True, resetBack)
                    go = True
                elif not gs and go:
                    Utilities.Update([BackHold0], True, resetBack)
                    go = False
                wordObj = NewInput.DispText(newWord, 20, BLUE, YELLOWISH, 'center', (xSize/2, ySize/5 + 250))
                get = NewInput.Typed(get, 1)
                Utilities.Update([wordObj] + AskObj, True, clearRect, YELLOWISH)
                if isinstance(get, int):
                    continue
                newWord = "y or n: " + get
                added = get
            if added == 'y':
                File.write(',' + a)
                Pend[Pend.index(a)] = ''
                addObj = NewInput.DispText('Added!', 20, BLUE, YELLOWISH, 'center', (xSize/2, ySize/5 + 200))
                Utilities.Update([addObj, AskObj[0]], True, clearRect, YELLOWISH)
                Utilities.Sleep(1.5)
                break
            elif added == 'n':
                Pend[Pend.index(a)] = ''
                addObj = NewInput.DispText('Denied!', 20, BLUE, YELLOWISH, 'center', (xSize/2, ySize/5 + 200))
                Utilities.Update([addObj, AskObj[0]], True, clearRect, YELLOWISH)
                Utilities.Sleep(1.5)
                break
            else:
                addObj = NewInput.DispText('Answer not y or n!', 20, BLUE, YELLOWISH, 'center', (xSize/2, ySize/5 + 200))
                Utilities.Update([addObj, AskObj[0]], True, clearRect, YELLOWISH)
                Utilities.Sleep(1.5)
    File.seek(0)
    return [Pend, File.read().split(','), False]
