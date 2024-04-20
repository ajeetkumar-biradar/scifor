# Nidhi's father is not able to calculate his annual tax correctly. He is a bit confused with the taxation rule also each year his total annual income is different. So to help her father Nidhi decides to write a python program that can calculate the tax to be paid based on annual income. Write the same program to calculate the tax to be paid based on annual income. ● Hint: take the annual income as input from the user and print the amount of tax to be paid. These are tax rules.

try:
    annual_income = float(input("Enter your annual income: "))

    if annual_income < 0:
        print("Annual income cannot be negative.")
    else:
        if annual_income <= 250000:
            tax = 0
        elif annual_income <= 500000:
            tax = (annual_income - 250000) * 0.05
        elif annual_income <= 1000000:
            tax = 12500 + (annual_income - 500000) * 0.2
        else:
            tax = 112500 + (annual_income - 1000000) * 0.3

        print("Tax to be paid: ", tax)

except ValueError:
    print("Invalid input. Please enter a valid number.")