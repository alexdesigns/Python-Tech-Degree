#methods for starting game, handling interactions, getting a random phrase, 
#checking for a win/loss state, and removing "lives" 
import time

# Import your Phrase class
from phrasehunter.phrase import Phrase

# Create your Game class logic in here.
class Game:
    def __init__(self, phrase):
        self.guessed_list = []
        self.phrases = phrase
        self.phrase_answer = Phrase(self.phrases)
    
    # method for display characters for guess phrase
    def call_phrase_letters(self):
        letters_list = self.phrase_answer.return_letters()
        letters_string = " ".join(letters_list)
        print(letters_string)
    
    #determine if char choose already
    def eval_char(self, guess_input):
        if str(guess_input) in self.guessed_list:
            return True
        else:
            self.guessed_list.append(str(guess_input))
            return False

    #restart method
    def restart_game(self, phrase):
        time.sleep(.5)
        restart_input = input("Try again? Enter Y: ")
        if restart_input.upper() == "Y":
            main_game = Game(phrase)
            main_game.call_game()
        else:
            print("Thanks for playing!")
            quit()

        return main_game

    #starting game
    def call_game(self):
        #print(phrase)
        lives_left = 5
        guess_attempt = False

        #intro game:
        print("\n")
        print("Welcome to Phrase Hunters:")
        time.sleep(.5)
        print("\n")
        self.call_phrase_letters()

        game_play = True
        while game_play:
            
            try:
                if guess_attempt == False:
                    print("\n")
                    print("Guess a letter to match phrase. Choose q to quit.")
                    print("\n")

                time.sleep(.5)  
                guess_input = input("Enter letter: ")
                
            except:
                lives_left -= 1
                print("ERROR: Enter only letters")
                continue
            """else:
                print("BYPASS")
                pass"""
            if guess_input == 'q':
                print("\nGoodbye...")
                quit()
            elif guess_input == self.eval_char(guess_input):
                lives_left -= 1
                print(">> ERROR: You already choose that letter. Try again")
                continue
            elif len(guess_input) > 1:
                print(">>> ERROR: Enter only 1 letter")
                continue
            else:
                guess_attempt = True

                user_entry = self.phrase_answer.eval_guess(guess_input)    
                print("-" * 60)
                #Evalauate the phrase and show lives left
                if user_entry:
                    #correct answers 
                    print("\n")
                    self.call_phrase_letters()
                    print("\n")

                    if self.phrase_answer.eval_phrase():
                        print("Congrats! You won.")
                        self.restart_game(self.phrases)
                    else:
                        print("That's right. Keep going!")
                        continue
                
                #Incorrect answers
                else:
                    if lives_left > 1:
                        lives_left -= 1
                        print(">>> SORRY! That was incorrect. ")
                    else:
                        print("GAME OVER!")
                        self.restart_game(self.phrases)

                print("\nYou have {} lives remaining. Try again...".format(lives_left)) 
                print("\n")

        self.call_phrase_letters()
        print("\n")
             


    

