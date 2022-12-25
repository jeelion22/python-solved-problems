a = int(input())

for i in range(a):
    print(" " * i, end="")
    print("* " * (a - i))

for i in range(2, a + 1):
    print(" " * (a - i), end="")
    print("* " * i)
