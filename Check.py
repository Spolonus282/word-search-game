''' ============== Check ===============
*** Created by Sam Polonus
*** This module is free-to-use and edit.
*** Created on February 7, 2017.
*** No other sources were used.
'''

Positions = {'0':  [0,0], '1':  [1,0], '2':  [2,0], '3':  [3,0],
             '4':  [0,1], '5':  [1,1], '6':  [2,1], '7':  [3,1],
             '8':  [0,2], '9':  [1,2], '10': [2,2], '11': [3,2],
             '12': [0,3], '13': [1,3], '14': [2,3], '15': [3,3]}

'''overall idea:
    basically, what I want to do here is gather every single
    coordinate for the first letter and store them away. Then
    I will do the same for 2, 3, etc. and finally check for a
    correlation.'''

def preValid(Input, Surface):
    'Check that letters are on board'
    t = list(Input)
    for i in range(0,len(Input)):
        r = t[0]
        del t[0]
        if r in Surface:
            if r == max(Input):
                return True
        else:
            return False

def assignNums(Input, Surface, valueOn):
    'Assign coords'
    a = Input[valueOn]
    b = list(Surface)
    z = []
    while True:
        try:
            e = b.index(a)
            z.append(Positions['{0}'.format(e)])
            b[e] = '#'
        except ValueError:
            break
    p = Surface.count(Input[valueOn])
    return z

def validity(num):
    'Assure coords are adjacent'
    x = list(num)
    y = len(x)
    nums = x[0]
    nums1 = x[1]
    nums2 = x[2]
    if y > 3: nums3 = x[3]
    if y > 4: nums4 = x[4]
    if y > 5: nums5 = x[5]
    if y > 6: nums6 = x[6]
    if y > 7: nums7 = x[7]
    if y == 3:
        for b in nums:
            for c in nums1:
                for d in nums2:
                    if c[0] in (b[0], b[0] + 1, b[0] - 1) and c[1] in (b[1], b[1] + 1, b[1] - 1) and c != b:
                        if d[0] in (c[0], c[0] + 1, c[0] - 1) and d[1] in (c[1], c[1] + 1, c[1] - 1) and d != c and d != b:
                            return True
        return False
    elif y == 4:
        for b in nums:
            for c in nums1:
                for d in nums2:
                    for e in nums3:
                        if c[0] in (b[0], b[0] + 1, b[0] - 1) and c[1] in (b[1], b[1] + 1, b[1] - 1) and c != b:
                            if d[0] in (c[0], c[0] + 1, c[0] - 1) and d[1] in (c[1], c[1] + 1, c[1] - 1) and d != c and d != b:
                                if e[0] in (d[0], d[0] + 1, d[0] - 1) and e[1] in (d[1], d[1] + 1, d[1] - 1) and e != d and e != b and e != c:
                                    return True
        return False
    elif y == 5:
        for b in nums:
            for c in nums1:
                for d in nums2:
                    for e in nums3:
                        for f in nums4:
                            if c[0] in (b[0], b[0] + 1, b[0] - 1) and c[1] in (b[1], b[1] + 1, b[1] - 1) and c != b:
                                if d[0] in (c[0], c[0] + 1, c[0] - 1) and d[1] in (c[1], c[1] + 1, c[1] - 1) and d != c and d != b:
                                    if e[0] in (d[0], d[0] + 1, d[0] - 1) and e[1] in (d[1], d[1] + 1, d[1] - 1) and e != d and e != b and e != c:
                                        if f[0] in (e[0], e[0] + 1, e[0] - 1) and f[1] in (e[1], e[1] + 1, e[1] - 1) and f != e and f != b and f != c and f != d:
                                            return True
        return False
    elif y == 6:
        for b in nums:
            for c in nums1:
                for d in nums2:
                    for e in nums3:
                        for f in nums4:
                            for g in nums5:
                                if c[0] in (b[0], b[0] + 1, b[0] - 1) and c[1] in (b[1], b[1] + 1, b[1] - 1) and c != b:
                                    if d[0] in (c[0], c[0] + 1, c[0] - 1) and d[1] in (c[1], c[1] + 1, c[1] - 1) and d != c and d != b:
                                        if e[0] in (d[0], d[0] + 1, d[0] - 1) and e[1] in (d[1], d[1] + 1, d[1] - 1) and e != d and e != b and e != c:
                                            if f[0] in (e[0], e[0] + 1, e[0] - 1) and f[1] in (e[1], e[1] + 1, e[1] - 1) and f != e and f != b and f != c and f != d:
                                                if g[0] in (f[0], f[0] + 1, f[0] - 1) and g[1] in (f[1], f[1] + 1, f[1] - 1) and g != e and g != b and g != c and g != d and g != f:
                                                    return True
        return False
    elif y == 7:
        for b in nums:
            for c in nums1:
                for d in nums2:
                    for e in nums3:
                        for f in nums4:
                            for g in nums5:
                                for h in nums6:
                                    if c[0] in (b[0], b[0] + 1, b[0] - 1) and c[1] in (b[1], b[1] + 1, b[1] - 1) and c != b:
                                        if d[0] in (c[0], c[0] + 1, c[0] - 1) and d[1] in (c[1], c[1] + 1, c[1] - 1) and d != c and d != b:
                                            if e[0] in (d[0], d[0] + 1, d[0] - 1) and e[1] in (d[1], d[1] + 1, d[1] - 1) and e != d and e != b and e != c:
                                                if f[0] in (e[0], e[0] + 1, e[0] - 1) and f[1] in (e[1], e[1] + 1, e[1] - 1) and f != e and f != b and f != c and f != d:
                                                    if g[0] in (f[0], f[0] + 1, f[0] - 1) and g[1] in (f[1], f[1] + 1, f[1] - 1) and g != e and g != b and g != c and g != d and g != f:
                                                        if h[0] in (g[0], g[0] + 1, g[0] - 1) and h[1] in (g[1], g[1] + 1, g[1] - 1) and h != e and h != b and h != c and h != d and h != f and h != g:
                                                            return True
        return False
    else:
        for b in nums:
            for c in nums1:
                for d in nums2:
                    for e in nums3:
                        for f in nums4:
                            for g in nums5:
                                for h in nums6:
                                    for i in nums7:
                                        if c[0] in (b[0], b[0] + 1, b[0] - 1) and c[1] in (b[1], b[1] + 1, b[1] - 1) and c != b:
                                            if d[0] in (c[0], c[0] + 1, c[0] - 1) and d[1] in (c[1], c[1] + 1, c[1] - 1) and d != c and d != b:
                                                if e[0] in (d[0], d[0] + 1, d[0] - 1) and e[1] in (d[1], d[1] + 1, d[1] - 1) and e != d and e != b and e != c:
                                                    if f[0] in (e[0], e[0] + 1, e[0] - 1) and f[1] in (e[1], e[1] + 1, e[1] - 1) and f != e and f != b and f != c and f != d:
                                                        if g[0] in (f[0], f[0] + 1, f[0] - 1) and g[1] in (f[1], f[1] + 1, f[1] - 1) and g != e and g != b and g != c and g != d and g != f:
                                                            if h[0] in (g[0], g[0] + 1, g[0] - 1) and h[1] in (g[1], g[1] + 1, g[1] - 1) and h != e and h != b and h != c and h != d and h != f and h != g:
                                                                if i[0] in (h[0], h[0] + 1, h[0] - 1) and i[1] in (h[1], h[1] + 1, h[1] - 1) and i != e and i != b and i != c and i != d and i != f and i != g and i != h:
                                                                    return True
        return False
    return False
