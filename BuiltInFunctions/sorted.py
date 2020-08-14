nums = [1, 5, 8, 4, 2, 5, 8, 90, 7, 5, 3]
nums2 = (1, 4, 5, 78, 98, 65, 3, 2, 34, 45, 6, 8, 8, 64, 2)
print(sorted(nums))  # [1, 2, 3, 4, 5, 5, 5, 7, 8, 8, 90]
print(sorted(nums, reverse=True))  # [90, 8, 8, 7, 5, 5, 5, 4, 3, 2, 1]
print(nums)  # [1, 5, 8, 4, 2, 5, 8, 90, 7, 5, 3]

print(sorted(nums2))  # [1, 2, 2, 3, 4, 5, 6, 8, 8, 34, 45, 64, 65, 78, 98]
# [98, 78, 65, 64, 45, 34, 8, 8, 6, 5, 4, 3, 2, 2, 1]
print(sorted(nums2, reverse=True))

# ========================================================================

users = [
    {'username': 'John', 'tweets': ['Go Jazz!', 'FTR!']},
    {'username': 'Karl', 'tweets': ['I love trucks']},
    {'username': 'Andrei', 'tweets': ['ak47 is the GOAT nickname!']}
]

alphabetical = sorted(users, key=lambda user: user['username'])
print(alphabetical)

most_tweets = sorted(users, key=lambda user: len(user['tweets']))
print(most_tweets)


songs = [
    {'title': 'Just Like a Woman', 'playcount': 55},
    {'title': 'Lua', 'playcount': 500},
    {'title': 'WAP', 'playcount': 5}
]

most_played = sorted(songs, key=lambda song: song['playcount'], reverse=True)

# ['Lua', 'Just Like a Woman', 'WAP']
print([song['title'] for song in most_played])
