a = int(input())

for i in range(1, (2 * a + 2)):

    for j in range(1, a + 1):
        if j == 1 or j == a:
            print("*", end=" ")
        elif i == 1 or i == (2 * a + 1) // 2 + 1 or i == 2 * a + 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")

    print()
