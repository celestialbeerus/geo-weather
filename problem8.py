# Write a program to find the greatest of four numbers entered by the user. 
a=int(input("Enter the value of a :"))
b=int(input("Enter the value of b :"))
c=int(input("Enter the value of c :"))
d=int(input("Enter the value of d:"))

if(a>b and a>c and a>d):
    print("a is greatest among all \n value of a is %i"%a)
elif(b>a and b>c and b>d):
    print("b is greatest among all \n value of b is %i"%b)
elif(c>b and c>a and c>d):
    print("c is greatest among all \n value of c is %i"%c)
elif(d>b and d>c and d>c):
    print("d is greatest among all  \n value of d is %i"%d)

