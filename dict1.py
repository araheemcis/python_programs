phone = input("phone: ")
digits_mappings = {
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four",
    "5": "five",
    "6": "six",
    "7": "seven",
    "8": "eight",
    "9": "nine"
}
output = ""
output2 = ""
for i in phone:
   output += digits_mappings.get(i, "!") + " "   # output += digits_mappings[i] + " "
   output2 += digits_mappings[i] + " "
   
print(output2)
