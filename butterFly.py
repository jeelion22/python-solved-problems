a = int(input())
b = 0
c = 0
d = 0

for i in range(1, 2 * a + 1):

    if i <= a + 1:
        for j in range(1, 2 * a + 1):
            if j <= i or j >= (2 * a + 1 - i):
                print("*", end=" ")
            else:
                print(" ", end=" ")

        print()

    else:
        for j in range(1, 2 * a + 1):
            b += 1

            if j < (2 * a - b - c) or (j >= a + 2 + d):
                print("*", end=" ")
            else:
                print(" ", end=" ")
        b = 0
        b += 1
        c += 2
        d += 1

        print()
