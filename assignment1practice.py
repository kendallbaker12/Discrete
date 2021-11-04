a = 100
b = 2


if(a < 0 and b > 0):
    q = int(a/b) - 1
    r = a - (b*q)

elif(a > 0 and b < 0):
    q = int(a/b)
    r = a - (b*q)

elif(a > 0 and b > 0):
    q = int(a/b)
    r = a - (b*q)

elif(a < 0 and b < 0):
    q = int((a+b)/b)
    r = a - (b*q)


print(q)
print(r)