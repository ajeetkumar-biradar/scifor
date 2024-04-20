import random


def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])


def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
            (user_choice == 'paper' and computer_choice == 'rock') or \
            (user_choice == 'scissors' and computer_choice == 'paper'):
        return "You win!"
    else:
        return "Computer wins!"


def simulate_game():
    user_choice = random.choice(['rock', 'paper', 'scissors'])
    computer_choice = get_computer_choice()
    print(f"You chose {user_choice}. Computer chose {computer_choice}.")
    print(determine_winner(user_choice, computer_choice))


simulate_game()
