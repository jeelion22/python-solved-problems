a = int(input())

for i in range(1, (a + 1)):
    for j in range(1, (2 * a)):
        if j == a:
            print("1", end=" ")
        else:
            if j <= a - i or j >= a + i:
                print("0", end=" ")
            else:
                print("1", end=" ")

    print()
