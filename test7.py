str_list = "Anjali25 is python4 Expert".split()
num_list = []
newStr = ""
print(str_list)
for item in str_list:
    if item.isdigit():
        num_list.append(int(item))
    else:

        for char in item:
            if char.isdigit():
                newStr += char
            else:
                newStr += " "
new_list = newStr.split(" ")

for i in new_list:
    if i.isdigit():
        num_list.append(int(i))


sum_of_list = sum(num_list)
avg_nums = sum_of_list / len(num_list)
print(sum_of_list)
print(round(avg_nums, 2))
