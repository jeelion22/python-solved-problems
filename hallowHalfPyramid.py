a = int(input())
sp = 1
for i in range(1, a + 1):
    if i <= 2:
        for j in range(1, i + 1):
            print(j, end=" ")
        print()
    elif i == a:
        for j in range(1, i + 1):
            print(j, end=" ")
        print()
    else:
        for j in range(1, i + 1):
            if j == 1 or j == i:
                print(j, " " * sp, end=" ")
                sp += 1
        print()
