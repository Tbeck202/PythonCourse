from csv import writer

with open('dogs.csv', 'w') as file:
    csv_writer = writer(file)
    csv_writer.writerow(['Name', 'Age'])
    csv_writer.writerow(['Lua', 15])
    csv_writer.writerow(['Jasper', 6])