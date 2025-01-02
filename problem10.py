# Write a program 
# to find out whether a given post is talking about “Harry” or not.
post=input("enter the post")
if("Harry".lower()  in post.lower()  ): #using.lower we can basically program advance as if someone write haRry then detect this post is talking about harry
    print("this post is talking about harry ")
else:
    print("this post is not talking about harry")