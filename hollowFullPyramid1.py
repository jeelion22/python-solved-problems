a = int(input())
b = a - 1

for i in range(1, a + 1):
    print(" " * b, end="")
    b -= 1

    if i <= 2 or i == a:
        for j in range(1, i + 1):
            print("*", end=" ")

    else:
        for j in range(1, i + 1):
            if j == 1 or j == i:
                print("*", end=" ")
            else:
                print(" ", end=" ")

    print()
