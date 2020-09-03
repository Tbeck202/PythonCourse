# import random - import the whole module
# import random as rand - import the whole module but change the name
#import only what you want
from random import choice, randint

# If you imported the whole module, you use it like below
# print(rand.choice(['apple','banana','cherry','durian']))
# print(rand.randint(0,101))

#if you specified what you want, you use it like below (you don't say the module name, just the part you imported)
print(choice(['apple','banana','cherry','durian']))
print(randint(0,101))
