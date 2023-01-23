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

'''todo:
        gather input with prompt
        display input
        record and return input'''

def DispText(prompt, fontType, fontSize, color1, color2, antialiasing, side, dim):
    'Display text'
    fontObj = pygame.font.Font(fontType, fontSize)
    textObj = fontObj.render(prompt, antialiasing, color1, color2)
    rectObj = textObj.get_rect()
    if side == 'center':
        rectObj.center = dim
    elif side == 'topleft':
        rectObj.topleft = dim
    elif side == 'topright':
        rectObj.topright = dim
    return [textObj, rectObj]

def Typed(Key, Shifted, maxlen, File):
    'Check for typed input'
    for event in pygame.event.get():
        if event.type == QUIT:
            try:
                a = File[2][1]
                b = File[2][0]
                loadWord = a[b].bestWord
                loadHigh = str(a[b].high)
                loadScore = str(a[b].bestScore)
                load = ','.join([loadWord, loadHigh, loadScore])
                File[2][2].write(load)
                File[2][2].close()
            except IndexError:
                File[0]
            File[1][0].seek(0)
            File[1][0].write(','.join(File[1][1]))
            File[1][0].close()
            File[0].close()
            pygame.quit()
            sys.exit()
        if event.type == KEYUP:
            if event.key == K_LSHIFT or event.key == K_RSHIFT:
                Shifted = False
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                try:
                    a = File[2][1]
                    b = File[2][0]
                    loadWord = a[b].bestWord
                    loadHigh = str(a[b].high)
                    loadScore = str(a[b].bestScore)
                    load = ','.join([loadWord, loadHigh, loadScore])
                    File[2][2].write(load)
                    File[2][2].close()
                except IndexError:
                    File[0]
                File[1][0].seek(0)
                File[1][0].write(','.join(File[1][1]))
                File[1][0].close()
                File[0].close()
                pygame.quit()
                sys.exit()
            elif event.key == K_RETURN: return ['return', Key]
            elif event.key == K_BACKSPACE:
                Key = Key[:-1]
            elif event.key == K_LSHIFT or event.key == K_RSHIFT:
                Shifted = True
            if not Shifted:
                if event.key == K_BACKQUOTE: Key += '`'
                elif event.key == K_1: Key += '1'
                elif event.key == K_2: Key += '2'
                elif event.key == K_3: Key += '3'
                elif event.key == K_4: Key += '4'
                elif event.key == K_5: Key += '5'
                elif event.key == K_6: Key += '6'
                elif event.key == K_7: Key += '7'
                elif event.key == K_8: Key += '8'
                elif event.key == K_9: Key += '9'
                elif event.key == K_0: Key += '0'
                elif event.key == K_MINUS: Key += '-'
                elif event.key == K_EQUALS: Key += '='
                elif event.key == K_q: Key += 'q'
                elif event.key == K_w: Key += 'w'
                elif event.key == K_e: Key += 'e'
                elif event.key == K_r: Key += 'r'
                elif event.key == K_t: Key += 't'
                elif event.key == K_y: Key += 'y'
                elif event.key == K_u: Key += 'u'
                elif event.key == K_i: Key += 'i'
                elif event.key == K_o: Key += 'o'
                elif event.key == K_p: Key += 'p'
                elif event.key == K_LEFTBRACKET: Key += '['
                elif event.key == K_RIGHTBRACKET: Key += ']'
                elif event.key == K_BACKSLASH: Key += '\\'
                elif event.key == K_a: Key += 'a'
                elif event.key == K_s: Key += 's'
                elif event.key == K_d: Key += 'd'
                elif event.key == K_f: Key += 'f'
                elif event.key == K_g: Key += 'g'
                elif event.key == K_h: Key += 'h'
                elif event.key == K_j: Key += 'j'
                elif event.key == K_k: Key += 'k'
                elif event.key == K_l: Key += 'l'
                elif event.key == K_SEMICOLON: Key += ';'
                elif event.key == K_QUOTE: Key += '\''
                elif event.key == K_z: Key += 'z'
                elif event.key == K_x: Key += 'x'
                elif event.key == K_c: Key += 'c'
                elif event.key == K_v: Key += 'v'
                elif event.key == K_b: Key += 'b'
                elif event.key == K_n: Key += 'n'
                elif event.key == K_m: Key += 'm'
                elif event.key == K_COMMA: Key += ','
                elif event.key == K_PERIOD: Key += '.'
                elif event.key == K_SLASH: Key += '/'
                elif event.key == K_SPACE: Key += ' '
                while len(Key) > maxlen:
                    Key = Key[:-1]
            elif Shifted:
                if event.key == K_BACKQUOTE: Key += '~'
                elif event.key == K_1: Key += '!'
                elif event.key == K_2: Key += '@'
                elif event.key == K_3: Key += '#'
                elif event.key == K_4: Key += '$'
                elif event.key == K_5: Key += '%'
                elif event.key == K_6: Key += '^'
                elif event.key == K_7: Key += '&'
                elif event.key == K_8: Key += '*'
                elif event.key == K_9: Key += '('
                elif event.key == K_0: Key += ')'
                elif event.key == K_MINUS: Key += '_'
                elif event.key == K_EQUALS: Key += '+'
                elif event.key == K_q: Key += 'Q'
                elif event.key == K_w: Key += 'W'
                elif event.key == K_e: Key += 'E'
                elif event.key == K_r: Key += 'R'
                elif event.key == K_t: Key += 'T'
                elif event.key == K_y: Key += 'Y'
                elif event.key == K_u: Key += 'U'
                elif event.key == K_i: Key += 'I'
                elif event.key == K_o: Key += 'O'
                elif event.key == K_p: Key += 'P'
                elif event.key == K_LEFTBRACKET: Key += '{'
                elif event.key == K_RIGHTBRACKET: Key += '}'
                elif event.key == K_BACKSLASH: Key += '|'
                elif event.key == K_a: Key += 'A'
                elif event.key == K_s: Key += 'S'
                elif event.key == K_d: Key += 'D'
                elif event.key == K_f: Key += 'F'
                elif event.key == K_g: Key += 'G'
                elif event.key == K_h: Key += 'H'
                elif event.key == K_j: Key += 'J'
                elif event.key == K_k: Key += 'K'
                elif event.key == K_l: Key += 'L'
                elif event.key == K_SEMICOLON: Key += ':'
                elif event.key == K_QUOTE: Key += '"'
                elif event.key == K_z: Key += 'Z'
                elif event.key == K_x: Key += 'X'
                elif event.key == K_c: Key += 'C'
                elif event.key == K_v: Key += 'V'
                elif event.key == K_b: Key += 'B'
                elif event.key == K_n: Key += 'N'
                elif event.key == K_m: Key += 'M'
                elif event.key == K_COMMA: Key += '<'
                elif event.key == K_PERIOD: Key += '>'
                elif event.key == K_SLASH: Key += '?'
                while len(Key) > maxlen:
                    Key = Key[:-1]
            return [Shifted, Key]
    return [Shifted, Key]
