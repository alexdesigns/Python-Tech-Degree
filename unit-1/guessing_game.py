import random
user_name = input("What is your name? ")

def start_game():
    print("Welcome to game {}".format(user_name))
    ran_num = random.randint(1, 10)
    #print(ran_num)
    attempt = 0

    game_play = True
    while game_play:
       
        #print(attempt)
        answer = input("Pick a number between 1 - 10: ")
        answer = int(answer)
        high_score = attempt

        if answer < 1 or answer > 10:
            print("not in range")
            attempt += 1
            continue
        elif answer > ran_num:
            print("It's lower")
            attempt += 1
            continue
        elif answer < ran_num:
            print("It's higher")
            attempt += 1
            continue
        elif answer == ran_num:
            attempt += 1
            print("Got it. It took you {} attempts.".format(attempt))
            play_again = input("What to restart? Y/N ")
            if play_again.upper() == "Y":
                if attempt < high_score:
                    high_score = attempt
                    print("---- Highscore is {} ----\n".format(high_score))
                else:
                    print("---- Highscore is {} ----\n".format(high_score))
                attempt = 1
                continue
            else:
                print("Game Over. Bye!")
                game_play = False
                break



if __name__ == '__main__':
    # Kick off the program by calling the start_game function.
    start_game()