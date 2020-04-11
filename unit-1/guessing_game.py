import random
import time

print("-" * 20)
print(" Welcome to the Number Guessing Game!")
print("-" * 20)

all_scores = [99]

def highscore():
    return min(all_scores)

def start_game():
    #default values
    ran_num = random.randint(1, 10)
    stage = 1
    attempt = 1
    high_score = highscore()
    
    #Step: 1 - Collect Name
    time.sleep(.5)
    user_name = input("\nWhat is your name? ")
    time.sleep(.1)
    print("\nWelcome {}".format(user_name.capitalize()))
    time.sleep(.5)
    print("-" * 20)
    print("Begin Round: {}".format(stage))
    print("-" * 20, "\n")

    game_play = True
    while game_play:

        #Step: 2 - Choose Number
        answer = input("ATTEMPT #{}: Pick a number between 1 - 10: ".format(attempt))

        try:
            answer = int(answer)
        except ValueError:
            attempt += 1
            print ("ERROR: ENTER 1-10")
            continue
        else:
            if answer < 1 or answer > 10:
                attempt += 1
                print("\nERROR - NOT IN RANGE\n")
                continue
            elif answer > ran_num:
                attempt += 1
                print("\nTry Again - It's Lower\n")
                continue
            elif answer < ran_num:
                print("\nTry Again - It's Higher\n")
                attempt += 1
                continue
            elif answer == ran_num:
                all_scores.append(attempt)
                print("\n","-" * 40)
                print(" CORRECT. It took you {} attempts.".format(attempt))
                print("", "-" * 40)
                if attempt < high_score:
                    high_score = attempt
                    if stage != 1:
                        print("\n---- Congratulations New Highscore: {} Attempts ----\n".format(high_score))
                
                time.sleep(.5)   
                stage += 1

                play_again = ""                       
                while play_again != "N":
                    play_again = input("\nWhat to try again? Y/N: ")

                    if play_again.upper() == "Y":
                        print("-" * 40)
                        print("Begin Round: {} | Current Highscore: {}".format(stage, high_score))
                        print("-" * 40, "\n")
                        #print("Attempt: {} High Score: {} Stage: {} Scores: {}" .format(attempt,high_score, stage,all_scores))
                        attempt = 1
                        ran_num = random.randint(1, 10)                    
                        break
                    elif play_again.upper() == "N":
                        print("-" * 40)
                        print("Game Over. Bye!")
                        print("-" * 40)
                        game_play = False
                        break
                    else:
                        print("Enter Y or N")
                        continue


if __name__ == '__main__':
    # Kick off the program by calling the start_game function.
    start_game()