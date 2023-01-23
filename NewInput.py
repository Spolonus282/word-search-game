''' ============== Input ===============
*** Created by Sam Polonus
*** This module is free-to-use and edit.
*** One source, eztext, made by EzMeNu,
*** Was used a a reference and is
*** not affiliated with this module.
'''

import pygame, sys
from pygame.locals import *
pygame.init()

HasTyped = 0 

'''todo:
        gather input with prompt
        display input
        record and return input'''

def DispText(prompt, fontSize, color1, color2, justify, coord,
             transBack = False, antialiasing = True,
             fontType = 'freesansbold.ttf'):
    'Display text'
    fontObj = pygame.font.Font(fontType, fontSize)
    textObj = fontObj.render(prompt, antialiasing, color1, color2)
    if transBack: textObj.set_colorkey(color2)
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
    if not isinstance(Key, str):
        raise TypeError('Key must be type str')
    if not isinstance(maxlen, int):
        raise TypeError('maxlen must be type int')
    Shifted = False
    Keys = pygame.key.get_pressed()
    global HasTyped
    if Keys[K_LSHIFT] or Keys[K_RSHIFT]: Shifted = True
    if Keys[K_RETURN]: return 1
    if Keys[K_BACKSPACE] and not HasTyped[K_BACKSPACE]: Key = Key[:-1]
    if not Shifted:
        if Keys[K_BACKQUOTE] and not HasTyped[K_BACKQUOTE]: Key += '`'
        elif Keys[K_1] and not HasTyped[K_1]: Key += '1'
        elif Keys[K_2] and not HasTyped[K_2]: Key += '2'
        elif Keys[K_3] and not HasTyped[K_3]: Key += '3'
        elif Keys[K_4] and not HasTyped[K_4]: Key += '4'
        elif Keys[K_5] and not HasTyped[K_5]: Key += '5'
        elif Keys[K_6] and not HasTyped[K_6]: Key += '6'
        elif Keys[K_7] and not HasTyped[K_7]: Key += '7'
        elif Keys[K_8] and not HasTyped[K_8]: Key += '8'
        elif Keys[K_9] and not HasTyped[K_9]: Key += '9'
        elif Keys[K_0] and not HasTyped[K_0]: Key += '0'
        elif Keys[K_MINUS] and not HasTyped[K_MINUS]: Key += '-'
        elif Keys[K_EQUALS] and not HasTyped[K_EQUALS]: Key += '='
        elif Keys[K_q] and not HasTyped[K_q]: Key += 'q'
        elif Keys[K_w] and not HasTyped[K_w]: Key += 'w'
        elif Keys[K_e] and not HasTyped[K_e]: Key += 'e'
        elif Keys[K_r] and not HasTyped[K_r]: Key += 'r'
        elif Keys[K_t] and not HasTyped[K_t]: Key += 't'
        elif Keys[K_y] and not HasTyped[K_y]: Key += 'y'
        elif Keys[K_u] and not HasTyped[K_u]: Key += 'u'
        elif Keys[K_i] and not HasTyped[K_i]: Key += 'i'
        elif Keys[K_o] and not HasTyped[K_o]: Key += 'o'
        elif Keys[K_p] and not HasTyped[K_p]: Key += 'p'
        elif Keys[K_LEFTBRACKET] and not HasTyped[K_LEFTBRACKET]: Key += '['
        elif Keys[K_RIGHTBRACKET] and not HasTyped[K_RIGHTBRACKET]: Key += ']'
        elif Keys[K_BACKSLASH] and not HasTyped[K_BACKSLASH]: Key += '\\'
        elif Keys[K_a] and not HasTyped[K_a]: Key += 'a'
        elif Keys[K_s] and not HasTyped[K_s]: Key += 's'
        elif Keys[K_d] and not HasTyped[K_d]: Key += 'd'
        elif Keys[K_f] and not HasTyped[K_f]: Key += 'f'
        elif Keys[K_g] and not HasTyped[K_g]: Key += 'g'
        elif Keys[K_h] and not HasTyped[K_h]: Key += 'h'
        elif Keys[K_j] and not HasTyped[K_j]: Key += 'j'
        elif Keys[K_k] and not HasTyped[K_k]: Key += 'k'
        elif Keys[K_l] and not HasTyped[K_l]: Key += 'l'
        elif Keys[K_SEMICOLON] and not HasTyped[K_SEMICOLON]: Key += ';'
        elif Keys[K_QUOTE] and not HasTyped[K_QUOTE]: Key += '\''
        elif Keys[K_z] and not HasTyped[K_z]: Key += 'z'
        elif Keys[K_x] and not HasTyped[K_x]: Key += 'x'
        elif Keys[K_c] and not HasTyped[K_c]: Key += 'c'
        elif Keys[K_v] and not HasTyped[K_v]: Key += 'v'
        elif Keys[K_b] and not HasTyped[K_b]: Key += 'b'
        elif Keys[K_n] and not HasTyped[K_n]: Key += 'n'
        elif Keys[K_m] and not HasTyped[K_m]: Key += 'm'
        elif Keys[K_COMMA] and not HasTyped[K_COMMA]: Key += ','
        elif Keys[K_PERIOD] and not HasTyped[K_PERIOD]: Key += '.'
        elif Keys[K_SLASH] and not HasTyped[K_SLASH]: Key += '/'
        elif Keys[K_SPACE] and not HasTyped[K_SPACE]: Key += ' '
    elif Shifted:
        if Keys[K_BACKQUOTE] and not HasTyped[K_BACKQUOTE]: Key += '~'
        elif Keys[K_1] and not HasTyped[K_1]: Key += '!'
        elif Keys[K_2] and not HasTyped[K_2]: Key += '@'
        elif Keys[K_3] and not HasTyped[K_3]: Key += '#'
        elif Keys[K_4] and not HasTyped[K_4]: Key += '$'
        elif Keys[K_5] and not HasTyped[K_5]: Key += '%'
        elif Keys[K_6] and not HasTyped[K_6]: Key += '^'
        elif Keys[K_7] and not HasTyped[K_7]: Key += '&'
        elif Keys[K_8] and not HasTyped[K_8]: Key += '*'
        elif Keys[K_9] and not HasTyped[K_9]: Key += '('
        elif Keys[K_0] and not HasTyped[K_0]: Key += ')'
        elif Keys[K_MINUS] and not HasTyped[K_MINUS]: Key += '_'
        elif Keys[K_EQUALS] and not HasTyped[K_EQUALS]: Key += '+'
        elif Keys[K_q] and not HasTyped[K_q]: Key += 'Q'
        elif Keys[K_w] and not HasTyped[K_w]: Key += 'W'
        elif Keys[K_e] and not HasTyped[K_e]: Key += 'E'
        elif Keys[K_r] and not HasTyped[K_r]: Key += 'R'
        elif Keys[K_t] and not HasTyped[K_t]: Key += 'T'
        elif Keys[K_y] and not HasTyped[K_y]: Key += 'Y'
        elif Keys[K_u] and not HasTyped[K_u]: Key += 'U'
        elif Keys[K_i] and not HasTyped[K_i]: Key += 'I'
        elif Keys[K_o] and not HasTyped[K_o]: Key += 'O'
        elif Keys[K_p] and not HasTyped[K_p]: Key += 'P'
        elif Keys[K_LEFTBRACKET] and not HasTyped[K_LEFTBRACKET]: Key += '{'
        elif Keys[K_RIGHTBRACKET] and not HasTyped[K_RIGHTBRACKET]: Key += '}'
        elif Keys[K_BACKSLASH] and not HasTyped[K_BACKSLASH]: Key += '|'
        elif Keys[K_a] and not HasTyped[K_a]: Key += 'A'
        elif Keys[K_s] and not HasTyped[K_s]: Key += 'S'
        elif Keys[K_d] and not HasTyped[K_d]: Key += 'D'
        elif Keys[K_f] and not HasTyped[K_f]: Key += 'F'
        elif Keys[K_g] and not HasTyped[K_g]: Key += 'G'
        elif Keys[K_h] and not HasTyped[K_h]: Key += 'H'
        elif Keys[K_j] and not HasTyped[K_j]: Key += 'J'
        elif Keys[K_k] and not HasTyped[K_k]: Key += 'K'
        elif Keys[K_l] and not HasTyped[K_l]: Key += 'L'
        elif Keys[K_SEMICOLON] and not HasTyped[K_SEMICOLON]: Key += ':'
        elif Keys[K_QUOTE] and not HasTyped[K_QUOTE]: Key += '"'
        elif Keys[K_z] and not HasTyped[K_z]: Key += 'Z'
        elif Keys[K_x] and not HasTyped[K_x]: Key += 'X'
        elif Keys[K_c] and not HasTyped[K_c]: Key += 'C'
        elif Keys[K_v] and not HasTyped[K_v]: Key += 'V'
        elif Keys[K_b] and not HasTyped[K_b]: Key += 'B'
        elif Keys[K_n] and not HasTyped[K_n]: Key += 'N'
        elif Keys[K_m] and not HasTyped[K_m]: Key += 'M'
        elif Keys[K_COMMA] and not HasTyped[K_COMMA]: Key += '<'
        elif Keys[K_PERIOD] and not HasTyped[K_PERIOD]: Key += '>'
        elif Keys[K_SLASH] and not HasTyped[K_SLASH]: Key += '?'
    while len(Key) > maxlen: Key = Key[:-1]
    HasTyped = Keys
    return Key

def TypedNumeric(Key, maxlen):
    'Check for typed numbers and operations'
    if not isinstance(Key, str):
        raise TypeError('Key must be type str')
    if not isinstance(maxlen, int):
        raise TypeError('maxlen must be type int')
    Keys = pygame.key.get_pressed()
    global HasTyped
    if not any(Keys): HasTyped = False
    if HasTyped: return Key
    if any(Keys): HasTyped = True
    if Keys[K_LSHIFT] or Keys[K_RSHIFT]: Shifted = True
    if Keys[K_RETURN]: return 1
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

