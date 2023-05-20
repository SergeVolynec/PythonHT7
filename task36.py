def print_operation_table(operation, num_rows=6, num_columns=6):
    return list(map(lambda x: print(*list(map(lambda y: operation(x, y),
                                              range(1, num_columns+1)))), range(1, num_rows+1)))


print_operation_table(lambda x, y: x * y)
