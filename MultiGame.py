#Import and initialize
import time, random, Input, Utilities, Check, Game
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

def GatherWords(Surface, Words, Timeout, clearRects, borderFunctions, Names):
    'Handles mulitplayer'
    def runBorders():
        for border in borderFunctions:
            border()
    t = 1
    for NameChange in Names:
        if len(NameChange) > 3:
            if NameChange[:3] in Names:
                Names[Names.index(NameChange)] = NameChange[:3] + str(t)
                t = t+1
            else:
                Names[Names.index(NameChange)] = NameChange[:3]
    x = 25
    y = 100
    WordCount = 0
    lowered = Utilities.Lower(Surface)
    check = True
    Score = 0
    Valids = []
    Inputs = []
    TimeLeft = len(Names) * Timeout
    Player3 = len(Names) == 3
    Player4 = len(Names) > 3
    t = 0
    clearRects[4].center = (xSize/2, 625)
    Utilities.Sleep(1)
    CountDown = Input.DispText('Ready', font, 48, RED, BROWNED, True, 'center', (xSize/2, 600))
    for g in range(255, 0, -2):
        CountDown[0].set_alpha(g)
        Utilities.Update([CountDown], True, clearRects[4])
    Utilities.Sleep(0.5)
    CountDown1 = Input.DispText('Set', font, 48, RED, BROWNED, True, 'center', (xSize/2, 600))
    for g in range(255, 0, -2):
        CountDown1[0].set_alpha(g)
        Utilities.Update([CountDown1], True, clearRects[4])
    Utilities.Sleep(0.5)
    CountDown2 = Input.DispText('Go!', font, 48, RED, BROWNED, True, 'center', (xSize/2, 600))
    Utilities.Update([CountDown2], True, clearRects[4])
    Utilities.Sleep(1)
    StartPoint = time.clock()
    Count1Obj = Input.DispText('Word: %i' %0, font, 32, GREEN, BROWNED, True, 'center', (125, 590))
    Count2Obj = Input.DispText('%s: ' %Names[0] + str(Score), font, 32, GREEN, BROWNED, True, 'center', (125, 625))
    Count3Obj = Input.DispText('Word: %i' %0, font, 32, GREEN, BROWNED, True, 'center', (650, 590))
    Count4Obj = Input.DispText('%s: ' %Names[1] + str(Score), font, 32, GREEN, BROWNED, True, 'center', (650, 625))
    if Player3 or Player4:
        Count5Obj = Input.DispText('Word: %i' %0, font, 32, GREEN, BROWNED, True, 'center', (125, 150))
        Count6Obj = Input.DispText('%s: ' %Names[2] + str(Score), font, 32, GREEN, BROWNED, True, 'center', (125, 185))
    if Player4:
        Count7Obj = Input.DispText('Word: %i' %0, font, 32, GREEN, BROWNED, True, 'center', (690, 150))
        Count8Obj = Input.DispText('%s: ' %Names[3] + str(Score), font, 32, GREEN, BROWNED, True, 'center', (690, 185))
    Utilities.Update([Count1Obj, Count2Obj, Count3Obj, Count4Obj], True, [clearRects[0],clearRects[1]])
    if Player3 or Player4:
        Utilities.Update([Count5Obj, Count6Obj], True, clearRects[2])
    if Player4:
        Utilities.Update([Count7Obj, Count8Obj], True, clearRects[3])
    runBorders()
    Utilities.Update()
    PlayerOn = 0
    # [Score, WordScore]
    PlayerM1 = [(125, 625), (125, 590)]
    PlayerM2 = [(650, 625), (650, 590)]
    if Player3 or Player4:
        PlayerM3 = [(125, 185), (125, 150)]
    if Player4:
        PlayerM4 = [(690, 185), (690, 150)]
    Player = PlayerM1
    Score1 = 0
    Score2 = 0
    if Player3 or Player4:
        Score3 = 0
    if Player4:
        Score4 = 0
    Valid1 = []
    Valid2 = []
    Name1 = Names[0]
    Name2 = Names[1]
    if Player3 or Player4:
        Valid3 = []
        Name3 = Names[2]
    if Player4:
        Valid4 = []
        Name4 = Names[3]
    while True:
        PlayerOn += 1
        if Player4:
            if PlayerOn == 5:
                PlayerOn = 1
        elif Player3 or Player4:
            if PlayerOn == 4:
                PlayerOn = 1
        else:
            if PlayerOn == 3:
                PlayerOn = 1
        if PlayerOn == 1:
            if Player4:
                Score4 = Score
                Valid4 = Valids
            elif Player3 or Player4:
                Score3 = Score
                Valid3 = Valids
            else:
                Score2 = Score
                Valid2 = Valids
            Name = Name1
            Score = 0
            Player = PlayerM1
            Score = Score1
            Pack = borderFunctions[0]
            Gone = clearRects[0]
            Valids = Valid1
        elif PlayerOn == 2:
            Name = Name2
            Score1 = Score
            Player = PlayerM2
            Score = 0
            Score = Score2
            Pack = borderFunctions[0]
            Gone = clearRects[1]
            Valid1 = Valids
            Valids = Valid2
        elif PlayerOn == 3:
            Name = Name3
            Score2 = Score
            Player = PlayerM3
            Score = Score3
            Pack = borderFunctions[0]
            Gone = clearRects[2]
            Valid2 = Valids
            Valids = Valid3
        elif PlayerOn == 4:
            Name = Name4
            Score3 = Score
            Player = PlayerM4
            Score = Score4
            Pack = borderFunctions[0]
            Gone = clearRects[3]
            Valid3 = Valids
            Valids = Valid4
        WordTyped = ''
        Guess = [False, WordTyped]
        DispHeaderObj = Input.DispText('Words:', font, 20, RED, BROWNED, True, 'center', (xSize/2, 550))
        Utilities.Update([DispHeaderObj])
        while Guess[0] != 'return':
            timerObj = Utilities.checkTimer(StartPoint, TimeLeft)
            DispGuessObj = Input.DispText(WordTyped, font, 16, RED, BROWNED, True, 'center', (xSize/2, 575))
            Guess = Input.Typed(Guess[1], Guess[0], 10, [File, [Pending, Pend], file2])
            WordTyped = ''.join(Guess[1])
            Utilities.Update([DispGuessObj, timerObj[1]], True, clearRects[4])
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
                ScoreObjs = Input.DispText(Name + ': ' + str(Score), font, 32, GREEN, BROWNED, True, 'center', Player[0])
                WordScoreObj = Input.DispText('Word: %i' %0, font, 32, GREEN, BROWNED, True, 'center', Player[1])
                Utilities.Update([ScoreObjs, deniedObj, timerObj[1], WordScoreObj], True, Gone)
                Pack()
                Utilities.Sleep(0.5)
                check = False
                if timerObj[0]:
                    break
            elif o == '':
                deniedObj = Input.DispText('You Didn\'t Type Anything!', font, 16, RED, BROWNED, True, 'center', (xSize/2, 575))
                timerObj = Utilities.checkTimer(StartPoint, TimeLeft)
                ScoreObjs = Input.DispText(Name + ': ' + str(Score), font, 32, GREEN, BROWNED, True, 'center', Player[0])
                WordScoreObj = Input.DispText('Word: %i' %0, font, 32, GREEN, BROWNED, True, 'center', Player[1])
                Utilities.Update([ScoreObjs, deniedObj, timerObj[1], WordScoreObj], True, Gone)
                Pack()
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
            ScoreObjs = Input.DispText(Name + ': ' + str(Score), font, 32, GREEN, BROWNED, True, 'center', Player[0])
            WordScoreObj = Input.DispText('Word: %i' %0, font, 32, GREEN, BROWNED, True, 'center', Player[1])
            Utilities.Update([ScoreObjs, deniedObj, timerObj[1], WordScoreObj], True, Gone)
            Pack()
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
                ScoreObjs = Input.DispText(Name + ': ' + str(Score), font, 32, GREEN, BROWNED, True, 'center', Player[0])
                WordScoreObj = Input.DispText('Word: %i' %0, font, 32, GREEN, BROWNED, True, 'center', Player[1])
                Utilities.Update([ScoreObjs, deniedObj, timerObj[1], WordScoreObj], True, Gone)
                Pack()
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
                ScoreObjs = Input.DispText(Name + ': ' + str(Score), font, 32, GREEN, BROWNED, True, 'center', Player[0])
                WordScoreObj = Input.DispText('Word: %i' %0, font, 32, GREEN, BROWNED, True, 'center', Player[1])
                Utilities.Update([ScoreObjs, deniedObj, timerObj[1], WordScoreObj], True, Gone)
                Pack()
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
                        Score += Game.GenScore(Inputs[t])
                        WordScore = Game.GenScore(Inputs[t])
                        Valids.append(Inputs[t])
                        t = t + 1
                        ScoreObjs = Input.DispText(Name + ': ' + str(Score), font, 32, GREEN, BROWNED, True, 'center', Player[0])
                        WordScoreObj = Input.DispText('Word: %i' %WordScore, font, 32, GREEN, BROWNED, True, 'center', Player[1])
                        Utilities.Update([ScoreObjs, timerObj[1], WordScoreObj], True, Gone)
                        Pack()
                        Utilities.Update()
                    else:
                        deniedObj = Input.DispText('Word Not On Board! -%i' %(len(Inputs[t]) - 2), font, 16, RED, BROWNED, True, 'center', (xSize/2, 575))
                        timerObj = Utilities.checkTimer(StartPoint, TimeLeft)
                        Score -= len(Inputs[t]) - 2
                        if Score < 0:
                            Score = 0
                        ScoreObjs = Input.DispText(Name + ': ' + str(Score), font, 32, GREEN, BROWNED, True, 'center', Player[0])
                        WordScoreObj = Input.DispText('Word: %i' %0, font, 32, GREEN, BROWNED, True, 'center', Player[1])
                        Utilities.Update([ScoreObjs, deniedObj, timerObj[1], WordScoreObj], True, Gone)
                        Pack()
                        Utilities.Sleep(0.5)
                        if timerObj[0]:
                            break
                        t = t + 1
                elif u >= 9:
                    deniedObj = Input.DispText('Sorry, I don\'t take words above 8 letters, right now.', font, 16, RED, BROWNED, True, 'center', (xSize/2, 575))
                    timerObj = Utilities.checkTimer(StartPoint, TimeLeft)
                    ScoreObjs = Input.DispText(Name + ': ' + str(Score), font, 32, GREEN, BROWNED, True, 'center', Player[0])
                    WordScoreObj = Input.DispText('Word: %i' %0, font, 32, GREEN, BROWNED, True, 'center', Player[1])
                    Utilities.Update([ScoreObjs, deniedObj, timerObj[1], WordScoreObj], True, Gone)
                    Pack()
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
                ScoreObjs = Input.DispText(Name + ': ' + str(Score), font, 32, GREEN, BROWNED, True, 'center', Player[0])
                WordScoreObj = Input.DispText('Word: %i' %0, font, 32, GREEN, BROWNED, True, 'center', Player[1])
                Utilities.Update([ScoreObjs, deniedObj, timerObj[1], WordScoreObj], True, Gone)
                Pack()
                Utilities.Sleep(0.5)
                t = t + 1
                if timerObj[0]:
                    break
        if timerObj[0]:
            break
    if Player3:
        return [[Score1, Score2, Score3], [Valid1, Valid2, Valid3]]
    elif Player4:
        return [[Score1, Score2, Score3, Score4], [Valid1, Valid2, Valid3, Valid4]]
    else:
        return [[Score1, Score2], [Valid1, Valid2]]

def GetScore(Score, Inputs, Names, BgRect):
    'Displays the score, wordcount, and other things'
    Player3 = len(Names) == 3
    Player4 = len(Names) > 3
    m = 0
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
    if Player3:
        if Score[0] > Score[1] and Score[0] > Score[2]:
            score = '%s wins with %i points!' %(Names[0], Score[0])
        elif Score[1] > Score[0] and Score[1] > Score[2]:
            score = '%s wins with %i points!' %(Names[1], Score[1])
        elif Score[2] > Score[0] and Score[2] > Score[1]:
            score = '%s wins with %i points!' %(Names[2], Score[2])
        elif Score[0] == Score[1]:
            score = '%s ties with %s for %i points!' %(Names[0], Names[1], Score[0])
        elif Score[0] == Score[2]:
            score = '%s ties with %s for %i points!' %(Names[0], Names[2], Score[0])
        elif Score[1] == Score[2]:
            score = '%s ties with %s for %i points!' %(Names[1], Names[2], Score[1])
        else:
            score = 'It\'s a tie! All players have %i points!' %Score[0]
        valids = 'Total word count: %i' %len(Inputs[0] + Inputs[1] + Inputs[2])
        ScoreObj = Input.DispText(score, font, 20, RED, YELLOWISH, True, 'center', (xSize/2, ySize/5 + 60))
        WordObj = Input.DispText(valids, font, 20, RED, YELLOWISH, True, 'center', (xSize/2, ySize/5 + 95))
        Utilities.Update([ScoreObj, WordObj, LineObj])
        valids1 = Input.DispText('%s\'s words: %i' %(Names[0], len(Inputs[0])), font, 20, RED, YELLOWISH, True, 'center', (xSize/2, ySize/5 + 125))
        Utilities.Update([valids1])
        valids2 = Input.DispText('%s\'s words: %i' %(Names[1], len(Inputs[1])), font, 20, RED, YELLOWISH, True, 'center', (xSize/2, ySize/5 + 148))
        Utilities.Update([valids2])
        valids3 = Input.DispText('%s\'s words: %i' %(Names[2], len(Inputs[2])), font, 20, RED, YELLOWISH, True, 'center', (xSize/2, ySize/5 + 170))
        Utilities.Update([valids3])
    elif Player4:
        if Score[0] > Score[1] and Score[0] > Score[2] and Score[0] > Score[3]:
            score = '%s wins with %i points!' %(Names[0], Score[0])
        elif Score[1] > Score[0] and Score[1] > Score[2] and Score[1] > Score[3]:
            score = '%s wins with %i points!' %(Names[1], Score[1])
        elif Score[2] > Score[0] and Score[2] > Score[1] and Score[2] > Score[3]:
            score = '%s wins with %i points!' %(Names[2], Score[2])
        elif Score[3] > Score[0] and Score[3] > Score[1] and Score[3] > Score[2]:
            score = '%s wins with %i points!' %(Names[3], Score[3])
        elif Score[0] == Score[1]:
            score = '%s ties with %s for %i points!' %(Names[0], Names[1], Score[0])
        elif Score[0] == Score[2]:
            score = '%s ties with %s for %i points!' %(Names[0], Names[2], Score[0])
        elif Score[0] == Score[3]:
            score = '%s ties with %s for %i points!' %(Names[0], Names[3], Score[0])
        elif Score[1] == Score[2]:
            score = '%s ties with %s for %i points!' %(Names[1], Names[2], Score[1])
        elif Score[1] == Score[3]:
            score = '%s ties with %s for %i points!' %(Names[1], Names[3], Score[1])
        elif Score[2] == Score[3]:
            score = '%s ties with %s for %i points!' %(Names[2], Names[3], Score[2])
        else:
            score = 'It\'s a tie! All players have %i points!' %Score[0]
        valids = 'Total word count: %i' %len(Inputs[0] + Inputs[1] + Inputs[2] + Inputs[3])
        ScoreObj = Input.DispText(score, font, 20, RED, YELLOWISH, True, 'center', (xSize/2, ySize/5 + 60))
        WordObj = Input.DispText(valids, font, 20, RED, YELLOWISH, True, 'center', (xSize/2, ySize/5 + 95))
        Utilities.Update([ScoreObj, WordObj, LineObj])
        valids1 = Input.DispText('%s\'s words: %i' %(Names[0], len(Inputs[0])), font, 20, RED, YELLOWISH, True, 'center', (xSize/2, ySize/5 + 120))
        Utilities.Update([valids1])
        valids2 = Input.DispText('%s\'s words: %i' %(Names[1], len(Inputs[1])), font, 20, RED, YELLOWISH, True, 'center', (xSize/2, ySize/5 + 138))
        Utilities.Update([valids2])
        valids3 = Input.DispText('%s\'s words: %i' %(Names[2], len(Inputs[2])), font, 20, RED, YELLOWISH, True, 'center', (xSize/2, ySize/5 + 158))
        Utilities.Update([valids3])
        valids4 = Input.DispText('%s\'s words: %i' %(Names[3], len(Inputs[3])), font, 20, RED, YELLOWISH, True, 'center', (xSize/2, ySize/5 + 175))
        Utilities.Update([valids4])
    else:
        if Score[0] > Score[1]:
            score = ''.join(['%s wins with ' %Names[0], str(Score[0]), ' points!'])
        elif Score[0] < Score[1]:
            score = ''.join(['%s wins with ' %Names[1], str(Score[1]), ' points!'])
        else:
            score = ''.join(['It\'s a tie! Both players have ', str(Score[0]), ' points!'])
        valids = ''.join(['Total word count: ', str(len(Inputs[0] + Inputs[1]))])
        ScoreObj = Input.DispText(score, font, 20, RED, YELLOWISH, True, 'center', (xSize/2, ySize/5 + 60))
        WordObj = Input.DispText(valids, font, 20, RED, YELLOWISH, True, 'center', (xSize/2, ySize/5 + 95))
        Utilities.Update([ScoreObj, WordObj, LineObj])
        valids1 = Input.DispText('%s\'s words: %i' %(Names[0], len(Inputs[0])), font, 20, RED, YELLOWISH, True, 'center', (xSize/2, ySize/5 + 130))
        Utilities.Update([valids1])
        valids2 = Input.DispText('%s\'s words: %i' %(Names[1], len(Inputs[1])), font, 20, RED, YELLOWISH, True, 'center', (xSize/2, ySize/5 + 165))
        Utilities.Update([valids2])
    b = 0
    e = 'Neither'
    d = 'None'
    for a in Inputs:
        for a1 in a:
            c = Game.GenScore(a1)
            if c > b:
                b = c
                d = a1
                if a == Inputs[0]:
                    e = Names[0]
                elif a == Inputs[1]:
                    e = Names[1]
                elif a == Inputs[2]:
                    e = Names[2]
                elif a == Inputs[3]:
                    e = Names[3]
    BestWordObj = Input.DispText('Best word this game by %s: %s' %(e,d), font, 20, RED, YELLOWISH, True, 'center', (xSize/2, ySize/5 + 200))
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
    if Player3:
        score = 'Last game score: %i - %i - %i' %(Score[0],Score[1],Score[2])
        valids = ''.join(['Last word count: ', str(len(Inputs[0] + Inputs[1] + Inputs[2]))])
    elif Player4:
        score = 'Last game score: %i - %i - %i - %i' %(Score[0],Score[1],Score[2],Score[3])
        valids = ''.join(['Last word count: ', str(len(Inputs[0] + Inputs[1] + Inputs[2] + Inputs[3]))])
    else:
        score = 'Last game score: %i - %i' %(Score[0],Score[1])
        valids = ''.join(['Last word count: ', str(len(Inputs[0] + Inputs[1]))])
    ScoreObj1 = Input.DispText(score, font, 20, BLUE, BROWNED, True, 'center', (xSize/2, ySize/5 + 50))
    WordObj1 = Input.DispText(valids, font, 20, BLUE, BROWNED, True, 'center', (xSize/2, ySize/5 + 100))
    BestWordObj = Input.DispText('Best word last game: ' + d, font, 20, BLUE, BROWNED, True, 'center', (xSize/2, ySize/5 + 150))
    BestScoreObj = Input.DispText('Best word score last game: %i' %b, font, 20, BLUE, BROWNED, True, 'center', (xSize/2, ySize/5 + 200))
    Utilities.Update([ScoreObj1, WordObj1, BestWordObj, BestScoreObj])
