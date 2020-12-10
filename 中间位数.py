#求数列中间位
def median(date1, date2, date3):
    data = 0
    if date1 > date2 :
        data = date1
        date1 = date2
        date2 = data
        data = 0
    if date1 > date3 :
        data = date1
        date1 = date3
        date3 = data
        data = 0
    if date2 > date3 :
        data = date2
        date2 = date3
        date3 = data
        data = 0
    print(date2, end = ' ')




median(14, 146, 155)
median(150, 54, 146)
median(2347, 964, 1537)
median(195, 236, 189)
median(101, 1080, 94)
median(496, 73, 66)
median(840, 11, 9)
median(385, 3, 8)
median(102, 309, 9)
median(483, 326, 335)
median(9, 11, 62)
median(60, 65, 143)
median(60, 550, 644)
median(106, 107, 89)
median(664, 662, 609)
median(4, 74, 73)
median(45, 33, 28)
median(49, 75, 6)
median(1685, 708, 1884)
median(22, 727, 724)
median(76, 86, 446)
median(683, 1207, 1436)
median(984, 1822, 1829)
median(839, 851, 861)
median(267, 357, 322)
