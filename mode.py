a = [1, 1, 1, 1, 1, 2, 2, 3, 4]
a.sort()
b = a.copy()
k = 0
l = 0
c = []


for i in a:
    for j in a:
        if j == i:
            a.remove(j)

for i in a:
    count = 0
    for j in b:
        if j == i:
            count += 1
            k = j
            l = count
    c += [(k, l)]

print(c)

largest = None
num = None

for (x, y) in c:
    if largest is None or y > largest:
        largest = y
        if largest:
            k = x

print(k, largest)
