# Finds the number has maximum value in a given list

number_list = input(
    "\nEnter a list of numbers by starting '['and closing ']' brackets: "
)

largest = None

for number in number_list[1:-2:3]:
    print(number_list[1:-2:1])
    num = float(number)
    if largest is None or num > largest:
        largest = num

print(f"Largest number in the list is {largest}")
