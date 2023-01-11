def arithmetic_arranger(list_1):
    new_list = []
    for item in list_1:
        item_list = item.split(" ")
        new_list.append((item_list))

    string_1 = ""
    string_2 = ""
    string_3 = ""
    count = 0

    for num in new_list:
        if count == 0:
            if len(num[0]) <= 4:
                string_a = " " * (4 - len(num[0])) + num[0]
                string_b = num[1] + " " + num[2]
                string_1 += string_a
                string_2 += string_b
        else:
            if len(num[0]) <= 4:
                string_a = " " * 4 + " " * (2 * ((4 - len(num[0])) + 1)) + num[0]
                string_1 += string_a
                string_b = " " * 4 + num[1] + " " * (4 - len(num[2])) + num[2]
                string_2 += string_b
        count += 1
    print(string_1)
    print(string_2)


list_1 = ["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]
arithmetic_arranger(list_1)
