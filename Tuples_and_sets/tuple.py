#

# months = ('jan', 'feb', 'mar', 'apr', 'may', 'jun',
#           'jul', 'aug', 'sep', 'oct', 'nov', 'dec')
# for mon in months:
#     if mon[0] == 'j':
#         print(mon)

locations = {
    (35.6895, 39.6917): 'Tokyo',
    (41.7128, 74.0060): 'New York',
    (37.7749, 122.4194): 'San Francisco'
}

check = 0

while check == 0:
    requested_city = input(
        'What city office are you looking for?')
    for coord, city in locations.items():
        if requested_city.lower() == city.lower():
            check += 1
            print(
                f'Our {city} is located at latitude: {coord[0]}, Longitude:{coord[1]}.')
            break
    if check == 0:
        print(f"Sorry, we don't have an office in {requested_city}")
