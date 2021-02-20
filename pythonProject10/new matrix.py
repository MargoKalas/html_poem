from random import randint


def print_matrix(matrix, columns, rows, title="Original matrix"):
    print(title)
    for i in range(0, columns):
        row = ''
        for j in range(0, rows):
            cell = matrix[i][j]
            cell_formated = f'{cell: >3},'
            row = row + cell_formated
        print(row)


def generate_matrix(rows, columns):
    M = [[randint(-10, 10) for i in range(1, columns+1)] for j in range(1, rows+1)]

    return(M)


def find_null_index(matrix, rows, columns, null_rows=None, null_columns=None, title="Matrix after null"):
    print(title)
    for i in range(0, columns):
        for j in range(0, rows):
            cell = matrix[i][j]
            if cell == 0:
                null_rows.append(j)
                null_columns.append(i)
    print(null_rows, null_columns)
    null_rows_or_columns(matrix, rows, columns, null_rows, null_columns)


def null_rows_or_columns(matrix, rows, columns, null_rows=None, null_columns=None):
    null_rows = null_rows or []
    null_columns = null_columns or []
    for i in range(0, columns):
        for j in range(0, rows):
            if i in null_columns or j in null_rows:
                matrix[i][j] = 0


def main():
    rows, columns = 5, 5
    M = generate_matrix(rows, columns)
    print_matrix(M, rows=rows, columns=columns, title=f"Original matrix")
    find_null_index(matrix=M, rows=rows, columns=columns, null_rows=[], null_columns=[])
    print_matrix(matrix=M, rows=rows, columns=columns, title=f"Matrix after null")


main()
    #find_null_rows_and_columns(matrix=M, rows=rows, columns=columns, null_rows=[], null_columns=[])
    #print_matrix(matrix=M, rows=rows, columns=columns, title=f"Matrix after null")
    #null_rows_or_columns(matrix, rows, columns, null_rows, null_columns)
    #print_matrix(matrix=matrix, rows=rows, columns=columns, title=f"Matrix with null")





#    null_rows_or_columns(matrix=M, rows=rows, columns=columns, null_rows=[0], null_columns=[0])
#    print_matrix(matrix=M, rows=rows, columns=columns, title=f"Matrix after null")


#def inicialising_matrix(matrix=matrix, null_rows=[0], null_columns=[0]):
#    for i in range(0, null_rows):
#            for j in range(0, null_columns):

#                if null_rows() and null_columns():
#                    print("The matrix does not contain zeros")
#                return(M)
#            else:
#                for i in range(null_columns=[0]):
#                    rows = ''
#                    for j in range(null_rows=[0]):
#                        cell = M[i][j]
#                        cell_formated = f'{cell: >3},'
#                        row = row + cell_formated
#                    print(row)
#                    print("Matrix null")


