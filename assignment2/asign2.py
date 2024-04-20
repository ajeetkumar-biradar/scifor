# It's Domino's 25th Anniversary and is planning for a big give away and in order to choose the lucky draw winner Domino's first needs to collect all of its customer details. On collecting the customer details Domino's even wants to thank each and every customer for visiting as soon as they entered their details.Write a program to accept customer details like customer name, customer mobile number, customer age, customer email Id.On successfully receiving all the customer information write a print() to thank the customer by using his name for example"Hi", customerName,"!! Thanks for visiting our restaurant and registering for our lucky draw competition on our 25th Anniversary.""Once the lucky draw results are announced you will receive a message on your mobile number :",customerMobileNumber"An detailed description of your gift on your email Id :",customerEmailId"Thank you for being a valued customer",customerName,"!!""Dominos"

customer_name = input("Enter your name: ")
customer_mobile_number = input("Enter your mobile number: ")
customer_age = input("Enter your age: ")
customer_email_id = input("Enter your email Id: ")

print("Hi", customer_name, "!! Thanks for visiting our restaurant and registering for our lucky draw competition on our 25th Anniversary.")
print("Once the lucky draw results are announced you will receive a message on your mobile number:", customer_mobile_number)
print("A detailed description of your gift will be sent to your email Id:", customer_email_id)
print("Thank you for being a valued customer", customer_name, "!!")
print("Dominos")