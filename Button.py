'''Clickable button class'''
import pygame, sys
from pygame.locals import *
pygame.init()

class Button():
    'creates a new button'
    def __init__(self, coords, image0, image1, runFunction, dynamic = False):
        'image0 is the idle button. image1 is highlighted.\nrunFunction takes a keyword for a runnable function in the parent function\ndynamic defines a growing or stationary button'
        assert isinstance(coords, tuple)
        self.x = coords[0]
        self.y = coords[1]
        self.coords = [self.x, self.y]
        self.image0 = image0
        self.image1 = image1
        self.images = [self.image0, self.image1]
        if dynamic:
            self.rect0 = self.image0.get_rect()
            self.rect1 = self.image1.get_rect()
            self.hold0 = [self.image0, self.rect0]
            self.hold1 = [self.image1, self.rect1]
            self.rect0.center = self.coords
            self.rect1.center = self.coords
            self.reset = self.rect1.copy()
        else:
            self.rectangle = self.image0.get_rect()
            self.hold0 = [self.image0, self.rectangle]
            self.hold1 = [self.image1, self.rectangle]
            self.rectangle.center = self.coords
            self.reset = self.rectangle.copy()
        self.run = runFunction
    def getx(): return self.x
    def gety(): return self.y
    def setx(x):
        self.coords[0] = x
        self.x = x
    def sety(y):
        self.coords[1] = y
        self.y = y

def checkClick(buttons, Update):
    'Update takes function with parameters for blitting one surface\nand filling a specified rectangle.\nButtons is a list of objects of class Button'
    if not isinstance(buttons, list): buttons = [buttons]
    check = {}  
    getMouse = pygame.mouse.get_pos()
    getClick = pygame.mouse.get_pressed()[0]
    for x in buttons:
        if (x.dynamic and (x.rect0.left < getMouse[0] < x.rect0.right and x.rect0.top < getMouse[1] < x.rect0.bottom)) or ((not x.dynamic) and (x.rectangle.left < getMouse[0] < x.rectangle.right and x.rectangle.top < getMouse[1] < x.rectangle.bottom)):
            check[x] = True
            Update([x.hold1], True, x.reset)
        else:
            check[x] = False
            Update([x.hold0], True, x.reset)
    if getClick:
        for c in buttons:
            Update([], True, c.reset)
            if check[c]: return c.runFunction
    return None
