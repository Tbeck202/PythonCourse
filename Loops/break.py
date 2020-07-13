# while True:
#     command = input("Type 'stop' to stop: ")
#     if command == "stop":
#         break

print("I'll say whatever you want, as many times as you want.")
msg = input("Tell me what to say: ")
times = int(input("How many times should I say it? "))
for x in range(times):
    print(msg)
    if x == 5:
        print("Nevermind, I got bored.")
        break
