# :Shubham is worried about his health. He keeps checking his height and weight daily. Recently he came to know about the BMI report, and now he wants to calculate his own BMI by writing a python program. Write a program in python to check your BMI by putting your height and weight as input. ● Note: ● Body Mass Index is a simple calculation using a person's height and weight. The formula is BMI = kg/m2 where kg is a person's weight in kilograms and m2 is their height in meters squared. A BMI of 25.0 or more is overweight, while the healthy range is 18.5 to 24.9. BMI applies to most adults 18-65 years.
try:
    height = float(input("Enter your height in meters: "))
    weight = float(input("Enter your weight in kilograms: "))

    if height <= 0 or weight <= 0:
        print("Height and weight must be positive numbers.")
    else:
        bmi = weight / (height ** 2)
        print("Your BMI is:", bmi)

        if bmi < 18.5:
            print("You are underweight.")
        elif bmi >= 18.5 and bmi <= 24.9:
            print("You are in the healthy weight range.")
        else:
            print("You are overweight.")

except ValueError:
    print("Invalid input. Please enter valid numbers for height and weight.")