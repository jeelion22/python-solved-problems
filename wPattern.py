a = int(input())

print("* " * (2 * a - 1))

for i in range(0, a - 1):
    print(" " * i, end=" ")
    print("* " * (a - 1 - i), end="")
    print(" " * (2 * i), end="")
    print("* " * (a - 1 - i), end=" ")

    print()
