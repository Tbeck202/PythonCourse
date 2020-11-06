from csv import DictReader, DictWriter

with open('cats.csv', 'w') as file:
    headers = ['Name', 'Breed', 'Age']
    csv_writer = DictWriter(file, fieldnames=headers)
    csv_writer.writeheader()
    csv_writer.writerow({
        "Name": "Garfield",
        "Breed": "Tabby",
        "Age": 10
    })