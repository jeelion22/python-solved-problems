a = int(input())

for i in range(1, a + 1):
    print("* " * i, end=" ")
    print()
for j in range(1, a):
    print("* " * (a - j), end=" ")
    print()
