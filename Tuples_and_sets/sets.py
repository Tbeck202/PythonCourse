# cities = ['Los Angeles', 'Boulder', 'Kyoto', 'Florence', 'Santiago',
#           'Los Angeles', 'Shanghai', 'Boulder', 'San Francisco', 'Oslo', 'Tokyo']

# no_duplicates = set(cities)
# # print(no_duplicates)

# no_duplicates.add('Portland')

# print(no_duplicates)

# no_duplicates.remove('Shanghai')
# print(no_duplicates)

# ============================

# math_students = {"Matt", "Helen", "Prashant", "James", "Aparna"}
# biology_students = {"Jane", "Matt", "Charlotte", "Mesut", "Oliver", "James"}

# all_students = math_students | biology_students
# print(all_students)
# dual_students = math_students & biology_students
# print(dual_students)

# =======================
# COMPREHENSION

# print({x**2 for x in range(10)})
# print({x: x**2 for x in range(10)})

user_string = input("Type a word, homie!\n")
vowel_check = len({char for char in user_string if char in 'aeiou'})

if vowel_check == 5:
    print(f"{user_string} has all five vowels in it!")
elif vowel_check > 1:
    print(f"{user_string} has {vowel_check} unique vowels in it.")
elif vowel_check == 1:
    print(f"{user_string} has {vowel_check} unique vowel in it.")
else:
    print(f"{user_string} has no unique vowels in it.")
