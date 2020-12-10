'''
n = 14
net = 1
for i in range(1,n+1):
    net *= i

for j in range(1,n+1):
    det = 10 ** j
    #print(det)
    if net % det != 0:
        break
print (net,j-1)
n = 75
for i in range(n):
    det = n // 5
print(det)

net = 1
        for i in range(1,n+1):
            net *= i
        for j in range(1,n+1):
            det = 10 ** j
            if net % det != 0:
                break
        return(j-1)
'''