instructor = {
    'name': 'Colt',
    'owns_dog': True,
    'num_courses': 4,
    'fav_lang': 'Python',
    'is_funny': False,
    44: 'Fav number'
}
# for key in instructor.keys():
#     print(key)
# print(" == == == == == == == == == =")
# for val in instructor.values():
#     print(val)
# print(" == == == == == == == == == =")
# for k, v in instructor.items():
#     print(f"{k}: {v}")

# instructor_name = instructor.get("name")
# print(instructor_name)

# test_dict = {}.fromkeys(range(1, 10), 'blank')
# print(test_dict)

# instructor_2 = instructor.copy()
# print(f'{instructor == instructor_2} {instructor is instructor_2}')

# item = instructor.popitem()
# item2 = instructor.popitem()
# item3 = instructor.pop('name')
# print(item)
# print(instructor)
# print(item2)
# print(instructor)
# print(item3)
# print(instructor)

print(instructor)

person = {'city': 'Portland'}
person.update(instructor)
print(person)
