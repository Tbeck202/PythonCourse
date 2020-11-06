from csv import DictReader

with open('fighters.csv') as file:
    dict_reader = DictReader(file)
    for fighter in dict_reader:
        print(f"{fighter['Name']} is from {fighter['Country']} and is {fighter['Height (in cm)']}cm tall")