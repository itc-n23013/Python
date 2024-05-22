def print_table(table_data):

    col_widths = [max(len(item) for item in column) for column in table_data]

    transposed_table = list(zip(*table_data))

    for row in transposed_table:
        for i, item in enumerate(row):
            print(item.rjust(col_widths[i]), end=' ')
        print()

table_data = [['apples', 'oranges', 'cherries', 'banana'],
              ['Alice', 'Bob', 'Carol', 'David'],
              ['dogs', 'cats', 'moose', 'goose']]

print_table(table_data)


