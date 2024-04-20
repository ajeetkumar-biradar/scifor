# 1:Aarush recently learned probability in his school. He was finding the probability of different events and he wondered whether he can develop a program to do the same thing or not. To help Aarush create a program in python where user can enter number of favorable outcomes and total number of possible outcomes and then program will print the probability of that event on the screen. ● Note: ● Print the probability of the event only up to 2 decimal places. ( For this use round() function ) ● Sample run ● >>Enter the number of favorable outcomes: 1 ● >>Enter the total number of possible outcomes: 2 ● >>Probability: 0.5
favorable_outcomes = int(input("Enter the number of favorable outcomes: "))
total_outcomes = int(input("Enter the total number of possible outcomes: "))

probability = favorable_outcomes / total_outcomes

print("Probability:", round(probability, 2))