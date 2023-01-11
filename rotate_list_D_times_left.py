def get_int_list(inp_list):
    int_list = []
    for i in inp_list:
        int_list.append(int(i))
    return int_list


def get_left_rotate_D_times(int_list, rot_tim):
    rotate = rot_tim % len(inp_list)
    return int_list[rotate:] + int_list[:rotate]


inp_list = input().split(",")
rot_tim = int(input())
int_list = get_int_list(inp_list)
print(get_left_rotate_D_times(int_list, rot_tim))
