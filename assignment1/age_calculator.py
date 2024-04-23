# Rakshita wants to calculate her age. So she subtracted her year of birth from the current year. Her classmates also wanted to find their age in the same way. So she decides to write a python program where students can input their year of birth, then the program will print their age. Write the same program to find your age and help your classmates in finding their age

def calculate_age(year_of_birth):
    current_year = 2024
    age = current_year - year_of_birth
    return age


year_of_birth = int(input("Enter your year of birth: "))

age = calculate_age(year_of_birth)

print("Your age is:", age)
