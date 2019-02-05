"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------

For this first project we will be using Workspaces. 

NOTE: If you strongly prefer to work locally on your own computer, you can totally do that by clicking: File -> Download Workspace in the file menu after you fork the snapshot of this workspace.

"""

import random


def show_intro():  #Show game text before starting game
    print("Welcome to the Number Guessing Game:\n")
    print("""
        You will need to guess a number between 1 and 20.
        The program will let you know whether the number is higher or lower based on your last guess.
        Once you correctly guess the number then the program will let you know how many guesses you had
        You will also see if you got the highest score

        You can press q while guessing to end the game
        """)

def menu_text():
    print()
    print("""
        a: Play Game
        b: See Lowest Score
    
        q: Quit Game
    """)


def highest_score(score):
    print("\n The current highest score is {}".format(score))

def check_lowest(number, best):
    if best is None:
        print("You are the first person to play the game so you have the lowest score of {}".format(number))
        return number
    elif number < best:
        print("Congratulations....... You have the lowest score of {}.".format(number))
        return number
    else:
        print("Sorry your {} attempts is higher than {} guesses.".format(number, best))
        return best
    

def check_guess(correct_number, guess):
    if guess < correct_number:  #Checking number is lower than correct number return false
        print("Your guess ({}) is lower than the correct number".format(guess))
        return False
    elif guess > correct_number:  #Checking number is higher than correct number return false
        print("Your guess ({}) is higher than the correct number".format(guess))
        return False
    else:
        print("Correct, {} is the correct number!".format(guess))
        return True


def start_game():
    best_score = None
    while True:
        menu_text()
        menu_choice = input("Please enter a menu_choice: ")
        if menu_choice.lower() == "a":
            game_number = random.randint(1, 20)
            attempt = 0
            correct = False
            while correct != True:
                print("The current lowest score is {}\n".format(best_score))
                number_guess = input("Please choose a number between 1 and 20: ")
                if number_guess.lower() == 'q':
                    attempt = 0
                    break
                else:
                    try:
                        number_guess = int(number_guess)
                    except ValueError:
                        print("You need to enter a whole number as your guess, try again!")
                        continue
                if number_guess < 1 or number_guess > 20:
                    print("You have entered a number outside the range of the game, try again")
                    continue 
                attempt += 1  
                correct = check_guess(game_number, number_guess)
            print("End of Game.  Your score is {}\n".format(attempt))
            best_score = check_lowest(attempt, best_score)
            continue
        elif menu_choice.lower() == "b":
            highest_score(best_score)
            continue
        elif menu_choice.lower() == "q":
                print("\n Thanks for playing.  Goodbye!")
                break  
        else:
            print("Sorry wrong selection, try again")
            continue

if __name__ == '__main__':

    show_intro()
    start_game()
