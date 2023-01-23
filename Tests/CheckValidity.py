Inputs = ['apes']
Final = False
t = 0
m = Inputs[t]
Surface = ['a','b','c','d','e','f','g','h','i','j','k','l','m','o','p','a']
Score = 0
while not Final:
    if m[0] in Surface and m[1] in Surface and m[2] in Surface:
        e = Surface.index(m[0])
        m1 = Surface.count(m[0])
        m2 = Surface.count(m[1])

        # Bottom right corner
        if e == 15 and m[1] in (Surface[14], Surface[11], Surface[10]):
            if m[1] == Surface[14] and m[2] in (Surface[13], Surface[9], Surface[10], Surface[11]):
                Score = Score + 1
                t = t + 1
                Final = True
            elif m[1] == Surface[11] and m[2] in (Surface[7], Surface[6], Surface[14], Surface[10]):
                Score = Score + 1
                t = t + 1
                Final = True
            elif m[1] == Surface[10] and m[2] in (Surface[13], Surface[9], Surface[5], Surface[6], Surface[7], Surface[11], Surface[14]):
                Score = Score + 1
                t = t + 1
                Final = True
            elif m1 > 1:
                if m2 > 1:
                    Surface[Surface.index(m[1])] = '#'
                else:
                    Surface[e] = '#'
            else:
                print("Invalid Word!")
                del Inputs[t]
                Final = True

        # Bottom left corner
        elif e == 12 and m[1] in (Surface[13], Surface[8], Surface[9]):
            if m[1] == Surface[13] and m[2] in (Surface[10], Surface[14], Surface[8], Surface[9]):
                Score = Score + 1
                t = t + 1
                Final = True
            elif m[1] == Surface[8] and m[2] in (Surface[4], Surface[5], Surface[13], Surface[9]):
                Score = Score + 1
                t = t + 1
                Final = True
            elif m[1] == Surface[9] and m[2] in (Surface[14], Surface[10], Surface[6], Surface[5], Surface[4], Surface[13], Surface[8]):
                Score = Score + 1
                t = t + 1
                Final = True
            elif m1 > 1:
                if m2 > 1:
                    Surface[Surface.index(m[1])] = '#'
                else:
                    Surface[e] = '#'
            else:
                print("Invalid Word!")
                del Inputs[t]
                Final = True
                    
        # Lower right side
        elif e == 11 and m[1] in (Surface[15], Surface[14], Surface[10], Surface[6], Surface[7]):
            if m[1] == Surface[15] and m[2] in (Surface[10], Surface[14]):
                Score = Score + 1
                t = t + 1
                Final = True
            elif m[1] == Surface[14] and m[2] in (Surface[10], Surface[15], Surface[13], Surface[9]):
                Score = Score + 1
                t = t + 1
                Final = True
            elif m[1] == Surface[10] and m[2] in (Surface[15], Surface[14], Surface[13], Surface[9], Surface[5], Surface[6], Surface[7]):
                Score = Score + 1
                t = t + 1
                Final = True
            elif m[1] == Surface[6] and m[2] in (Surface[10], Surface[9], Surface[5], Surface[1], Surface[2], Surface[3], Surface[7]):
                Score = Score + 1
                t = t + 1
                Final = True
            elif m[1] == Surface[7] and m[2] in (Surface[10], Surface[6], Surface[2], Surface[3]):
                Score = Score + 1
                t = t + 1
                Final = True
            elif m1 > 1:
                if m2 > 1:
                    Surface[Surface.index(m[1])] = '#'
                else:
                    Surface[e] = '#'
            else:
                print("Invalid Word!")
                del Inputs[t]
                Final = True
                
        # Lower left side
        elif e == 8 and m[1] in (Surface[12], Surface[13], Surface[9], Surface[5], Surface[4]):
            if m[1] == Surface[12] and m[2] in (Surface[13], Surface[9]):
                Score = Score + 1
                t = t + 1
                Final = True
            elif m[1] == Surface[13] and m[2] in (Surface[12], Surface[9], Surface[14], Surface[10]):
                Score = Score + 1
                t = t + 1
                Final = True
            elif m[1] == Surface[9] and m[2] in (Surface[12], Surface[13], Surface[14], Surface[10], Surface[6], Surface[5], Surface[4]):
                Score = Score + 1
                t = t + 1
                Final = True
            elif m[1] == Surface[5] and m[2] in (Surface[9], Surface[10], Surface[6], Surface[2], Surface[1], Surface[0], Surface[4]):
                Score = Score + 1
                t = t + 1
                Final = True
            elif m[1] == Surface[4] and m[2] in (Surface[9], Surface[5], Surface[1], Surface[0]):
                Score = Score + 1
                t = t + 1
                Final = True
            elif m1 > 1:
                if m2 > 1:
                    Surface[Surface.index(m[1])] = '#'
                else:
                    Surface[e] = '#'
            else:
                print("Invalid Word!")
                del Inputs[t]
                Final = True
            
        # Upper right side
        elif e == 7 and m[1] in (Surface[11], Surface[10], Surface[6], Surface[2], Surface[3]):
            if m[1] == Surface[3] and m[2] in (Surface[6], Surface[2]):
                Score = Score + 1
                t = t + 1
                Final = True
            elif m[1] == Surface[2] and m[2] in (Surface[3], Surface[6], Surface[5], Surface[1]):
                Score = Score + 1
                t = t + 1
                Final = True
            elif m[1] == Surface[6] and m[2] in (Surface[3], Surface[2], Surface[1], Surface[5], Surface[9], Surface[10], Surface[11]):
                Score = Score + 1
                t = t + 1
                Final = True
            elif m[1] == Surface[10] and m[2] in (Surface[11], Surface[15], Surface[14], Surface[13], Surface[9], Surface[5], Surface[6]):
                Score = Score + 1
                t = t + 1
                Final = True
            elif m[1] == Surface[11] and m[2] in (Surface[10], Surface[6], Surface[14], Surface[15]):
                Score = Score + 1
                t = t + 1
                Final = True
            elif m1 > 1:
                if m2 > 1:
                    Surface[Surface.index(m[1])] = '#'
                else:
                    Surface[e] = '#'
            else:
                print("Invalid Word!")
                del Inputs[t]
                Final = True

        # Upper left side
        elif e == 4 and m[1] in (Surface[8], Surface[9], Surface[5], Surface[1], Surface[0]):
            if m[1] == Surface[0] and m[2] in (Surface[1], Surface[5]):
                Score = Score + 1
                t = t + 1
                Final = True
            elif m[1] == Surface[1] and m[2] in (Surface[0], Surface[5], Surface[6], Surface[2]):
                Score = Score + 1
                t = t + 1
                Final = True
            elif m[1] == Surface[5] and m[2] in (Surface[0], Surface[1], Surface[2], Surface[6], Surface[10], Surface[9], Surface[8]):
                Score = Score + 1
                t = t + 1
                Final = True
            elif m[1] == Surface[9] and m[2] in (Surface[8], Surface[12], Surface[13], Surface[14], Surface[10], Surface[6], Surface[5]):
                Score = Score + 1
                t = t + 1
                Final = True
            elif m[1] == Surface[8] and m[2] in (Surface[12], Surface[13], Surface[9], Surface[5]):
                Score = Score + 1
                t = t + 1
                Final = True
            elif m1 > 1:
                if m2 > 1:
                    Surface[Surface.index(m[1])] = '#'
                else:
                    Surface[e] = '#'
            else:
                print("Invalid Word!")
                del Inputs[t]
                Final = True

        # Top right corner
        elif e == 3 and m[1] in (Surface[7], Surface[6], Surface[2]):
            if m[1] == Surface[7] and m[2] in (Surface[2], Surface[6], Surface[10], Surface[11]):
                Score = Score + 1
                t = t + 1
                Final = True
            elif m[1] == Surface[2] and m[2] in (Surface[1], Surface[5], Surface[6], Surface[7]):
                Score = Score + 1
                t = t + 1
                Final = True
            elif m[1] == Surface[6] and m[2] in (Surface[2], Surface[1], Surface[5], Surface[9], Surface[10], Surface[11], Surface[7]):
                Score = Score + 1
                t = t + 1
                Final = True
            elif m1 > 1:
                if m2 > 1:
                    Surface[Surface.index(m[1])] = '#'
                else:
                    Surface[e] = '#'
            else:
                print("Invalid Word!")
                del Inputs[t]
                Final = True

        # Top left corner
        elif e == 0 and m[1] in (Surface[4], Surface[5], Surface[1]):
            if m[1] == Surface[4] and m[2] in (Surface[1], Surface[5], Surface[9], Surface[8]):
                Score = Score + 1
                t = t + 1
                Final = True
            elif m[1] == Surface[1] and m[2] in (Surface[2], Surface[6], Surface[5], Surface[4]):
                Score = Score + 1
                t = t + 1
                Final = True
            elif m[1] == Surface[5] and m[2] in (Surface[1], Surface[2],Surface[6], Surface[10], Surface[9], Surface[8], Surface[4]):
                Score = Score + 1
                t = t + 1
                Final = True
            elif m1 > 1:
                if m2 > 1:
                    Surface[Surface.index(m[1])] = '#'
                else:
                    Surface[e] = '#'
            else:
                print("Invalid Word!")
                del Inputs[t]
                Final = True

        # Top left
        elif e == 1 and m[1] in (Surface[0], Surface[4], Surface[5], Surface[6], Surface[2]):
            if m[1] == Surface[0] and m[2] in (Surface[4], Surface[5]):
                Score = Score + 1
                t = t + 1
                Final = True
            elif m[1] == Surface[4] and m[2] in (Surface[0], Surface[5], Surface[9], Surface[8]):
                Score = Score + 1
                t = t + 1
                Final = True
            elif m[1] == Surface[5] and m[2] in (Surface[0], Surface[4], Surface[8], Surface[9], Surface[10], Surface[6], Surface[2]):
                Score = Score + 1
                t = t + 1
                Final = True
            elif m[1] == Surface[6] and m[2] in (Surface[2], Surface[3], Surface[7], Surface[11], Surface[10], Surface[9], Surface[5]):
                Score = Score + 1
                t = t + 1
                Final = True
            elif m[1] == Surface[2] and m[2] in (Surface[3], Surface[7], Surface[6], Surface[5]):
                Score = Score + 1
                t = t + 1
                Final = True
            elif m1 > 1:
                if m2 > 1:
                    Surface[Surface.index(m[1])] = '#'
                else:
                    Surface[e] = '#'
            else:
                print("Invalid Word!")
                del Inputs[t]
                Final = True

        # Top right
        elif e == 2 and m[1] in (Surface[1], Surface[5], Surface[6], Surface[7], Surface[3]):
            if m[1] == Surface[1] and m[2] in (Surface[0], Surface[4], Surface[5], Surface[6]):
                Score = Score + 1
                t = t + 1
                Final = True
            elif m[1] == Surface[5] and m[2] in (Surface[1], Surface[0], Surface[4], Surface[8], Surface[9], Surface[10], Surface[6]):
                Score = Score + 1
                t = t + 1
                Final = True
            elif m[1] == Surface[6] and m[2] in (Surface[1], Surface[5], Surface[9], Surface[10], Surface[11], Surface[7], Surface[3]):
                Score = Score + 1
                t = t + 1
                Final = True
            elif m[1] == Surface[7] and m[2] in (Surface[3], Surface[6], Surface[10], Surface[11]):
                Score = Score + 1
                t = t + 1
                Final = True
            elif m[1] == Surface[3] and m[2] in (Surface[7], Surface[6]):
                Score = Score + 1
                t = t + 1
                Final = True
            elif m1 > 1:
                if m2 > 1:
                    Surface[Surface.index(m[1])] = '#'
                else:
                    Surface[e] = '#'
            else:
                print("Invalid Word!")
                del Inputs[t]
                Final = True

        # Bottom left
        elif e == 13 and m[1] in (Surface[14], Surface[10], Surface[9], Surface[8], Surface[12]):
            if m[1] == Surface[12] and m[2] in (Surface[8], Surface[9]):
                Score = Score + 1
                t = t + 1
                Final = True
            elif m[1] == Surface[8] and m[2] in (Surface[4], Surface[5], Surface[9], Surface[12]):
                Score = Score + 1
                t = t + 1
                Final = True
            elif m[1] == Surface[9] and m[2] in (Surface[14], Surface[10], Surface[6], Surface[5], Surface[4], Surface[8], Surface[12]):
                Score = Score + 1
                t = t + 1
                Final = True
            elif m[1] == Surface[10] and m[2] in (Surface[9], Surface[14], Surface[15], Surface[11], Surface[7], Surface[6], Surface[5]):
                Score = Score + 1
                t = t + 1
                Final = True
            elif m[1] == Surface[14] and m[2] in (Surface[15], Surface[11], Surface[10], Surface[9]):
                Score = Score + 1
                t = t + 1
                Final = True
            elif m1 > 1:
                if m2 > 1:
                    Surface[Surface.index(m[1])] = '#'
                else:
                    Surface[e] = '#'
            else:
                print("Invalid Word!")
                del Inputs[t]
                Final = True
                                 
        # Bottom right
        elif e == 14 and m[1] in (Surface[15], Surface[11], Surface[10], Surface[9], Surface[13]):
            if m[1] == Surface[13] and m[2] in (Surface[12], Surface[8], Surface[9], Surface[10]):
                Score = Score + 1
                t = t + 1
                Final = True
            elif m[1] == Surface[9] and m[2] in (Surface[13], Surface[12], Surface[8], Surface[4], Surface[5], Surface[6], Surface[10]):
                Score = Score + 1
                t = t + 1
                Final = True
            elif m[1] == Surface[10] and m[2] in (Surface[15], Surface[11], Surface[7], Surface[6], Surface[5], Surface[9], Surface[13]):
                Score = Score + 1
                t = t + 1
                Final = True
            elif m[1] == Surface[11] and m[2] in (Surface[15] or m[2] == Surface[10] or m[2] == Surface[6] or m[2] == Surface[7]):
                Score = Score + 1
                t = t + 1
                Final = True
            elif m[1] == Surface[15] and m[2] in (Surface[11] or m[2] == Surface[10]):
                Score = Score + 1
                t = t + 1
                Final = True
            elif m1 > 1:
                if m2 > 1:
                    Surface[Surface.index(m[1])] = '#'
                else:
                    Surface[e] = '#'
            else:
                print("Invalid Word!")
                del Inputs[t]
                Final = True

        # Upper left
        elif e == 5 and m[1] in (Surface[0], Surface[1], Surface[2], Surface[6], Surface[10], Surface[9], Surface[8], Surface[4]):
            if m[1] == Surface[0] and m[2] in (Surface[1], Surface[4]):
                Score = Score + 1
                t = t + 1
                Final = True
            elif m[1] == Surface[1] and m[2] in (Surface[0], Surface[4], Surface[2], Surface[6]):
                Score = Score + 1
                t = t + 1
                Final = True
            elif m[1] == Surface[2] and m[2] in (Surface[1], Surface[6], Surface[7], Surface[3]):
                Score = Score + 1
                t = t + 1
                Final = True
            elif m[1] == Surface[6] and m[2] in (Surface[1], Surface[2], Surface[3], Surface[7], Surface[11], Surface[10], Surface[9]):
                Score = Score + 1
                t = t + 1
                Final = True
            elif m[1] == Surface[10] and  m[2] in (Surface[6], Surface[7], Surface[11], Surface[15], Surface[14], Surface[13], Surface[9]):
                Score = Score + 1
                t = t + 1
                Final = True
            elif m[1] == Surface[9] and m[2] in (Surface[6], Surface[10], Surface[14], Surface[13], Surface[12], Surface[8], Surface[4]):
                Score = Score + 1
                t = t + 1
                Final = True
            elif m[1] == Surface[8] and m[2] in (Surface[12], Surface[13], Surface[9], Surface[4]):
                Score = Score + 1
                t = t + 1
                Final = True
            elif m[1] == Surface[4] and m[2] in (Surface[0], Surface[1], Surface[9], Surface[8]):
                Score = Score + 1
                t = t + 1
                Final = True
            elif m1 > 1:
                if m2 > 1:
                    Surface[Surface.index(m[1])] = '#'
                else:
                    Surface[e] = '#'
            else:
                print("Invalid Word!")
                del Inputs[t]
                Final = True

        #Upper right
        elif e == 6 and m[1] in (Surface[1], Surface[2], Surface[3], Surface[7], Surface[11], Surface[10], Surface[9], Surface[5]):
            if m[1] == Surface[3] and m[2] in (Surface[2], Surface[7]):
                Score = Score + 1
                t = t + 1
                Final = True
            elif m[1] == Surface[2] and m[2] in (Surface[1], Surface[5], Surface[3], Surface[7]):
                Score = Score + 1
                t = t + 1
                Final = True
            elif m[1] == Surface[1] and m[2] in (Surface[0], Surface[4], Surface[5], Surface[2]):
                Score = Score + 1
                t = t + 1
                Final = True
            elif m[1] == Surface[5] and m[2] in (Surface[2], Surface[1], Surface[0], Surface[4], Surface[8], Surface[9], Surface[10]):
                Score = Score + 1
                t = t + 1
                Final = True
            elif m[1] == Surface[9] and  m[2] in (Surface[5], Surface[4], Surface[8], Surface[12], Surface[13], Surface[14], Surface[10]):
                Score = Score + 1
                t = t + 1
                Final = True
            elif m[1] == Surface[10] and m[2] in (Surface[7], Surface[11], Surface[15], Surface[14], Surface[13], Surface[9], Surface[5]):
                Score = Score + 1
                t = t + 1
                Final = True
            elif m[1] == Surface[11] and m[2] in (Surface[7], Surface[10], Surface[14], Surface[15]):
                Score = Score + 1
                t = t + 1
                Final = True
            elif m[1] == Surface[7] and m[2] in (Surface[2], Surface[3], Surface[10], Surface[11]):
                Score = Score + 1
                t = t + 1
                Final = True
            elif m1 > 1:
                if m2 > 1:
                    Surface[Surface.index(m[1])] = '#'
                else:
                    Surface[e] = '#'
            else:
                print("Invalid Word!")
                del Inputs[t]
                Final = True

        # Lower left
        elif e == 9 and m[1] in (Surface[4], Surface[5], Surface[6], Surface[10], Surface[14], Surface[13], Surface[12], Surface[8]):
            if m[1] == Surface[12] and m[2] in (Surface[8], Surface[13]):
                Score = Score + 1
                t = t + 1
                Final = True
            elif m[1] == Surface[13] and m[2] in (Surface[8], Surface[12], Surface[10], Surface[14]):
                Score = Score + 1
                t = t + 1
                Final = True
            elif m[1] == Surface[14] and m[2] in (Surface[13], Surface[10], Surface[11], Surface[15]):
                Score = Score + 1
                t = t + 1
                Final = True
            elif m[1] == Surface[10] and m[2] in (Surface[5], Surface[6], Surface[7], Surface[11], Surface[15], Surface[14], Surface[13]):
                Score = Score + 1
                t = t + 1
                Final = True
            elif m[1] == Surface[6] and  m[2] in (Surface[5], Surface[1], Surface[2], Surface[3], Surface[7], Surface[11], Surface[10]):
                Score = Score + 1
                t = t + 1
                Final = True
            elif m[1] == Surface[5] and m[2] in (Surface[8], Surface[4], Surface[0], Surface[1], Surface[2], Surface[6], Surface[10]):
                Score = Score + 1
                t = t + 1
                Final = True
            elif m[1] == Surface[4] and m[2] in (Surface[0], Surface[1], Surface[8], Surface[5]):
                Score = Score + 1
                t = t + 1
                Final = True
            elif m[1] == Surface[8] and m[2] in (Surface[5], Surface[4], Surface[12], Surface[13]):
                Score = Score + 1
                t = t + 1
                Final = True
            elif m1 > 1:
                if m2 > 1:
                    Surface[Surface.index(m[1])] = '#'
                else:
                    Surface[e] = '#'
            else:
                print("Invalid Word!")
                del Inputs[t]
                Final = True

        # Lower right
        elif e == 10 and m[1] in (Surface[15], Surface[11], Surface[7], Surface[6], Surface[5], Surface[9], Surface[13], Surface[14]):
            if m[1] == Surface[15] and m[2] in (Surface[11], Surface[14]):
                Score = Score + 1
                t = t + 1
                Final = True
            elif m[1] == Surface[14] and m[2] in (Surface[13], Surface[9], Surface[15], Surface[11]):
                Score = Score + 1
                t = t + 1
                Final = True
            elif m[1] == Surface[13] and m[2] in (Surface[8], Surface[9], Surface[12], Surface[14]):
                Score = Score + 1
                t = t + 1
                Final = True
            elif m[1] == Surface[9] and m[2] in (Surface[14], Surface[13], Surface[12], Surface[8], Surface[4], Surface[5], Surface[6]):
                Score = Score + 1
                t = t + 1
                Final = True
            elif m[1] == Surface[5] and  m[2] in (Surface[9], Surface[8], Surface[4], Surface[0], Surface[1], Surface[2], Surface[6]):
                Score = Score + 1
                t = t + 1
                Final = True
            elif m[1] == Surface[6] and m[2] in (Surface[9], Surface[5], Surface[1], Surface[2], Surface[3], Surface[7], Surface[11]):
                Score = Score + 1
                t = t + 1
                Final = True
            elif m[1] == Surface[7] and m[2] in (Surface[3], Surface[2], Surface[6], Surface[11]):
                Score = Score + 1
                t = t + 1
                Final = True
            elif m[1] == Surface[11] and m[2] in (Surface[6], Surface[7], Surface[14], Surface[15]):
                Score = Score + 1
                t = t + 1
                Final = True
            elif m1 > 1:
                if m2 > 1:
                    Surface[Surface.index(m[1])] = '#'
                else:
                    Surface[e] = '#'
            else:
                print("Invalid Word!")
                del Inputs[t]
                Final = True
    else:
        print("Invalid Word!")
        del Inputs[t]
        Final = True
