# Creating a mini game of rock, scissor and paper where a player will play with computer
# In this game, user has to input one of the three options: rock, scissor or paper
# Computer will randomly select one of the three options
# The result of selection will be displayed on the screen
# Rock beats scissor, scissor beats paper and paper beats rock and if both are same, then it is a tie
# User will be presented an option if he wants to continue playing or not
# If user wants to continue, then game will continue else it will stop
# At the prompt type screen, user will be asked to enter one of the three options
# When the game stops, user will be presented with score which will list total games played by him and total won
# This will be a simple game with no GUI
# There will be validation check that lower case of user input word matches one of the rock, scissor or paper

import random
import sys

def main():
    print("Welcome to Rock, Scissor and Paper game")
    play_game()

def play_game():
    user_wins = 0
    total_games = 0
    while True:
        user_input = input("Enter your choice (rock, scissor, paper): ")
        user_input = user_input.lower()
        if user_input in ["rock", "scissor", "paper"]:
            total_games += 1
            computer_input = random.choice(["rock", "scissor", "paper"])
            print(f"Computer's choice: {computer_input}")
            if user_input == computer_input:
                print("It's a tie")
            elif user_input == "rock":
                if computer_input == "scissor":
                    print("You win")
                    user_wins += 1
                else:
                    print("Computer wins")
            elif user_input == "scissor":
                if computer_input == "paper":
                    print("You win")
                    user_wins += 1
                else:
                    print("Computer wins")
            elif user_input == "paper":
                if computer_input == "rock":
                    print("You win")
                    user_wins += 1
                else:
                    print("Computer wins")
            #print(f"Total games played: {total_games}, Total games won: {user_wins}")
            continue_playing = input("Do you want to continue playing? (yes/no): ")
            if continue_playing.lower() == "no":
                print("Thanks for playing")
                print(f"Total games played: {total_games}, Total games won: {user_wins}")
                sys.exit()
        else:
            print("Invalid input. Please enter one of the rock, scissor or paper")

# Call the main function
if __name__ == "__main__":
    main()