a = input()
b = ""
for i in a:

    if ord(i) in range(65, 91):
        b += "_" + i.lower()

    else:
        b += i
print(b[1:])
