a = int(input())
k = int(input())
c = 0
for i in range(a, 0, -1):
    if a % i == 0:
        c += 1
    if c == k:
        print(i)
        break
if k > c:
    print(1)
