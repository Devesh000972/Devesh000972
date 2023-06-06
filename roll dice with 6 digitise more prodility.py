import random

list = [1,2,3,4,5,6,6,6,6,6,1]

i = int(input ('Enter How many times to roll the dice:'))
for n in range(i):
    nu = random.choice(list)
    print (nu)