x = int(input("Enter a value x: "))
y = int(input("Enter a value y: "))
first = math.sqrt(math.cos(2*y)+math.sin(4*y) + math.sqrt(math.exp(x) + math.exp(-x)))
second = math.pow(((math.pow(math.e,(-x))) + math.pow(math.e,x)),3) * math.pow((math.sin(4*y) + math.cos(2*y) - 2), 2)
H = fist/second
print ("Answer: ", "H={0:2f}".format(H))
