
i = 0
while i < 5:
    input1 = input(">:")
    if input1 != 'help':
        print(" Invalid option, please reenter.You have",(4 - i),"  retries left")
        i = i + 1
    else:
        break
        
if input1 == 'help':
    print(''' 
          start - to start the car
          stop - to stop the car
          quit - to exit ''')
elif input1 == 'start':
     print(f"the car is started ...")
elif input1 == 'stop':
     print(f"the car is stopped")
elif input1 == 'quit':
     print(f"quit")
else:
    
    print(f"invalid option {input1}, max tries reached")