''' ============== Input ===============
*** Created by Sam Polonus
*** This module is free-to-use and edit.
*** Created on Frebruary 17, 2017.
*** One source, eztext, made by EzMeNu,
*** Was used a a reference and is
*** not affiliated with this module.
'''

import pygame, sys
from pygame.locals import *
pygame.init()

'''todo:
        gather input with prompt
        display input
        record and return input'''

def DispText(prompt, fontSize, color1, color2, justify, coord, antialiasing = True, fontType = 'freesansbold.ttf'):
    'Display text'
    fontObj = pygame.font.Font(fontType, fontSize)
    textObj = fontObj.render(prompt, antialiasing, color1, color2)
    rectObj = textObj.get_rect()
    if justify == 'center':
        rectObj.center = coord
    elif justify == 'topleft':
        rectObj.topleft = coord
    elif justify == 'topright':
        rectObj.topright = coord
    elif justify == 'bottomleft':
        rectObj.bottomleft = coord
    elif justify == 'bottomright':
        rectObj.bottomright = coord
    return [textObj, rectObj]

def Typed(Key, maxlen):
    'Check for typed input'
    Shifted = False
    Keys = pygame.key.get_pressed()
    if Keys[K_LSHIFT] or Keys[K_RSHIFT]: Shifted = True
    if Keys[K_RETURN]: return 'return'
    if Keys[K_BACKSPACE]: Key = Key[:-1]
    if not Shifted:
        if Keys[K_BACKQUOTE]: Key += '`'
        elif Keys[K_1]: Key += '1'
        elif Keys[K_2]: Key += '2'
        elif Keys[K_3]: Key += '3'
        elif Keys[K_4]: Key += '4'
        elif Keys[K_5]: Key += '5'
        elif Keys[K_6]: Key += '6'
        elif Keys[K_7]: Key += '7'
        elif Keys[K_8]: Key += '8'
        elif Keys[K_9]: Key += '9'
        elif Keys[K_0]: Key += '0'
        elif Keys[K_MINUS]: Key += '-'
        elif Keys[K_EQUALS]: Key += '='
        elif Keys[K_q]: Key += 'q'
        elif Keys[K_w]: Key += 'w'
        elif Keys[K_e]: Key += 'e'
        elif Keys[K_r]: Key += 'r'
        elif Keys[K_t]: Key += 't'
        elif Keys[K_y]: Key += 'y'
        elif Keys[K_u]: Key += 'u'
        elif Keys[K_i]: Key += 'i'
        elif Keys[K_o]: Key += 'o'
        elif Keys[K_p]: Key += 'p'
        elif Keys[K_LEFTBRACKET]: Key += '['
        elif Keys[K_RIGHTBRACKET]: Key += ']'
        elif Keys[K_BACKSLASH]: Key += '\\'
        elif Keys[K_a]: Key += 'a'
        elif Keys[K_s]: Key += 's'
        elif Keys[K_d]: Key += 'd'
        elif Keys[K_f]: Key += 'f'
        elif Keys[K_g]: Key += 'g'
        elif Keys[K_h]: Key += 'h'
        elif Keys[K_j]: Key += 'j'
        elif Keys[K_k]: Key += 'k'
        elif Keys[K_l]: Key += 'l'
        elif Keys[K_SEMICOLON]: Key += ';'
        elif Keys[K_QUOTE]: Key += '\''
        elif Keys[K_z]: Key += 'z'
        elif Keys[K_x]: Key += 'x'
        elif Keys[K_c]: Key += 'c'
        elif Keys[K_v]: Key += 'v'
        elif Keys[K_b]: Key += 'b'
        elif Keys[K_n]: Key += 'n'
        elif Keys[K_m]: Key += 'm'
        elif Keys[K_COMMA]: Key += ','
        elif Keys[K_PERIOD]: Key += '.'
        elif Keys[K_SLASH]: Key += '/'
        elif Keys[K_SPACE]: Key += ' '
    elif Shifted:
        if Keys[K_BACKQUOTE]: Key += '~'
        elif Keys[K_1]: Key += '!'
        elif Keys[K_2]: Key += '@'
        elif Keys[K_3]: Key += '#'
        elif Keys[K_4]: Key += '$'
        elif Keys[K_5]: Key += '%'
        elif Keys[K_6]: Key += '^'
        elif Keys[K_7]: Key += '&'
        elif Keys[K_8]: Key += '*'
        elif Keys[K_9]: Key += '('
        elif Keys[K_0]: Key += ')'
        elif Keys[K_MINUS]: Key += '_'
        elif Keys[K_EQUALS]: Key += '+'
        elif Keys[K_q]: Key += 'Q'
        elif Keys[K_w]: Key += 'W'
        elif Keys[K_e]: Key += 'E'
        elif Keys[K_r]: Key += 'R'
        elif Keys[K_t]: Key += 'T'
        elif Keys[K_y]: Key += 'Y'
        elif Keys[K_u]: Key += 'U'
        elif Keys[K_i]: Key += 'I'
        elif Keys[K_o]: Key += 'O'
        elif Keys[K_p]: Key += 'P'
        elif Keys[K_LEFTBRACKET]: Key += '{'
        elif Keys[K_RIGHTBRACKET]: Key += '}'
        elif Keys[K_BACKSLASH]: Key += '|'
        elif Keys[K_a]: Key += 'A'
        elif Keys[K_s]: Key += 'S'
        elif Keys[K_d]: Key += 'D'
        elif Keys[K_f]: Key += 'F'
        elif Keys[K_g]: Key += 'G'
        elif Keys[K_h]: Key += 'H'
        elif Keys[K_j]: Key += 'J'
        elif Keys[K_k]: Key += 'K'
        elif Keys[K_l]: Key += 'L'
        elif Keys[K_SEMICOLON]: Key += ':'
        elif Keys[K_QUOTE]: Key += '"'
        elif Keys[K_z]: Key += 'Z'
        elif Keys[K_x]: Key += 'X'
        elif Keys[K_c]: Key += 'C'
        elif Keys[K_v]: Key += 'V'
        elif Keys[K_b]: Key += 'B'
        elif Keys[K_n]: Key += 'N'
        elif Keys[K_m]: Key += 'M'
        elif Keys[K_COMMA]: Key += '<'
        elif Keys[K_PERIOD]: Key += '>'
        elif Keys[K_SLASH]: Key += '?'
    while len(Key) > maxlen: Key = Key[:-1]
    return Key

def TypedNumeric(Key, maxlen):
    'Check for typed numbers and operations'
    Keys = pygame.key.get_pressed()
    if Keys[K_LSHIFT] or Keys[K_RSHIFT]: Shifted = True
    if Keys[K_RETURN]: return 'return'
    if Keys[K_BACKSPACE]: Key = Key[:-1]
    if not Shifted:
        if Keys[K_1]: Key += '1'
        elif Keys[K_2]: Key += '2'
        elif Keys[K_3]: Key += '3'
        elif Keys[K_4]: Key += '4'
        elif Keys[K_5]: Key += '5'
        elif Keys[K_6]: Key += '6'
        elif Keys[K_7]: Key += '7'
        elif Keys[K_8]: Key += '8'
        elif Keys[K_9]: Key += '9'
        elif Keys[K_0]: Key += '0'
        elif Keys[K_MINUS]: Key += '-'
        elif Keys[K_EQUALS]: Key += '='
        elif Keys[K_PERIOD]: Key += '.'
        elif Keys[K_SLASH]: Key += '/'
    elif Shifted:
        if Keys[K_5]: Key += '%'
        elif Keys[K_8]: Key += '*'
        elif Keys[K_9]: Key += '('
        elif Keys[K_0]: Key += ')'
        elif Keys[K_EQUALS]: Key += '+'
        elif Keys[K_COMMA]: Key += '<'
        elif Keys[K_PERIOD]: Key += '>'
    while len(Key) > maxlen: Key = Key[:-1]
    return Key
