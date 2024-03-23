name = input("Please create you username: ")
names = (len(name))
if names < 3:
    print("Name must be at least 3 characters")
elif names > 50:
    print("Name can be a maximum of 50 characters")
else:
    print("Your name is ",name.upper(), ", looks good!")



