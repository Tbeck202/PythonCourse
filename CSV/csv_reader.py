from csv import reader

with open("fighters.csv") as file:
    # csv_reader is an iterator, NOT a list. 
    csv_reader = reader(file)
    # use "next" to skip the headers in the csv file
    next(csv_reader)
    for fighter in csv_reader:
        print(f"{fighter[0]} is from {fighter[1]}")

print("=============================")

with open("fighters.csv") as file:
    # csv_reader is an iterator, NOT a list. 
    csv_reader = reader(file)
    # turn csv_reader into a list
    data = list(csv_reader)
    idx = 0
    for fighter in data:
        if idx != 0:
            print(f"{fighter[0]} is from {fighter[1]}")
        idx += 1