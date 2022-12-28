def get_int_list(num_list):
    new_list = []
    for i in num_list:
        if i.isdigit():
            new_list.append(int(i))
    return new_list


num_list = input().split(",")

print(get_int_list(num_list))
