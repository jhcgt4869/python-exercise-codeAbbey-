#以date1位起始位，date2位步长date3为个数求数列之和
def arithmetic(date1,date2,date3):
    sum = 0
    for i in range(date3):
        sum += (date1 + (i * date2))
    print(sum,end = ' ')

arithmetic(4, 14, 73)
arithmetic(11, 2, 82)
arithmetic(10, 10, 33)
arithmetic(18, 18, 15)
arithmetic(3, 1, 98)
arithmetic(27, 10, 61)
arithmetic(12, 8, 70)
arithmetic(4, 0, 99)