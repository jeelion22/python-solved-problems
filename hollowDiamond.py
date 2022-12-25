a = int(input())
b = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

d = 0
e = a - 1

for i in range(1, 2 * a):
    d += 1
    if d >= a:
        e -= 1

    for j in range(1, 2 * a + 1):
        if i == 1 or i == 2 * a - 1:
            if j == a:
                print(b[0], end="")
                d -= 1

            else:
                print(" ", end="")
        elif i <= a:

            if j == a + 1 - i or j == a - 1 + i:
                print(b[d], end="")

            else:
                print(" ", end="")
        elif i > a and i < 2 * a - 1:

            if j == i - a + 1 or j == 3 * a - i - 1:
                print(b[e], end="")

            else:
                print(" ", end="")

    print()
