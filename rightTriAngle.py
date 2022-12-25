a = int(input())
c = []

for i in range(1, a + 1):
    d = ""
    for j in range(1, i + 1):
        d += str(j)
    c += [d]


for j in c:
    if j == c[0]:
        print(j)
    else:
        print(j + (j[::-1])[1:])
