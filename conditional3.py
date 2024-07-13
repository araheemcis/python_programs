price_string = input("What is the price of the house? ")
price = int(price_string)
credit = input("Is your credit good ,Yes or No ?")

if credit == 'Yes':
    print("you have to put down \n ",(price * 10 / 100))
else:
    print("You have put down \n", (price * 20/100))