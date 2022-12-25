a = int(input())
sp = 2 * a - 7
for i in range(a + 1):
    j = a + 1 - i
    if j <= 3 or j == a + 1:
        for k in range(1, j):
            print(k, end=" ")
        print()

    else:
        for k in range(1, j + 1):
            if k == 1 or k == j - 1:
                print(k, " " * sp, end=" ")
                sp -= 1
        print()
