a = int(input())
b = 1
d = []
large = None
while b <= a:
    c = int(input())
    d += [c]
    if c == max(d):
        large = c
    print(large)
    b += 1
