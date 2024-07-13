name = input("Type your name :")
if len(name) < 3:
    print(" Name must have atlease 3 characters")
elif len(name) > 10:
    print("Name is long")
else:
    print( f"Name {name} is ok")