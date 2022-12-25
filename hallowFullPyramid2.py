a = int(input())

for i in range(1, a + 1):
    print(" " * (a - i), end="")
    if i <= 2 or i == a:
        for j in range(1, i + 1):
            print(j, end=" ")
    else:
        for j in range(1, i + 1):
            if j == 1 or j == i:
                print(j, end=" ")
            else:
                print(" ", end=" ")
    print()
