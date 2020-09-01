d = {'name': 'Ricky'}

def get(d,key):
    try:
        return d[key]
    except KeyError:
        return None

print(get(d,'name')) # Ricky
print(get(d,'city')) # None

#============================================

while True:
    try:
        num = int(input('Please enter a number: '))
    except ValueError:
        print("That's not a number!")
    else:
        print(f"You entered {num}")
        break
    finally:
        print('"Finally" runs no matter what!')
