number = int(input('number = '))

i = number // 100
j = number % 10
z = (number - (i * 100) - j ) // 10
newnumber = j * 100 + z * 10 + i
print('number = ', newnumber)