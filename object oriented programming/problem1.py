#Write a class “Calculator” capable of finding square, cube and square root of a number
class calculator:
    a=('''
                1. Square 
                2. Cube
                3. Square Root
                4. Exit''')
        
calac=calculator()
print(calac.a)
user=int(input("enter your choice:\n"))
if(user==4):
    print("Exiting......")
else:    
    ent_num=float(input("enter the number:\n"))
    if(user==1):
        print(f"the square of {ent_num} is {ent_num*ent_num} ")
    elif(user== 2):
        print(f"the cube of {ent_num} is {ent_num*ent_num*ent_num} ")
    elif(user== 3):
        print(f"the square of {ent_num} is {ent_num**0.5} ")
    else:
        print("You enter invalid input.\n Please select input 1,2,3 or 4")
