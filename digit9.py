a = int(input())

for i in range(1, (2 * a)):

    if i == 1 or i == ((2 * a) // 2) or i == (2 * a - 1):
        for j in range(1, a + 1):
            print("*", end=" ")

    elif i > 1 and i <= ((2 * a - 1) // 2):
        for j in range(1, a + 1):
            if j == 1 or j == a:
                print("*", end=" ")
            else:
                print(" ", end=" ")
    else:
        for j in range(1, a + 1):
            if j == a:
                print("*", end=" ")
            else:
                print(" ", end=" ")

    print()
