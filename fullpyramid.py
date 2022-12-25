print("\n            Full Pyramid            ")
a = int(input("Enter a base number for pyramid: "))


for i in range(1, a + 1):
    print(" " * (2 * a - i), end="")
    for j in range(1, i + 1):
        print(j, end=" ")

    print()
