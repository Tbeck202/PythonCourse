nums = [1, 2, 3, 99, 4, 5, 6, 7, 8, 9]
print(max(nums))
print(min(nums))

names = ['Karl', 'Donovan', 'Andrei', 'Bryon', 'Deron', 'John']
longest = max(names, key=lambda n: len(n))
print(longest)

songs = [
    {'title': 'Just Like a Woman', 'playcount': 55},
    {'title': 'Lua', 'playcount': 500},
    {'title': 'WAP', 'playcount': 5}
]

least_played = min(songs, key=lambda song: song['playcount'])
most_played = max(songs, key=lambda song: song['playcount'])
print(
    f"The least played song is {least_played['title']}, with only {least_played['playcount']} plays")
print(
    f"The most played song is {most_played['title']}, with {most_played['playcount']} plays")
