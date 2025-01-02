# Write a program to fill in a letter template given below with name and date. 
Name=input("enter your Name :")
Date=input("Enter the Date :")
letter = '''  
Dear <|Name|>, 
You are selected! 
<|Date|> 
'''
letter=(letter.replace("<|Name|>",Name).replace("<|Date|>",Date))
print(letter)