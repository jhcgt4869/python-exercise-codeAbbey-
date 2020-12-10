def olf (x1, y1, x2, y2):
    for i in range(10):
        for j in range(10):
            if x1 * i + j == y1 and x2 * i + j == y2:
                print('(%d %d)'%(i,j))


olf(0, 0, 1, 1)
olf(1, 0, 0, 1)