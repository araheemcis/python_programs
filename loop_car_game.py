
i = 0
while i < 5:
    input1 = input(">:").lower()
    if input1()  not in ["help","start","stop","quit"]:
        print(" Invalid option, please reenter.You have",(4 - i),"  retries left")
        i = i + 1
    else:
        break
        
if input1 == 'help':
        print(''' 
          start - to start the car
          stop - to stop the car
          quit - to exit \n
          ''')
        input2 = input("please enter valid option >")
        if input2 in ['start','stop','quit']:
            if input2 == 'start':
                print(f"the car is started ...")
            elif input2 == 'stop':
                print(f"car is stopped")
            elif input2 == 'quit':
                print(f"quit the program")
            else:
                print("invalid entry")
                
elif input1 == 'start':
     print(f"the car is started ...")
elif input1 == 'stop':
     print(f"the car is stopped")
elif input1 == 'quit':
     print(f"quit")
else:
    
    print(f"invalid option {input1}, max tries reached")