import random, time, Players, Check
from Players import Players
File = open('Words.txt','a+')

def AddPlayer(Users):
    NewUser = input("Type your name: ")
    Users[NewUser] = Players(NewUser)
    print("Hello, " + NewUser + ". Let's begin!")
    return [NewUser, Users]
    
def GetScore(Score, Inputs, User):
    q = 0
    m = 0
    r = User[1]
    word = ''
    Length = 0
    print("Time's Up!")
    time.sleep(1.5)
    print("Calculating score", end = "")
    print(".", end = "")
    while q < 5:
        time.sleep(.5)
        print(".", end = "")
        q = q + 1
    print()
    print("Your score is: " + str(Score) + "")
    print("Valid Word Count: " + str(len(Inputs)) + "")
    r[User[0]].checkBest(Inputs)
    r[User[0]].checkHigh(Score)


def ChooseDie(UsedOnes):
    A = ['A','E','A','N','E','G']
    B = ['A','H','S','P','C','O']
    C = ['A','S','P','F','F','K']
    D = ['O','B','J','O','A','B']
    E = ['I','O','T','M','U','C']
    F = ['R','Y','V','D','E','L']
    G = ['L','R','E','I','X','D']
    H = ['E','I','U','N','E','S']
    I = ['W','N','G','E','E','H']
    J = ['L','N','H','N','R','Z']
    K = ['T','S','T','I','Y','D']
    L = ['O','W','T','O','A','T']
    M = ['E','R','T','T','Y','L']
    N = ['T','O','E','S','S','I']
    O = ['T','E','R','W','H','V']
    P = ['N','U','I','H','M','Q']
    Letters = [A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P]
    x = random.choice(Letters)
    while x in UsedOnes:
        x = random.choice(Letters)
    y = random.choice(x)
    z = [x,y]
    return z

def CalcBoard():
    p = 0
    Gen = []
    Die1 = ChooseDie(Gen)
    Gen.append(Die1[0])
    Die2 = ChooseDie(Gen)
    Gen.append(Die2[0])
    Die3 = ChooseDie(Gen)
    Gen.append(Die3[0])
    Die4 = ChooseDie(Gen)
    Gen.append(Die4[0])
    Die5 = ChooseDie(Gen)
    Gen.append(Die5[0])
    Die6 = ChooseDie(Gen)
    Gen.append(Die6[0])
    Die7 = ChooseDie(Gen)
    Gen.append(Die7[0])
    Die8 = ChooseDie(Gen)
    Gen.append(Die8[0])
    Die9 = ChooseDie(Gen)
    Gen.append(Die9[0])
    Die10 = ChooseDie(Gen)
    Gen.append(Die10[0])
    Die11 = ChooseDie(Gen)
    Gen.append(Die11[0])
    Die12 = ChooseDie(Gen)
    Gen.append(Die12[0])
    Die13 = ChooseDie(Gen)
    Gen.append(Die13[0])
    Die14 = ChooseDie(Gen)
    Gen.append(Die14[0])
    Die15 = ChooseDie(Gen)
    Gen.append(Die15[0])
    Die16 = ChooseDie(Gen)
    Gen.append(Die16[0])
    GenChar = [Die1[1],Die2[1],Die3[1],Die4[1],Die5[1],Die6[1],Die7[1],Die8[1],
               Die9[1],Die10[1],Die11[1],Die12[1],Die13[1],Die14[1],Die15[1],Die16[1]]
    while p < 16:
        if p == 3 or p == 7 or p == 11 or p == 15:
            print(''+ GenChar[p] +'')
        else:
            print(''+ GenChar[p] +'  ', end = '')
        p = p + 1
    return GenChar

def Lower(letters):
    b = []
    for a in letters:
        b.append(a.lower())
    return b

def AddWords():
    Confirm = True
    add = "y"
    print("Add words to Dictionary?")
    while add == "y":
        add = input("y or n ")
        if add == "n":
            break
        print("Input word")
        added = input()
        if len(str(added)) < 3:
            print("Word too short!")
            Confirm = False
        else:
            File.write(',' + added)
            Confirm = True
        if Confirm:
            print("Added!")
        time.sleep(1.5)
        print("Would you like to add another?")

def TryAgain():
    GoOn = False
    Play = True
    PlayAgain = "y"
    while not GoOn:
        print("Play again?")
        PlayAgain = input("y or n ")
        if PlayAgain == "y":
            Play = True
            GoOn = True
        elif PlayAgain == "n":
            Play = False
            GoOn = True
        else:
            print("Answer is not y or n")
            GoOn = False
    return Play

def Main(Surface, Word):
    lowered = Lower(Surface)
    check = True
    Score = 0
    Inputs = []
    TimeLeft = 180
    StartPoint = time.clock()
    t = 0
    while TimeLeft > 0:
        o = input()
        if t > 0:
            if o in Inputs:
                print("You said that already!")
                check = False
            else:
                Inputs.append(o)
                check = True
        else:
            Inputs.append(o)
            check = True
        if check:
            m = []
            p = Inputs[t]
            u = len(p)
            if p not in Word:
                print("Invalid Word!")
                del Inputs[t]
            elif Check.preValid(p, lowered):
                for r in range(0, u):
                    m.append(Check.assignNums(p, lowered, r))
                if u == 3:
                    if Check.validity(m[0],m[1],m[2],'x',0,0,0,0,0):
                        t = t + 1
                        Score = Score + 1
                    else:
                        print("Invalid Word!")
                        del Inputs[t]
                elif u == 4:
                    if Check.validity(m[0],m[1],m[2],m[3],'x',0,0,0,0):
                        t = t + 1
                        Score = Score + 1
                    else:
                        print("Invalid Word!")
                        del Inputs[t]
                elif u == 5:
                    if Check.validity(m[0],m[1],m[2],m[3],m[4],'x',0,0,0):
                        t = t + 1
                        Score = Score + 2
                    else:
                        print("Invalid Word!")
                        del Inputs[t]
                elif u == 6:
                    if Check.validity(m[0],m[1],m[2],m[3],m[4],m[5],'x',0,0):
                        t = t + 1
                        Score = Score + 3
                    else:
                        print("Invalid Word!")
                        del Inputs[t]
                elif u == 7:
                    if Check.validity(m[0],m[1],m[2],m[3],m[4],m[5],m[6],'x',0):
                        t = t + 1
                        Score = Score + 5
                    else:
                        print("Invalid Word!")
                        del Inputs[t]
                elif u == 8:
                    if Check.validity(m[0],m[1],m[2],m[3],m[4],m[5],m[6],m[7],'x'):
                        t = t + 1
                        Score = Score + 11
                    else:
                        print("Invalid Word!")
                        del Inputs[t]
                elif u >= 9:
                    print('Sorry, I don\'t take words above 8 letters, right now.')
                    del Inputs[t]
            else:
                print("Invalid Word!")
                del Inputs[t]
        TimeLeft = TimeLeft - (time.clock() - StartPoint)
    return [Score, Inputs]

Repeat = True
print("Welcome to Word Search! Ready to play?")
Player = AddPlayer({})
while Repeat:
    File.seek(0)
    Worded = File.read().split(',')
    Board = CalcBoard()
    Send = Main(Board, Worded)
    GetScore(Send[0], Send[1], Player)
    AddWords()
    Repeat = TryAgain()
File.close()
