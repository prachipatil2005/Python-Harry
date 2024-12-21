'''
1 for snake
-1 for water
0 for gun
'''
import random
computer =random.choice([-1,0,1])#()function []list
youstr = input("Enter your choice (s for snake, w for water, g for gun): ")
youDict = {"s": 1, "w": -1, "g": 0}
reverseDict={1:"Snake",-1:"Water",0:"Gun"}
you = youDict[youstr]
print(f"You choose:{reverseDict[you]}\nComputer chosse:{reverseDict[computer]}")

if computer == -1:  # Computer chooses water
    if you == 1:
        print("You win")
    elif you == 0:
        print("You lose")
    else:
        print("It's a draw")
elif computer == 1:  # Computer chooses snake
    if you == -1:
        print("You lose")
    elif you == 0:
        print("You win")
    else:
        print("It's a draw")
elif computer == 0:  # Computer chooses gun
    if you == -1:
        print("You win")
    elif you == 1:
        print("You lose")
    else:
        print("It's a draw")
else:
    print("something went wrong")