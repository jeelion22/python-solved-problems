m, n = input().split(" ")
m = int(m)
n = int(n)

matrix_list = []

for i in range(int(m)):
    new_list = []
    input_list = input().split(" ")
    for item in input_list:
        new_list.append(int(item))
    matrix_list.extend(new_list)


def get_ordered_matrix(matrix_list, m, n):
    matrix_list.sort()
    ordered_matrix = []
    index_position = 0

    for i in range(m):
        ordered_row = []
        count = 1

        for j in range(n):
            ordered_row.append(matrix_list[index_position])
            index_position += 1
        ordered_matrix.append(ordered_row)

    return ordered_matrix


print(get_ordered_matrix(matrix_list, m, n))
