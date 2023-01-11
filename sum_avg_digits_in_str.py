str_a = input()
num_list = []

for item in str_a:
    if item.isdigit():
        for digit in item:
            num_list.append(int(digit))
sum_of_list = sum(num_list)
avg_nums = sum_of_list / len(num_list)
print(sum_of_list)
print(round(avg_nums, 2))
