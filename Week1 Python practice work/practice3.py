a = int(input('1 number:'))
b = int(input('2 number:'))
c = int(input('3 number:'))
if (a < b and a < c):
    print('MinNumber:',a)
elif (b < a and b < c):
    print('MinNumber:',b)
else:
    print('MinNumber:',c)
