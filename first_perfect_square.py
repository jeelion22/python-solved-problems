first_number = int(input())
second_number = int(input())

for i in range(first_number, second_number + 1):
    first_perfect_square = None
    sqrt_value = i**0.5
    if sqrt_value % 2 == 0:
        first_perfect_square = i
        print(first_perfect_square)
        break

if first_perfect_square == None:
    print("No Perfect Square")
