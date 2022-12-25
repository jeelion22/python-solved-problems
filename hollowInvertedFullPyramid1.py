a = int(input())
b = 0

for i in range(a + 1):
    print(" " * b, end="")
    b += 1

    if (a - i) <= 2 or (a - i) == a:
        for j in range(1, (a - i + 1)):
            print("*", end=" ")

    else:
        for j in range(1, (a - i + 1)):
            if j == 1 or j == (a - i):
                print("*", end=" ")
            else:
                print(" ", end=" ")
    print()
