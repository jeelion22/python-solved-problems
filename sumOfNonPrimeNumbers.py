a = int(input())
b = 1
e = []

while b <= a:
    c = int(input())
    b += 1
    if c > 1:
        for j in range(2, c):
            if c % j == 0:
                e += [c]
                break


print(sum(e))
