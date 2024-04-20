# Jack, a 19 year old, has learnt python. He has written a code using python that will literally accept color names as an input from the user and prints all of the colors. Jack is still thinking of a logic and whenever the color is red hence he wrote a if condition inside a for loop but the compiler started throwing an error stating that if condition cannot be left empty.
# So write a python program to help Jack to keep his if condition empty temporarily and print rest of the colors using a for loop

colors = ["red", "blue", "green", "yellow", "orange", "purple", "pink", "brown", "black", "white"]

for color in colors:
    if color == "red":
        pass  # Temporary placeholder to keep the if condition empty
    else:
        print(color)