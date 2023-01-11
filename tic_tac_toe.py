def get_input():
    inputs = []
    for i in range(3):
        str_list = input().split(" ")
        inputs.append(str_list)
    return inputs


def get_winner(matrix):
    pri_dia = matrix[0][0] + matrix[1][1] + matrix[2][2]
    leg_dia = matrix[0][2] + matrix[1][1] + matrix[2][0]
    result = []
    for i in range(3):
        row = ""
        col = ""

        for j in range(3):
            row += matrix[i][j]
            col += matrix[j][i]
        if row == "OOO" or row == "XXX":
            result.append(row)
            if row == "XXX":
                print("Anjali Wins")

            else:
                print("Abhinav Wins")
        elif col == "OOO" or col == "XXX":
            result.append(col)

            if col == "XXX":

                print("Anjali Wins")
            else:
                print("Abhinav Wins")

    if pri_dia == "OOO" or pri_dia == "XXX":
        if pri_dia == "XXX":
            print("Anjali Wins")
        else:
            print("Abhinav Wins")
    elif leg_dia == "OOO" or leg_dia == "XXX":
        if leg_dia == "XXX":
            print("Anjali Wins")
        else:
            print("Abhinav Wins")
    else:
        if len(result) != 0:
            pass
        else:
            print("Tie")


matrix = get_input()

get_winner(matrix)
