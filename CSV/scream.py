from csv import reader, writer

with open('fighters copy.csv') as file:
    csv_reader = reader(file)
    screaming_fighters = [[s.upper() for s in row] for row in csv_reader]
    print(screaming_fighters)

with open('screaming_fighters.csv', 'w') as file:
    csv_writer = writer(file)
    for fighter in screaming_fighters:
        csv_writer.writerow(fighter)