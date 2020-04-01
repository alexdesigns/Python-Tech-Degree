import random
user_name = input("What is your name? ")

def start_game():
    print("Welcome to game {}".format(user_name))
    ran_num = random.randint(1, 10)
    print(ran_num)

    game_play = True
    while game_play:
        

        answer = input("Pick a number between 1 - 10: ")

        answer = int(answer)
        attempt = 1

        if answer not in range(1,10):
            print("not in range")
            attempt += 1
        elif answer > ran_num:
            print("It's lower")
            attempt += 1
        elif answer < ran_num:
            print("It's higher")
            attempt += 1
        elif answer == ran_num:
            attempt += 1
            print("Got it. It took you {} attempts.".format(attempt))
            play_again = input("What to restart? Y/N ")
            if play_again == "Y":
                start_game()
            else:
                print("Bye")
                game_play = False

    """Psuedo-code Hints
    
    When the program starts, we want to:
    ------------------------------------
    
    4. Once the guess is correct, stop looping, inform the user they "Got it"
         and show how many attempts it took them to get the correct number.
    5. Let the player know the game is ending, or something that indicates the game is over.
    
    ( You can add more features/enhancements if you'd like to. )
    """
    # write your code inside this function.


if __name__ == '__main__':
    # Kick off the program by calling the start_game function.
    start_game()