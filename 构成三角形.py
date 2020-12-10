#判定三个数是否构成三角形
def sides(a, b, c):
    if a + b >c and a + c > b and b + c > a :
        print(1 ,end = ' ')
    else:
        print(0 ,end = ' ')



sides(219, 519, 161)
sides(1380, 2346, 753)
sides(906, 1869, 644)
sides(143, 190, 408)
sides(435, 266, 959)
sides(1249, 334, 642)
sides(138, 226, 505)
sides(3102, 1472, 874)
sides(155, 300, 480)
sides(893, 2365, 1624)
sides(171, 314, 398)
sides(1604, 784, 686)
sides(317, 239, 482)
sides(601, 327, 1473)
sides(964, 1162, 1014)
sides(165, 401, 205)
sides(801, 264, 384)
sides(556, 958, 550)
sides(712, 273, 369)
sides(912, 1636, 2043)
sides(1639, 397, 727)
sides(1715, 1037, 691)
sides(874, 583, 394)
sides(2488, 1092, 704)
