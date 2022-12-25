a = int(input("Enter a number: "))
space = 2 * a - 7
space2 = 2 * a - 7

for i in range(1, a + 1):
    j = a + 1 - i
    if j == a:
        print("* " * j)
    elif j <= 2:
        print("* " * j)
    else:
        if a % 2 != 0:

            print("*", " " * space, "*")
            space -= 2
        else:
            print("*", " " * space2, "*")
            space2 -= 2
