''' ========== PlayersGui ==========
*** Created by Sam Polonus
*** This module is free-to-use and edit.
*** Created on February 22, 2017.
*** No other sources were used.
'''

#import and initialize
import pygame, Input, Utilities, os.path
from pygame.locals import *
pygame.init()
DISPSURF = ''
Pending = ''
Pend = ''
File = ''
xSize = 800
ySize = 700
BLACK     = (  0,   0,   0)
WHITE     = (255, 255, 255)
RED       = (255,   0,   0)
GREEN     = (  0, 255,   0)
BLUE      = (  0,   0, 128)
YELLOWISH = (238, 221, 130)
BROWNED   = (245, 222, 179)

font = 'freesansbold.ttf'

'''todo:
        Change code to pygame supported'''

class Players:
    'Name, Surface object -> new object\nThe players that are on this save file'
    totPlayers = 0

    def __init__(self, name):
        bestWord = 'None'
        bestScore = 0
        high = 0
        Players.totPlayers += 1
        self.name = name
        self.bestWord = bestWord
        self.high = high
        self.bestScore = bestScore

    def checkHigh(self, score, x, y, color, size):
        'Check high score'
        if score > self.high:
            self.high = score
            Change = ''.join(['New high score for ', self.name, ': ', str(self.high), '!'])
            ChangeObj = Input.DispText(Change, font, size, color[0], color[1], True, 'center', (x, y))
            DISPSURF.blit(ChangeObj[0], ChangeObj[1])
        else:
            NoChange = ''.join(['The high score remains at: ', str(self.high), '.'])
            NoChangeObj = Input.DispText(NoChange, font, size, color[0], color[1], True, 'center', (x, y))
            DISPSURF.blit(NoChangeObj[0], NoChangeObj[1])

    def checkBest(self, words, x1, y1, color, size):
        'Check best word'
        if self.bestWord == '':
            self.bestWord = 'None'
        grats = False
        for t in range(0,len(words)):
            wordScore = 0
            q = len(words[t])
            if q in (3,4):
                wordScore += 1
            elif q == 5:
                wordScore += 2
            elif q == 6:
                wordScore += 3
            elif q == 7:
                wordScore += 5
            elif q >= 8:
                wordScore += 11
            temp = words[t]
            x = ['a' in temp, 'b' in temp, 'c' in temp, 'd' in temp,
                 'e' in temp, 'f' in temp, 'g' in temp, 'h' in temp,
                 'i' in temp, 'j' in temp, 'k' in temp, 'l' in temp,
                 'm' in temp, 'n' in temp, 'o' in temp, 'p' in temp,
                 'q' in temp, 'r' in temp, 's' in temp, 't' in temp,
                 'u' in temp, 'v' in temp, 'w' in temp, 'x' in temp,
                 'y' in temp, 'z' in temp]
            if any([x[0],x[4],x[8],x[11],x[14],x[17],x[18],x[19],x[20]]):
                z = [x[0],x[4],x[8],x[11],x[14],x[17],x[18],x[19],x[20]]
                for y in range(z.count(True)):
                    wordScore += 1
            if any([x[1],x[2],x[7],x[13],x[15]]):
                z = [x[1],x[2],x[7],x[13],x[15]]
                for y in range(z.count(True)):
                    wordScore += 2
            if any([x[3],x[6],x[12]]):
                z = [x[3],x[6],x[12]]
                for y in range(z.count(True)):
                    wordScore += 3
            if any([x[5],x[22],x[24]]):
                z = [x[5],x[22],x[24]]
                for y in range(z.count(True)):
                    wordScore += 4
            if any([x[10],x[21]]):
                z = [x[10],x[21]]
                for y in range(z.count(True)):
                    wordScore += 5
            if any([x[9],x[23]]):
                z = [x[9],x[23]]
                for y in range(z.count(True)):
                    wordScore += 8
            if any([x[16],x[25]]):
                z = [x[16],x[25]]
                for y in range(z.count(True)):
                    wordScore += 10
            if wordScore > self.bestScore:
                self.bestScore = wordScore
                self.bestWord = words[t]
                grats = True
        if grats:
            Word = ''.join(['New best word for ', self.name, ': ', self.bestWord, '!'])
            WordObj = Input.DispText(Word, font, size, color[0], color[1], True, 'center', (x1, y1))
            DISPSURF.blit(WordObj[0], WordObj[1])
        else:
            NoWord = ''.join(['The best word remains at: ', self.bestWord, '.'])
            NoWordObj = Input.DispText(NoWord, font, size, color[0], color[1], True, 'center', (x1, y1))
            DISPSURF.blit(NoWordObj[0], NoWordObj[1])

def AddPlayer(Users = {}):
    'Adds a new player'
    TimeChange = 180
    string = 'Type your name: '
    name = [False, string]
    Objs = Input.DispText('Welcome to Word Search!', font, 32, BLUE, BROWNED, True, 'center', (xSize/2, ySize/6))
    BoundRect = Objs[1].copy()
    while name[0] != 'return':
        Objs = Input.DispText('Welcome to Word Search!', font, 32, BLUE, BROWNED, True, 'center', (xSize/2, ySize/6))
        InputObjs = Input.DispText(string, font, 32, BLUE, GREEN, True, 'center', (xSize/2, ySize/2))
        name = Input.Typed(name[1], name[0], 24, [File, [Pending, Pend]])
        string = ''.join(name[1])
        pygame.draw.polygon(DISPSURF, GREEN, ((100, 350), (400, 75), (700, 350), (400, 625)))
        pygame.draw.rect(DISPSURF, BLACK, BoundRect, 5)
        Utilities.Update([InputObjs, Objs])
    NewUserTemp = name[1].lstrip('Typeournam ')
    NewUser = NewUserTemp.lstrip(': ')
    if NewUser == '#dev#':
        NewUser = 'Sam'
        TimeChange = 4
    fileOpener = ''.join(["Players/",NewUser,'.txt'])
    if os.path.exists(fileOpener):
        reload = open(fileOpener, 'r')
        reload.seek(0)
        b = reload.read().split(',')
        Users[NewUser] = Players(NewUser)
        try:
            Users[NewUser].bestWord = b[0]
            Users[NewUser].high = int(b[1])
            Users[NewUser].bestScore = int(b[2])
        except IndexError:
            Users[NewUser].bestWord = ''
            Users[NewUser].high = 0
            Users[NewUser].bestScore = 0
        reload = open(fileOpener, 'w')
    else:
        reload = open(fileOpener, 'w')
        Users[NewUser] = Players(NewUser)
    Welcome = ''.join(['Hello, ', NewUser, '. Let\'s begin!'])
    h = 350
    WelcomeObjs = Input.DispText(Welcome, font, 32, RED, GREEN, True, 'center', (xSize/2, h))
    pygame.draw.polygon(DISPSURF, GREEN, ((100, 350), (400, 75), (700, 350), (400, 625)))
    pygame.draw.rect(DISPSURF, BLACK, BoundRect, 5)
    Utilities.Update([WelcomeObjs, Objs], True, InputObjs[1])
    Utilities.Sleep(1.5)
    cleanUp = WelcomeObjs[1].copy()
    cleanUp.h += 15
    UserObjs = Input.DispText(NewUser, font, 32, BLUE, BROWNED, True, 'topright', (750, 25))
    pygame.draw.rect(DISPSURF, BROWNED, (100, 75, 600, 600))
    pygame.draw.rect(DISPSURF, BLACK, BoundRect, 5)
    Utilities.Update([UserObjs, Objs], True, cleanUp)
    return [NewUser, Users, reload, TimeChange, UserObjs[1]]
