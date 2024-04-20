# Vishal is creating a form and he wants to take the contact number as input. However, some people do not enter the number properly. Vishal is confused about how to verify whether the given number is in the correct format or not. To help Vishal write a python program to show how we can verify whether a given phone number is valid or not. ● Note: A valid phone number contains 10 digits with 9,8 or 7 as the first digit. Phone number only contains numbers and not any character. ● Hint: ● User len() function to verify the number of digits. ● Use isnumeric() function to check it only contains numeric values.Use indexing to check whether the first character is 9,8 or 7 or not.
phone_number = input("Enter the phone number: ")

if len(phone_number) != 10:
    print("Invalid phone number")
else:
    if not phone_number.isnumeric():
        print("Invalid phone number")
    else:
        first_digit = phone_number[0]
        if first_digit not in ['9', '8', '7']:
            print("Invalid phone number")
        else:
            print("Valid phone number")
