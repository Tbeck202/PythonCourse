import re
# song = 'WUBWUBIWUBAMWUBWUBX'
# song = 'AWUBWUBWUBBWUBWUBWUBC'
# song = 'WUBPOOPWUBWUBWUBBWUBWUBWUBCWUB'
song = 'AWUBWUBWUBBWUBWUBWUBC'
def song_decoder(target):
    decoded = ''
    recoded = ''
    no_wubs = target.replace('WUB', ' ')

    for index, item in enumerate(no_wubs):
        if item != ' ':
            decoded += f"{item}"
        elif index > 0 and item == ' ':
            check_space = str(no_wubs[index - 1])
            if check_space != ' ':
                decoded += item
    for idx, item in enumerate(decoded):
        if idx == len(decoded) - 1 and item == ' ':
            continue
        else:
            recoded += f"{item}"
    return recoded



# def song_decoder(target):
#     decoded = ''
#     recoded = ''
#     clean_target = ''
#     wub = ('W','U','B')
#     for index, letter in enumerate(target):
#         if letter not in wub:
#             decoded += f"{letter}"
#         elif letter == 'W':
#             check_one_a = str(letter)
#             check_one_b = str(target[index+1])
#             check_one_c = str(target[index+2])
#             check_one = f"{check_one_a}{check_one_b}{check_one_c}"
#             if check_one != 'WUB':
#                 decoded += f"{letter}"
#             elif check_one == 'WUB':
#                 decoded += ' '
#         elif letter == 'U':
#             check_two_a = str(letter)
#             check_two_b = str(target[index-1])
#             check_two_c = str(target[index+1])
#             check_two = f"{check_two_b}{check_two_a}{check_two_c}"
#             if check_two != 'WUB':
#                 decoded += f"{letter}"
#         elif letter == 'B':
#             check_three_a = str(letter)
#             check_three_b = str(target[index-1])
#             check_three_c = str(target[index-2])
#             check_three = f"{check_three_c}{check_three_b}{check_three_a}"
#             if check_three != 'WUB':
#                 decoded += f"{letter}"
#     print(f'Length of decoded: {len(decoded) - 1}')
#     for idx, item in enumerate(decoded):
#         print(idx)
#         if item != ' ':
#             recoded += item
#         elif item == ' ' and idx > 0 and idx != len(decoded) - 1:
#             check_space = str(decoded[idx-1])
#             if check_space != ' ':
#                 recoded += ' '
#     print(recoded)
#     trailing_space = True
#     while trailing_space:
#         for idx, item in enumerate(recoded):
#             print(item)
#             if idx == len(recoded) - 1 and item == ' ':
#                 trailing_space = False
#             else:
#                 clean_target += f"{item}"

#     print(target)
#     return clean_target


# song_decoder(song)
print(song_decoder(song))