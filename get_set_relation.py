num_set = {1, 2, 3, 4, 5, 6, 7, 8, 9}
# Write your code here
def get_set(num_list):
    int_list = []
    for i in num_list:
        int_list.append(int(i))
    return set(int_list)


def get_set_relation(set_1, set_2):
    if set_1.issuperset(set_2):
        return "Superset"
    elif set_1.issubset(set_2):
        return "Subset"
    elif set_1.isdisjoint(set_2):
        return "Disjoint Set"


num_list = input().split(" ")
print(get_set_relation(num_set, get_set(num_list)))
