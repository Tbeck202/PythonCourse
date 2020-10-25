with open("haiku.txt", "w") as file:
    file.write("Writing files is great\n")
    file.write("Here's another line of text\n")
    file.write("Closing now, goodbye!")
    file.write("\n")

with open("haiku.txt", "a") as file:
    file.write("Here's one more haiku\n")
    file.write("What about the older one?\n")
    file.write("Let's go check it out!")

# with open("haiku.txt", "r+") as file:
#     file.write("Added later with r+")

# with open("lol.txt", "w") as file:
#     file.write("haha" * 10)
