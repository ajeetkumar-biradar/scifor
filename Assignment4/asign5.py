# Yash and Vishal have invested 10000$ in their bank. Yash is getting 6% simple interest from his bank and Vishal is getting 6% compound interest from his bank. Write a python program to calculate the difference in their returns after 30 years. What is the difference in their return in one year? What is the reason for this difference? Discuss ● Hint: Use the following parameters to calculate interest ● Principal amount ● Time ● Rate of interest
amount = int(input("enter the principal amount : "))

time = int(input("Enter the time : "))

interest = float(input("enter the rate of interest : "))

si = (amount*time*interest)/100

print(si)