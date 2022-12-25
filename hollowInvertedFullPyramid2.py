a = int(input())

for i in range(a + 1):
    print(" " * i, end="")

    if (a - i) <= 2 or (a - i) == a:
        for j in range(1, (a + 1 - i)):
            print(j, end=" ")
    else:
        for j in range(1, (a + 1 - 1)):
            if j == 1 or j == (a - i):
                print(j, end=" ")
            else:
                print(" ", end=" ")
    print()
