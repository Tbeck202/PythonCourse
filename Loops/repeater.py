print("Tell me what I should yell.")
phrase = input()
print("Now, how many times should I yell it?")
yell_num = int(input())

for yell in range(yell_num):
    print(f"{yell + 1}: {phrase}")
