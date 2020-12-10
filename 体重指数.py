#计算bmi求体重
def bmi (weight , height):
    bmi1 = weight / (height ** 2)
    if bmi1 >= 30 :
        print('obese' ,end = ' ')
    elif bmi1 >= 25 :
        print('over' , end = ' ')
    elif bmi1 >= 18.5 :
        print( 'normal' , end = ' ')
    elif bmi1 < 18.5 :
        print('under' , end = ' ')


bmi(74, 1.97)
bmi(120, 2.28)
bmi(106, 3.10)
bmi(65, 1.45)
bmi(53, 1.88)
bmi(113, 1.82)
bmi(72, 1.39)
bmi(46, 1.75)
bmi(100, 2.50)
bmi(87, 2.33)
bmi(56, 1.72)
bmi(77, 1.79)
bmi(59, 1.38)
bmi(110, 2.91)
bmi(113, 3.21)
bmi(94, 2.17)
bmi(66, 1.54)
bmi(104, 2.63)
bmi(95, 2.60)
bmi(114, 1.86)
bmi(61, 1.36)
bmi(97, 1.86)
bmi(104, 1.80)
bmi(106, 2.06)
bmi(120, 2.39)
bmi(99, 2.49)
bmi(97, 2.46)
bmi(95, 1.62)
bmi(118, 2.17)
bmi(42, 1.11)
bmi(84, 1.70)
