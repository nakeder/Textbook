# Guess My Number V2.0
# You need prepare a number in your heart,and the computer will guess the number.
import random
print("Now,you need choose a number form 0 to 100,I will guess the number as soon as possible")
input("\nPress Enter to begin this game")
guess_num = random.randint(0,100)
print("The number is",guess_num,",right?")
key = input("Please answer yes or no.\n")
begin_num = 0
end_num = 100
tries = 1
while key == "no" or key == "n":
    wrong_num = guess_num
    ans = input("Is the number I guessed higher than yours? Please answer yes or no.\n")
    if ans == "yes" or ans == "y":
        end_num = wrong_num - 1
        guess_num = random.randint(begin_num,end_num)
        print("The number is",guess_num,",right?")
        # print("from",begin_num,"to",end_num)
        key = input("Please answer yes or no.\n")
    else:
        begin_num = wrong_num + 1
        guess_num = random.randint(begin_num,end_num)
        print("The number is",guess_num,",right?")
        # print("from",begin_num,"to",end_num)
        key = input("Please answer yes or no.\n")
    tries += 1
print("I only use",tries,"times to get the right number.")
input("\nPress Enter to quit this game")