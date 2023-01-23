# Import and initilize
import time, random, Input, Utilities, Check
File  = ''
file2 = ''
Pending = ''
Pend = ''
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

def ChooseDie(UsedOnes):
    'Letters - UsedOnes -> new random letter'
    LetterString = 'ABCDEFGHIJKLMNOP'
    Letters = {'A': ['A','E','A','N','E','G'], 'B': ['A','H','S','P','C','O'],
               'C': ['A','S','P','F','F','K'], 'D': ['O','B','J','O','A','B'],
               'E': ['I','O','T','M','U','C'], 'F': ['R','Y','V','D','E','L'],
               'G': ['L','R','E','I','X','D'], 'H': ['E','I','U','N','E','S'],
               'I': ['W','N','G','E','E','H'], 'J': ['L','N','H','N','R','Z'],
               'K': ['T','S','T','I','Y','D'], 'L': ['O','W','T','O','A','T'],
               'M': ['E','R','T','T','Y','L'], 'N': ['T','O','E','S','S','I'],
               'O': ['T','E','R','W','H','V'], 'P': ['N','U','I','H','M','Q']}
    x = random.choice(LetterString)
    z = [x, random.choice(Letters[x])]
    return z

def CalcBoard():
    'Call -> random board'
    holdGen = {}
    GenChar = []
    Gen = []
    for t in range(1, 17):
        holdGen['Die{0}'.format(t)] = ChooseDie(Gen)
        GenChar.append(holdGen['Die{0}'.format(t)][1])
        Gen.append(holdGen['Die{0}'.format(t)][0])
    generatorObj = []
    a = 225
    b = 125
    for p in range(0, 16):
        if p == 4 or p == 8 or p == 12:
            a = 225
            b = b + 105
        generatorObj.append(Input.DispText(GenChar[p], font, 48, BLUE, BROWNED, True, 'topleft', (a, b)))
        Utilities.Update(generatorObj)
        a = a + 105
    return GenChar

def GenScore(words):
    'words -> score'
    temp = words
    WordScores = {3: 1, 4: 1, 5: 2, 6: 3, 7: 5}
    LetterScores = {'a': 1, 'b': 2, 'c': 2, 'd': 3,
                    'e': 1, 'f': 5, 'g': 3, 'h': 2,
                    'i': 1, 'j': 8, 'k': 5, 'l': 1,
                    'm': 3, 'n': 2, 'o': 1, 'p': 2,
                    'q': 10,'r': 1, 's': 1, 't': 1,
                    'u': 1, 'v': 5, 'w': 4, 'x': 8,
                    'y': 4, 'z': 10}
    wordScore = 0
    if not len(temp) >= 8:
        wordScore += WordScores[len(temp)]
    else:
        wordScore += 11
    for a in temp:
        wordScore += LetterScores[a]
    return wordScore

def GatherWords(Surface, Words, Timeout, byebyeRect, RectanglePack, ScoreGone, BackPack):
    'Handles the main game'
    x = 25
    y = 100
    WordCount = 0
    lowered = Utilities.Lower(Surface)
    check = True
    Score = 0
    Valids = []
    Inputs = []
    TimeLeft = Timeout
    t = 0
    byebyeRect.center = (xSize/2, 625)
    Utilities.Sleep(1)
    CountDown = Input.DispText('Ready', font, 48, RED, BROWNED, True, 'center', (xSize/2, 600))
    for g in range(255, 0, -2):
        CountDown[0].set_alpha(g)
        Utilities.Update([CountDown], True, byebyeRect)
    Utilities.Sleep(0.5)
    CountDown1 = Input.DispText('Set', font, 48, RED, BROWNED, True, 'center', (xSize/2, 600))
    for g in range(255, 0, -2):
        CountDown1[0].set_alpha(g)
        Utilities.Update([CountDown1], True, byebyeRect)
    Utilities.Sleep(0.5)
    CountDown2 = Input.DispText('Go!', font, 48, RED, BROWNED, True, 'center', (xSize/2, 600))
    Utilities.Update([CountDown2], True, byebyeRect)
    Utilities.Sleep(1)
    StartPoint = time.clock()
    WordScoreObj = Input.DispText('Word: %i' %0, font, 32, GREEN, BROWNED, True, 'center', (125, 590))
    ScoreObjs = Input.DispText('Score: ' + str(Score), font, 32, GREEN, BROWNED, True, 'center', (125, 625))
    Count1Obj = Input.DispText('Words', font, 32, GREEN, BROWNED, True, 'center', (650, 590))
    Count2Obj = Input.DispText('Found: %i' %WordCount, font, 32, GREEN, BROWNED, True, 'center', (650, 625))
    BackPack()
    Utilities.Update([ScoreObjs, WordScoreObj, Count1Obj, Count2Obj], True, [ScoreObjs[1], ScoreGone])
    RectanglePack()
    Utilities.Update()
    while True:
        WordTyped = ''
        Guess = [False, WordTyped]
        DispHeaderObj = Input.DispText('Words:', font, 20, RED, BROWNED, True, 'center', (xSize/2, 550))
        Utilities.Update([DispHeaderObj])
        while Guess[0] != 'return':
            timerObj = Utilities.checkTimer(StartPoint, TimeLeft)
            DispGuessObj = Input.DispText(WordTyped, font, 16, RED, BROWNED, True, 'center', (xSize/2, 575))
            Guess = Input.Typed(Guess[1], Guess[0], 10, [File, [Pending, Pend], file2])
            WordTyped = ''.join(Guess[1])
            Utilities.Update([DispGuessObj, timerObj[1]], True, byebyeRect)
            if timerObj[0]:
                break
        if timerObj[0]:
            break
        WordTyped = Utilities.Lower(WordTyped)
        o = WordTyped
        if t > 0:
            if o in Inputs:
                deniedObj = Input.DispText('You said that already.', font, 16, RED, BROWNED, True, 'center', (xSize/2, 575))
                timerObj = Utilities.checkTimer(StartPoint, TimeLeft)
                ScoreObjs = Input.DispText('Score: ' + str(Score), font, 32, GREEN, BROWNED, True, 'center', (125, 625))
                WordScoreObj = Input.DispText('Word: %i' %0, font, 32, GREEN, BROWNED, True, 'center', (125, 590))
                Utilities.Update([ScoreObjs, deniedObj, timerObj[1], WordScoreObj], True, [byebyeRect, ScoreGone])
                RectanglePack()
                Utilities.Sleep(0.5)
                check = False
                if timerObj[0]:
                    break
            elif o == '':
                deniedObj = Input.DispText('You Didn\'t Type Anything!', font, 16, RED, BROWNED, True, 'center', (xSize/2, 575))
                timerObj = Utilities.checkTimer(StartPoint, TimeLeft)
                ScoreObjs = Input.DispText('Score: ' + str(Score), font, 32, GREEN, BROWNED, True, 'center', (125, 625))
                WordScoreObj = Input.DispText('Word: %i' %0, font, 32, GREEN, BROWNED, True, 'center', (125, 590))
                Utilities.Update([ScoreObjs, deniedObj, timerObj[1], WordScoreObj], True, [byebyeRect, ScoreGone])
                RectanglePack()
                Utilities.Sleep(0.5)
                check = False
                if timerObj[0]:
                    break
            else:
                Inputs.append(o)
                check = True
        elif o == '':
            deniedObj = Input.DispText('You Didn\'t Type Anything!', font, 16, RED, BROWNED, True, 'center', (xSize/2, 575))
            timerObj = Utilities.checkTimer(StartPoint, TimeLeft)
            ScoreObjs = Input.DispText('Score: ' + str(Score), font, 32, GREEN, BROWNED, True, 'center', (125, 625))
            WordScoreObj = Input.DispText('Word: %i' %0, font, 32, GREEN, BROWNED, True, 'center', (125, 590))
            Utilities.Update([ScoreObjs, deniedObj, timerObj[1], WordScoreObj], True, Gone)
            RectanglePack()
            Utilities.Sleep(0.5)
            check = False
            if timerObj[0]:
                break
        else:
            Inputs.append(o)
            check = True
        if check:
            m = []
            p = Inputs[t]
            u = len(p)
            if u in (2, 1):
                deniedObj = Input.DispText('Word too short!', font, 16, RED, BROWNED, True, 'center', (xSize/2, 575))
                timerObj = Utilities.checkTimer(StartPoint, TimeLeft)
                ScoreObjs = Input.DispText('Score: ' + str(Score), font, 32, GREEN, BROWNED, True, 'center', (125, 625))
                WordScoreObj = Input.DispText('Word: %i' %0, font, 32, GREEN, BROWNED, True, 'center', (125, 590))
                Utilities.Update([ScoreObjs, deniedObj, timerObj[1], WordScoreObj], True, [byebyeRect, ScoreGone])
                RectanglePack()
                Utilities.Sleep(0.5)
                t = t + 1
                if timerObj[0]:
                    break
            elif p not in Words:
                deniedObj = Input.DispText('Invalid Word! -%i' %(len(Inputs[t]) - 2), font, 16, RED, BROWNED, True, 'center', (xSize/2, 575))
                timerObj = Utilities.checkTimer(StartPoint, TimeLeft)
                Score -= len(Inputs[t]) - 2
                if Score < 0:
                    Score = 0
                ScoreObjs = Input.DispText('Score: ' + str(Score), font, 32, GREEN, BROWNED, True, 'center', (125, 625))
                WordScoreObj = Input.DispText('Word: %i' %0, font, 32, GREEN, BROWNED, True, 'center', (125, 590))
                Utilities.Update([ScoreObjs, deniedObj, timerObj[1], WordScoreObj], True, [byebyeRect, ScoreGone])
                RectanglePack()
                Utilities.Sleep(0.5)
                if timerObj[0]:
                    break
                t = t + 1
            elif Check.preValid(p, lowered):
                for r in range(0, u):
                    m.append(Check.assignNums(p, lowered, r))
                if u < 9:
                    if Check.validity(m):
                        # If all is nice and dandy:
                        Score += GenScore(Inputs[t])
                        WordScore = GenScore(Inputs[t])
                        Valids.append(Inputs[t])
                        t = t + 1
                        BackPack()
                        WordCount += 1
                        Count2Obj = Input.DispText('Found: %i' %WordCount, font, 32, GREEN, BROWNED, True, 'center', (650, 625))
                        ScoreObjs = Input.DispText('Score: ' + str(Score), font, 32, GREEN, BROWNED, True, 'center', (125, 625))
                        WordScoreObj = Input.DispText('Word: %i' %WordScore, font, 32, GREEN, BROWNED, True, 'center', (125, 590))
                        Utilities.Update([Count2Obj, ScoreObjs, timerObj[1], WordScoreObj], True, [byebyeRect, ScoreGone])
                        RectanglePack()
                        Utilities.Update()
                    else:
                        deniedObj = Input.DispText('Word Not On Board! -%i' %(len(Inputs[t]) - 2), font, 16, RED, BROWNED, True, 'center', (xSize/2, 575))
                        timerObj = Utilities.checkTimer(StartPoint, TimeLeft)
                        Score -= len(Inputs[t]) - 2
                        if Score < 0:
                            Score = 0
                        ScoreObjs = Input.DispText('Score: ' + str(Score), font, 32, GREEN, BROWNED, True, 'center', (125, 625))
                        WordScoreObj = Input.DispText('Word: %i' %0, font, 32, GREEN, BROWNED, True, 'center', (125, 590))
                        Utilities.Update([ScoreObjs, deniedObj, timerObj[1], WordScoreObj], True, [byebyeRect, ScoreGone])
                        RectanglePack()
                        Utilities.Sleep(0.5)
                        if timerObj[0]:
                            break
                        t = t + 1
                elif u >= 9:
                    deniedObj = Input.DispText('Sorry, I don\'t take words above 8 letters, right now.', font, 16, RED, BROWNED, True, 'center', (xSize/2, 575))
                    timerObj = Utilities.checkTimer(StartPoint, TimeLeft)
                    ScoreObjs = Input.DispText('Score: ' + str(Score), font, 32, GREEN, BROWNED, True, 'center', (125, 625))
                    WordScoreObj = Input.DispText('Word: %i' %0, font, 32, GREEN, BROWNED, True, 'center', (125, 590))
                    Utilities.Update([ScoreObjs, deniedObj, timerObj[1], WordScoreObj], True, [byebyeRect, ScoreGone])
                    RectanglePack()
                    Utilities.Sleep(0.5)
                    t = t + 1
                    if timerObj[0]:
                        break
            else:
                deniedObj = Input.DispText('Word Not On Board! -%i' %(len(Inputs[t]) - 2), font, 16, RED, BROWNED, True, 'center', (xSize/2, 575))
                timerObj = Utilities.checkTimer(StartPoint, TimeLeft)
                Score -= len(Inputs[t]) -2
                if Score < 0:
                    Score = 0
                ScoreObjs = Input.DispText('Score: ' + str(Score), font, 32, GREEN, BROWNED, True, 'center', (125, 625))
                WordScoreObj = Input.DispText('Word: %i' %0, font, 32, GREEN, BROWNED, True, 'center', (125, 590))
                Utilities.Update([ScoreObjs, deniedObj, timerObj[1], WordScoreObj], True, [byebyeRect, ScoreGone])
                RectanglePack()
                Utilities.Sleep(0.5)
                t = t + 1
                if timerObj[0]:
                    break
        if check:
            Length = len(Inputs[t-1])
            if Length <= 6:
                if Inputs[t-1] in Valids:
                    MassUpdate = Input.DispText(Inputs[t-1], font, 32, BLUE, BROWNED, True, 'topleft', (x, y))
                else:
                    MassUpdate = Input.DispText(Inputs[t-1], font, 32, RED, BROWNED, True, 'topleft', (x, y))
            elif Length in (7, 8):
                if Inputs[t-1] in Valids:
                    MassUpdate = Input.DispText(Inputs[t-1], font, 22, BLUE, BROWNED, True, 'topleft', (x, y))
                else:
                    MassUpdate = Input.DispText(Inputs[t-1], font, 22, RED, BROWNED, True, 'topleft', (x, y))
            elif Length > 8:
                if Inputs[t-1] in Valids:
                    MassUpdate = Input.DispText(Inputs[t-1], font, 18, BLUE, BROWNED, True, 'topleft', (x, y))
                else:
                    MassUpdate = Input.DispText(Inputs[t-1], font, 18, RED, BROWNED, True, 'topleft', (x, y))
            y += 40
            if y > 500 and x == 25:
                Utilities.Update([], True, (600, 100, 100, 450))
                y = 100
                x = 600
            elif y > 500 and x == 600:
                Utilities.Update([], True, (25, 100, 100, 450))
                y = 100
                x = 25
            Utilities.Update([MassUpdate], True, byebyeRect)
        if timerObj[0]:
            break
    return [Score, Valids]

def GetScore(Score, Inputs, User, BgRect):
    'Displays the score, wordcount, and other things'
    m = 0
    r = User[1]
    word = ''
    Length = 0
    TimeObj = Input.DispText('Time\'s up!', font, 48, BLUE, YELLOWISH, True, 'center', (xSize/2, ySize/6 + 15))
    Utilities.Update([TimeObj], True, BgRect, YELLOWISH)
    Utilities.Sleep(1.5)
    Loading = 'Calculating score'
    for q in range(0, 5):
        LoadObj = Input.DispText(Loading, font, 16, RED, YELLOWISH, True, 'center', (xSize/2, ySize/5 + 25))
        Loading = ''.join([Loading, '.'])
        Utilities.Update([LoadObj])
        Utilities.Sleep(0.5)
    LineObj = Input.DispText('================', font, 16, RED, YELLOWISH, True, 'center', (xSize/2, ySize/5 + 25))
    score = ''.join(['Your score is: ', str(Score)])
    valids = ''.join(['Valid word count: ', str(len(Inputs))])
    ScoreObj = Input.DispText(score, font, 20, RED, YELLOWISH, True, 'center', (xSize/2, ySize/5 + 60))
    WordObj = Input.DispText(valids, font, 20, RED, YELLOWISH, True, 'center', (xSize/2, ySize/5 + 95))
    Utilities.Update([ScoreObj, WordObj, LineObj])
    r[User[0]].checkHigh(Score, xSize/2, ySize/5 + 130, [RED, YELLOWISH], 20)
    Utilities.Update()
    r[User[0]].checkBest(Inputs, xSize/2, ySize/5 + 165, [RED, YELLOWISH], 20)
    Utilities.Update()
    b = 0
    d = 'None'
    for a in Inputs:
        c = GenScore(a)
        if c > b:
            b = c
            d = a
    BestWordObj = Input.DispText('Best word this game: ' + d, font, 20, RED, YELLOWISH, True, 'center', (xSize/2, ySize/5 + 200))
    BestScoreObj = Input.DispText('Best word score this game: %i' %b, font, 20, RED, YELLOWISH, True, 'center', (xSize/2, ySize/5 + 235))
    Line2Obj = Input.DispText('================', font, 16, RED, YELLOWISH, True, 'center', (xSize/2, ySize/5 + 260))
    WaitObj = Input.DispText('Press Enter to Go Back', font, 32, BLUE, YELLOWISH, True, 'center', (xSize/2, ySize/5 + 290))
    Utilities.Update([Line2Obj, WaitObj, BestWordObj, BestScoreObj])
    Wait = [False, '']
    while Wait[0] != 'return':
        Wait = Input.Typed(Wait[1], Wait[0], 10, [File, [Pending, Pend], file2])
        WordTyped = ''.join(Wait[1])
        Utilities.Update()
    Utilities.Update([], True, (0, 75, xSize, ySize - 40))
    score = ''.join(['Last game score: ', str(Score)])
    valids = ''.join(['Last word count: ', str(len(Inputs))])
    ScoreObj1 = Input.DispText(score, font, 20, BLUE, BROWNED, True, 'center', (xSize/2, ySize/5 + 50))
    WordObj1 = Input.DispText(valids, font, 20, BLUE, BROWNED, True, 'center', (xSize/2, ySize/5 + 100))
    BestWordObj = Input.DispText('Best word last game: ' + d, font, 20, BLUE, BROWNED, True, 'center', (xSize/2, ySize/5 + 150))
    BestScoreObj = Input.DispText('Best word score last game: %i' %b, font, 20, BLUE, BROWNED, True, 'center', (xSize/2, ySize/5 + 200))
    Utilities.Update([ScoreObj1, WordObj1, BestWordObj, BestScoreObj])
