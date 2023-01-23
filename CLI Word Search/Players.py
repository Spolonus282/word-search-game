class Players:
    'The players that are on this save file'
    totPlayers = 0

    def __init__(self, name):
        bestWord = ''
        bestScore = 0
        high = 0
        Players.totPlayers += 1
        self.name = name
        self.bestWord = bestWord
        self.high = high
        self.bestScore = bestScore

    def checkHigh(self, score):
        if score > self.high:
            self.high = score
            print('New high score for ' + self.name + ': ' + str(self.high) + '!')
        else:
            print('The high score remains at: ' + str(self.high) + '.')

    def checkBest(self, words):
        grats = False
        for t in range(0,len(words)):
            wordScore = 0
            wordScore += len(words[t])
            if "q" in words[t]:
                wordScore += 1
            if "z" in words[t]:
                wordScore += 1
            if "x" in words[t]:
                wordScore += 1
            if wordScore > self.bestScore:
                self.bestScore = wordScore
                self.bestWord = words[t]
                grats = True
        if grats:
            print('New best word for ' + self.name + ': ' + self.bestWord + '!')
        else:
            print('The best word remains: ' + self.bestWord + '.')

    def dispStats(self):
        print('Name: ' + self.name +
              '\nHigh Score: ' + str(self.high) +
              '\nBest Word: ' + self.bestWord +
              '\nTotal Players: ' + str(Players.totPlayers))
