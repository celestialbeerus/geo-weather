#we have to make game of rock paper scissor
#so first we are going to import a random number to choose a number 
import random
'''
so we are choosing 
-1 for rock
0 for paper
1 for scissor
'''
computer=random.choice([-1,0,1])
user=input("Enter your choice:\n")
useroption={"r":-1,"p":0,"s":1}
reversevalue={1:"scissor",0:"paper",-1:"rock"}
value=useroption[user]
print(f"You chose {reversevalue[value]}\ncomputer chose {reversevalue[computer]}")
if(computer == value):
    print("It's a draw!")


else:
    if(computer == -1 and value ==0):
        print("You win!")
    elif(computer == -1 and value ==1):
        print("You lose!")
    elif(computer == 0 and value ==-1):
        print("You lose!")
    elif(computer == 0 and value ==1):
        print("You win!")
    elif(computer == 1 and value ==0):
        print("You win!")
    elif(computer == 1 and value ==-1):
        print("You lose!")
    else:
        print("Invalid choice,please select r(rock),p(paper),s(stone)")    
