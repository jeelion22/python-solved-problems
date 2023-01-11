def get_list(inp_str):
    num_list = []
    for item in inp_str:
        num_list.append(int(item))
    return sorted(num_list)


def get_K_sum_pairs(num_list, int_K):

    pair_list = []
    for num in num_list[:-1]:
        for pair in num_list[num_list.index(num) + 1 :]:
            if pair == int_K - num:
                pair_list.append((num, pair))
    pair_list = set(pair_list)
    pair_list = list(pair_list)
    return sorted(pair_list)


inp_str = input().split(",")
int_K = int(input())
num_list = get_list(inp_str)

for pairs in get_K_sum_pairs(num_list, int_K):
    print(pairs)
