print("\n\t\t\tArmstrong Numbers")
a = int(input("First number: "))
b = int(input("Last number: "))
armstrongNumber = []

for i in range(a, b + 1):
    d = str(i)
    c = []
    for j in d:

        e = int(j) ** len(d)
        c += [e]
        f = sum(c)

    if f == i:
        armstrongNumber += [f]
print(f"Armstrong number(s) between {a} and {b} is/are: ", end=" ")
print(armstrongNumber, sep=",")

print("\n")
