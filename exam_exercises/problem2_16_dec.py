def check_inside_matrix(row, col):
    if row not in range(n) or col not in range(n):
        return False
    return True


def move_up_down(row_position, current_col, word, current_row):
    pass


def move_left(current_row, current_col,  field, word):
    col_position = current_col - 1
    if not check_inside_matrix(current_row, col_position):
        word = word[:-1]
        return current_row, current_col, word
    current_element = matrix[current_row][col_position]
    if not current_element == "-":
        word += current_element
    matrix[current_row][col_position] = "P"
    matrix[current_row][current_col] = "-"
    return current_row, col_position, word


def move_right(current_row, current_col,  field, word):
    col_position = current_col + 1
    if not check_inside_matrix(current_row, col_position):
        word = word[:-1]
        return current_row, current_col, word
    current_element = matrix[current_row][col_position]
    if not current_element == "-":
        word += current_element
    matrix[current_row][col_position] = "P"
    matrix[current_row][current_col] = "-"
    return current_row, col_position, word


def move_up(current_row, current_col, field, word):
    row_position = current_row - 1
    if not check_inside_matrix(row_position, current_col):
        word = word[:-1]
        return current_row, current_col, word
    current_element = matrix[row_position][current_col]
    if not current_element == "-":
        word += current_element
    matrix[row_position][current_col] = "P"
    matrix[current_row][current_col] = "-"
    return row_position, current_col, word


def move_down(current_row, current_col, field, word):
    row_position = current_row + 1
    if not check_inside_matrix(row_position, current_col):
        word = word[:-1]
        return current_row, current_col, word
    current_element = field[row_position][current_col]
    if not current_element == "-":
        word += current_element
    field[row_position][current_col] = "P"
    field[current_row][current_col] = "-"
    return row_position, current_col, word


move_mapper = {
    "left": move_left,
    "right": move_right,
    "up": move_up,
    "down": move_down
}


initial_string = input()
n = int(input())

matrix = []

p_row_index = None
p_col_index = None

for row_index in range(n):
    curr_row = list(input())
    if "P" in curr_row:
        p_row_index = row_index
        p_col_index = curr_row.index("P")
    matrix.append(curr_row)

n_commands = int(input())

for _ in range(n_commands):
    command = input()
    p_row_index, p_col_index, initial_string = move_mapper[command](p_row_index, p_col_index, matrix, initial_string)


print(initial_string)
for row_index in range(n):
    print("".join(matrix[row_index]))