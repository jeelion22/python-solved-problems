a = int(input())

for i in range(1, a + 1):
    print(" " * (a - i), end="")
    for j in range(1, i + 1):
        print("*", end=" ")
    print()
for k in range(1, a):
    print(" " * k, end="")
    if (a + 1 - k) <= 3:
        for l in range(1, a + 1 - k):
            print("*", end=" ")
    else:
        for l in range(1, a + 1 - k):
            if l == 1 or l == (a - k):
                print("*", end=" ")
            else:
                print(" ", end=" ")
    print()
