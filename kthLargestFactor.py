a = int(input())
b = int(input())

factors = []

for i in range(1, a + 1):
    for j in range(1, a + 1):
        if i * j == a:
            factors += [i]
print(factors[-b])
