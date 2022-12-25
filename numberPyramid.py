a = int(input())
b = ""
for i in range(1, a + 1):
    print(" " * (a - i), end="")
    if i == 1:
        print(i, end="")
    else:
        for j in range(1, i + 1):
            b += str(j)
        c = b[::-1]

        print(c + b[1:], end="")
        b = ""
    print()
