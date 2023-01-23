# import and initialize
import pygame, Input, Utilities
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
    AskObj = Input.DispText('Add words to Dictionary', font, 32, BLUE, YELLOWISH, True, 'center', (xSize/2, ySize/5 + 150))
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
        newWord = 'Input word: '
        get = [False, newWord]
        go = False
        while get[0] != 'return':
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
            wordObj = Input.DispText(newWord, font, 20, BLUE, YELLOWISH, True, 'center', (xSize/2, ySize/5 + 200))
            get = Input.Typed(get[1], get[0], 33, [File, [Pending, Pend], file2])
            Utilities.Update([wordObj, AskObj], True, clearRect, YELLOWISH)
            newWord = ''.join(get[1])
        wordTemp = get[1].lstrip('Inputword()#esca= ')
        added = wordTemp.lstrip(': ')
        if len(str(added)) < 3:
            shortObj = Input.DispText('Word too short!', font, 20, BLUE, YELLOWISH, True, 'center', (xSize/2, ySize/5 + 200))
            Utilities.Update([shortObj, AskObj], True, clearRect, YELLOWISH)
        else:
            Pend.append(added)
            addObj = Input.DispText('Added!', font, 20, BLUE, YELLOWISH, True, 'center', (xSize/2, ySize/5 + 200))
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
        AskObj = [Input.DispText('Accept or Reject', font, 32, BLUE, YELLOWISH, True, 'center', (xSize/2, ySize/5 + 150)), Input.DispText(a, font, 20, BLUE, YELLOWISH, True, 'center', (xSize/2, ySize/5 + 200))]
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
            newWord = 'y or n: '
            get = [False, newWord]
            go = False
            while get[0] != 'return':
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
                wordObj = Input.DispText(newWord, font, 20, BLUE, YELLOWISH, True, 'center', (xSize/2, ySize/5 + 250))
                get = Input.Typed(get[1], get[0], 33, [File, [Pending, Pend], file2])
                Utilities.Update([wordObj] + AskObj, True, clearRect, YELLOWISH)
                newWord = ''.join(get[1])
            wordTemp = get[1].lstrip('yorn ')
            added = wordTemp.lstrip(': ')
            if added == 'y':
                File.write(',' + a)
                Pend[Pend.index(a)] = ''
                addObj = Input.DispText('Added!', font, 20, BLUE, YELLOWISH, True, 'center', (xSize/2, ySize/5 + 200))
                Utilities.Update([addObj, AskObj[0]], True, clearRect, YELLOWISH)
                Utilities.Sleep(1.5)
                break
            elif added == 'n':
                Pend[Pend.index(a)] = ''
                addObj = Input.DispText('Denied!', font, 20, BLUE, YELLOWISH, True, 'center', (xSize/2, ySize/5 + 200))
                Utilities.Update([addObj, AskObj[0]], True, clearRect, YELLOWISH)
                Utilities.Sleep(1.5)
                break
            else:
                addObj = Input.DispText('Answer not y or n!', font, 20, BLUE, YELLOWISH, True, 'center', (xSize/2, ySize/5 + 200))
                Utilities.Update([addObj, AskObj[0]], True, clearRect, YELLOWISH)
                Utilities.Sleep(1.5)
    File.seek(0)
    return [Pend, File.read().split(','), False]
