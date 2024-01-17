import math

f = float(input("Enter n1 value :"))
s = float(input("Enter n2 value :"))
t = float(input("Enter n0 value :"))

result= math.asin(math.sqrt(((f)**2) - ((s)**2)) / (t))
h = math.degrees(result)
d = (math.sqrt((f)**2 - (s)**2) / (t))
print(" ans is : " + str(h))
print(" numerical aparture is = "+ str(d))
