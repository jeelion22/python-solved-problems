def get_num_list(str_list):
    num_list = []
    for i in str_list:
        num_list.append(int(i))
    return num_list


def get_unique_elements(num_list):
    set_a = set(num_list)
    if len(num_list) > 1 and len(set_a) == 1:
        return True
    else:
        return sorted(list(set_a))


str_list = input().split(" ")
num_list = get_num_list(str_list)
print(get_unique_elements(num_list))
