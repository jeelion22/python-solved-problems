a = int(input())

for i in range(1, a + 1):
    print(" " * (a - i), end="")
    for j in range(1, i + 1):
        print(j, end=" ")
    print()
for k in range(1, a):
    print(" " * k, end="")
    for l in range(1, (a + 1 - k)):
        print(l, end=" ")
    print()
