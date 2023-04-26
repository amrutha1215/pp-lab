import math
a,b,c=[int(x) for x in input ("enter sides:").split ()]
s=(a+b+c)/2
area=math.sqrt(s*(s-a)*(s-b)*(s-c))
print("area is",area)

