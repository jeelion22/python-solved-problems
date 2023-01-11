inp_1 = input().split(" ")
inp_2 = input().split(" ")
inp_3 = input().split(" ")


def get_set(inp_1):
    set_1 = set()
    for i in inp_1:
        set_1.add(int(i))
    return set_1


def get_common_element_in_sets(set_1, set_2, set_3):
    com_set_1 = set_1 & set_2
    com_set_2 = set_1 & set_3
    com_set = com_set_1 & com_set_2
    com_set = list(com_set)
    return sorted(com_set)


set_1 = get_set(inp_1)
set_2 = get_set(inp_2)
set_3 = get_set(inp_3)

print(get_common_element_in_sets(set_1, set_2, set_3))
