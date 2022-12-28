def get_missing_int(num_list):
    list_1 = []
    list_2 = []

    for i in num_list:
        list_1.append(int(i))
    list_1.sort()
    for j in range(list_1[0], list_1[-1] + 1):
        list_2.append(j)

    missing_set = set(list_2) - set(list_1)
    missing_list = sorted(list(missing_set))
    return missing_list


num_list = input().split(" ")
print(get_missing_int(num_list))
