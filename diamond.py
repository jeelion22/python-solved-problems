a = int(input())


for i in range(1, 2 * a):

    for j in range(1, 2 * a):
        if i == a:
            print("0", end=" ")

        elif i <= a - 1:
            if j <= a - i or j >= a + i:
                print(".", end=" ")
            else:
                print("0", end=" ")

        elif i >= a + 1:
            if j <= i - a or j > 3 * a - i - 1:
                print(".", end=" ")
            else:
                print("0", end=" ")
    print()
