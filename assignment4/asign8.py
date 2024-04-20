# A year consists of 365 days. But once in every four years, it consists of 366 days. And that is known as a leap year. Shisha wants to know whether the current year is a leap year or not. She found that any year divisible by 4 is a leap year, if the year is divisible by 100 then it will not be a leap year, and if the year is divisible by 400 then it will be a leap year. Write a program in python to check whether the given year is a leap year or not to help Shisha. ● Hint: Use if elif else condition

year = int(input("Enter year :"))

if year % 4 == 0:
    print("Leap year")
else:
    print("Not a leap year")
