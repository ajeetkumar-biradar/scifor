# A palindrome is a word, number, phrase, or other sequence of characters that reads the same backward as forward, such as madam or racecar. Arunima got a new puppy (pet) and she wants to decide the name for her pet. The name of the pet should be a palindrome. Write a program to take the pet name as input and print "true" if it is palindrome or print "false" on screen. Help Arunima to decide the name ( should be palindrome ) of the puppy. Hint: reverse the name and compare it with the original name.
pet_name = input("Enter the name for your pet: ")

pet_name = pet_name.lower()

reversed_name = pet_name[::-1]

if pet_name == reversed_name:
    print("true")
else:
    print("false")