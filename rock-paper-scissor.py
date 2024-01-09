import random

def get_computer_choice():
   choices = ['rock', 'paper', 'scissors']
   return random.choice(choices)

def get_player_choice():
   choice = input("Enter your choice (rock, paper, or scissors): ")
   return choice

def determine_winner(player_choice, computer_choice):
   if player_choice == computer_choice:
       return "It's a tie!"
   elif (player_choice == 'rock' and computer_choice == 'scissors') or \
       (player_choice == 'paper' and computer_choice == 'rock') or \
       (player_choice == 'scissors' and computer_choice == 'paper'):
       return "Player wins!"
   else:
       return "Computer wins!"

player_choice = get_player_choice()
computer_choice = get_computer_choice()

print("Player chose", player_choice)
print("Computer chose", computer_choice)

winner = determine_winner(player_choice, computer_choice)
print(winner)
