print("Enter a distance in Kilometers, and I'll convert it to miles!")
kms = input()
miles = float(kms)/1.60934
round_miles = round(miles, 2)
print(f"Ok, {kms} kilometers are equal to {round_miles} miles!")
