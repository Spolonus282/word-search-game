def TryAgain():
    BgRect = Rect(0, ySize/6 - 25, xSize, ySize/5 + 225)
    DISPSURF.fill(YELLOWISH, BgRect)
    GoOn = False
    Play = True
    PlayAgain = "y"
    WhiteRect = Rect(0, ySize/2 + 1, xSize, 20)
    while not GoOn:
        PAObj = Input.DispText('Play Again?', font, 20, BLUE, YELLOWISH, True, 'center', BgRect.center)
        Update([PAObj])
        PlayAgain = 'y or n: '
        idk = [False, PlayAgain]
        WhiteRect.center = (xSize/2, BgRect.centery + 25)
        while idk[0] != 'return':
            AgainObj = Input.DispText(PlayAgain, font, 16, BLUE, YELLOWISH, True, 'center', (xSize/2, BgRect.centery + 25))
            idk = Input.Typed(idk[1], idk[0], 9, [File, file2])
            PlayAgain = ''.join(idk[1])
            Update([AgainObj], True, WhiteRect, YELLOWISH)
        ynTemp = idk[1].lstrip('yorn ')
        yn = ynTemp.lstrip(': ')
        if yn == "y":
            Play = True
            GoOn = True
        elif yn == "n":
            Play = False
            GoOn = True
        else:
            ErrorObj = Input.DispText('Answer is not \'y\' or \'n\'.', font, 16, RED, YELLOWISH, True, 'center', (xSize/2, BgRect.centery + 25))
            Update([ErrorObj], True, WhiteRect, YELLOWISH)
            GoOn = False
            Sleep(0.5)
    Sleep(0.5)
    return Play
