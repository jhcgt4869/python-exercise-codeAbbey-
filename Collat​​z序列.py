def collatz(a):
    sum = 0
    while True:
        if a % 2 == 0:
            a /= 2
            sum += 1
        else:
            a = a * 3 + 1
            sum += 1
        if a == 1:
            break
    print( sum ,end = ' ')


date = [388, 4902, 485, 36, 14652,
        407, 316, 9261, 321, 329, 307, 73,
        461, 40, 33, 31451, 353, 3981, 3213]
for i in date:
    collatz(i)

