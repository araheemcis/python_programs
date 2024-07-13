import getpass
count = 0
guess1 = int(getpass.getpass("type the number from 1 to 10:")) # Hidden input from user.
while count < 4:
  guess = int(input("Guess the number ?"))
  if guess == guess1:
      
      count = 4
      break
  else:
      print(f"Try again")
  count = count + 1

if guess == guess1:
    print(f"you guess the correct number {guess1}")
else:
    print(f"sorry you were not able to guess it")