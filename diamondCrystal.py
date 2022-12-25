a = int(input())
b = 0
c = 2 * a - 2

for i in range(1, 2 * a + 1):
    if i <= a:
        print(" " * (a - i), end="")
        print("/" + " " * b + "\\", end="")
        b += 2
    else:
        print(" " * (i - a - 1), end="")
        print("\\" + " " * c + "/", end="")
        c -= 2
    print()
