nums1 = [1, 2, 3, 4, 5]
nums2 = [6, 7, 8, 9, 10]

z = zip(nums1, nums2)
print(list(z))  # [(1, 6), (2, 7), (3, 8), (4, 9), (5, 10)]

players = ['Rudy', 'Donovan', 'Joe', 'Royce', 'Mike']
jerseynums = [27, 45, 2, 23, 10]
zdict = dict(zip(players, jerseynums))
print(zdict)

five_by_two = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5)]
print(list(zip(*five_by_two)))  # [(0, 1, 2, 3, 4), (1, 2, 3, 4, 5)]

midterms = [80, 91, 78]
finals = [98, 89, 53]
students = ['dan', 'ang', 'kate']

# final_grades = [max(t) for t in zip(midterms, finals)]
final_grades = {t[0]: max(t[1], t[2]) for t in zip(students, midterms, finals)}
print(final_grades)
