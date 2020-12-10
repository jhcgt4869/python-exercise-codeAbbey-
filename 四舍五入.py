def rounding(ret,rer):
    data = ret / rer
    if data > 0 :
        print(round(data),end = ' ')
    elif data < 0:
        data_1 = ret // rer
        data_2 = data - data_1
        if data_2 >0.5:
            print((data_1+1),end = ' ')
        elif data_2 <= 0.5:
            print(data_1,end = ' ')
    else :
        print(0)


rounding(1028193, 3051573)
rounding(9213674, 258)
rounding(17247, 1896)
rounding(1529265, 90)
rounding(19093, 1100)
rounding(12239, 1190)
rounding(6333392, 296)
rounding(-3826305, -707876)
rounding(15143, 1974)
rounding(1612825, 238)
rounding(5331544, 789)
rounding(16789, 1524)
rounding(7545729, 530)
rounding(7897232, 589)
rounding(5795501, 532)
rounding(-4379191, -4532902)
rounding(5489653, 639)
