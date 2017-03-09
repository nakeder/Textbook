#fortune cookie

import random
input('press any key to draw cuts')
number = random.randint(1,3)
print(number),
if number == 1:
    print("good luck,you choose the first one")
elif number == 2:
    print("good luck,you choose the second one")
else:
    print("sorry,nothing for you.")

input('press any key to quit')


