a = input()
b = input()
c = 0

for i in a:
    if i == b[c]:
        c += 1
        if len(b) == c:
            break

if c == len(b):
    print("Yes")
else:
    print("No")
