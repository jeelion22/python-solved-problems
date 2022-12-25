a = int(input())
b = 1

while b <= a:
    c = int(input())
    b += 1
    if c % 5 == 0:
        break
    else:
        print(c)
