# coin
# you give times,we give you anwser
import random
aim = int(input('Please input a number \n'))
up = 0
down = 0
times = 0
while times < aim:
    times += 1
    key = random.randint(0,1)
    if key == 1:
        up += 1
    else:
        down += 1
print("\nThere are",up,"times side up and",down,"times side down.")
input('\nPress enter to quit')