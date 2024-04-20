# "Don't worry!! you got this username!!. buckle up and cheer yourself up. Good days are on their way. There is no beautiful rainbow without a heav.Sir Osborne Smith is a Governor who takes care of Reserve Bank Of India, his son Rahul Smith, a 15 year old, was learning coding being a Governor of RBI Sir Osborne wanted to test the coding skills of Rahul Smith and asked him to write a python code for an ATM machine. But Rahul is confused with few of the concepts.
# So write a python code to explain how an ATM machine code works and to explain the concepts to Rahul
# bank_balance = 50000
# The ATM Machine should be having the following options:
# 1) Withdraw : Withdraw amount that are multiples of 100 like 100, 200, 1000, 2000 and so onNote: throw error if user enters numbers like 111, 112, 781,etc as 1 rupees, 2 rupees, 10 rupees, 50 rupees are impossible in ATM2) Deposit Cash3) Balance Enquiry : Show the
# Account Balance4) Fast Cash : where there will be options on the screen like 5000, 10000, 15000, 20000, 25000, 30000, 40000, 45000, 50000 and the user can just select any one option so.

bank_balance = 50000


def withdraw(amount):
    global bank_balance
    if amount % 100 == 0:
        if amount <= bank_balance:
            bank_balance -= amount
            print("Amount", amount, "withdrawn successfully.")
        else:
            print("Insufficient balance!")
    else:
        print("Please enter amount in multiples of 100.")


def deposit(amount):
    global bank_balance
    bank_balance += amount
    print("Amount", amount, "deposited successfully.")


def balance_enquiry():
    print("Your current account balance is:", bank_balance)


def fast_cash(option):
    options = [5000, 10000, 15000, 20000, 25000, 30000, 40000, 45000, 50000]
    if option in options:
        withdraw(option)
    else:
        print("Invalid fast cash option.")


def main():
    while True:
        print("\nATM Options:")
        print("1) Withdraw")
        print("2) Deposit Cash")
        print("3) Balance Enquiry")
        print("4) Fast Cash")
        print("5) Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            amount = int(input("Enter the amount to withdraw: "))
            withdraw(amount)
        elif choice == 2:
            amount = int(input("Enter the amount to deposit: "))
            deposit(amount)
        elif choice == 3:
            balance_enquiry()
        elif choice == 4:
            print("Fast Cash Options:")
            print("5000, 10000, 15000, 20000, 25000, 30000, 40000, 45000, 50000")
            option = int(input("Select your option: "))
            fast_cash(option)
        elif choice == 5:
            print("Thank you for using our ATM!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
