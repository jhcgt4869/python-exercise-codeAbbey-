'''数字1,2,3 1*2+3的值相加的结果
11 9 1   11*9+1 =100  结果为1
14 90 232
111 15 111
answer:
1 16 21
'''
def digits(date,date1,date2):
    sum = (date * date1) + date2
    print(sod(sum),end = ' ')


def sod(sum):
    s = 0
    while (sum != 0):
        s += sum % 10
        sum = sum // 10
    return s


digits(207, 267, 191)
digits(207, 88, 46)
digits(67, 188, 8)
digits(395, 200, 3)
digits(194, 238, 21)
digits(365, 274, 48)
digits(312, 229, 36)
digits(398, 106, 126)
digits(372, 50, 121)
digits(189, 224, 35)
digits(115, 76, 13)
digits(98, 228, 71)
digits(188, 272, 196)
digits(203, 269, 130)
