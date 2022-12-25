num1 = int(input("First number: "))
num2 = int(input("Last number: "))

primeList = []
sum = 0

for num in range(num1, num2 + 1):
    if num1 <= 1:
        continue
    elif num1 > 1:
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            primeList += [num]
            sum += num

# if num1 == 2:
#    primeList = [2] + primeList

print("\nPRIME Number List: ", primeList)
print("SUM of PRIME Numbers: ", sum, "\n")
