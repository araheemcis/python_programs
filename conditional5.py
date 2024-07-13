## code to check if the input is a valid  float number else try the correct format before proceeding
# Weight conversion program

#weight = 0
while True:
  try:
     weight = float(input("Enter Weight : "))       
  except ValueError:
    print("Not an number!")
    continue
  else:
    unit = input("What is unit of weight? (K)gs or (L)bs. Type K or L")
    if unit.lower() == 'k':
      conversion = round(float(weight * 2.2),2)
      print(f" The weight is {conversion} pounds")
    elif unit.lower() == 'l':
      conversion = round(float(weight / 2.2),2)
      print(f"The weight is {conversion} kgs")
    else:
     print("Invalid conversion unit number")
    break

    weight = userInput * 2
    print(f"{weight}")
    break 