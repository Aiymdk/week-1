a = int(input('Enter first number: '))
b = int(input('Enter second number: '))
c = int(input('Enter third number: '))
if a>b:
    if a>c:
        d=a
else:
    if b>c:
        d=b
    else:
        d=c
if a<b:
    if a<c:
        z=a
else:
    if b<c:
        z=b
    else:
        z=c
print('Biggest number is: ' + str(d))
print('Smallest number is: ' + str(z))
