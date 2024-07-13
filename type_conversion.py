from datetime import datetime

birth_string = input('Birth Year: ')

current_year = datetime.now().year
birth_year = int(birth_string)

age = current_year - birth_year

print('your age is : ',  age)




