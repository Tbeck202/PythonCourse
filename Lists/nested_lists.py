# nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# [[print(val) for val in l] for l in nested_list]

# board = [[num for num in range(1, 4)] for val in range(1, 4)]
# print(board)

board = [[['*' for place in range(0, 3)]
          for list in range(1, 4)] for list in range(1, 4)]
print(board)
