file = open('test.txt')

print(file.read())
print('---------------------------')
file.seek(5)
print(file.read())

file.seek(0)
print('---------------------------')
print(file.readline())
print(file.readline())
print(file.readline())
print('---------------------------')
print('---------------------------')
file.seek(0)
lines = file.readlines()
cnt = 1
for line in lines:
    print(f"line {cnt}: {line}")
    cnt += 1
print('---------------------------')
print(file.closed)
file.close()
print(file.closed)
