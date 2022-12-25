import math

a = int(input())
b = int(input())
c = int(input())

x = (-b + math.sqrt(b**2 - (4 * a * c))) / (2 * a)
y = (-b - math.sqrt(b**2 - (4 * a * c))) / (2 * a)
print(round(x, 2))
print(round(y, 2))
