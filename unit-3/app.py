# Import your Game class
from phrasehunter.game import Game


# Create your Dunder Main statement.
if __name__ == '__main__': 
   
    phrase = ("Hello")

    # Inside Dunder Main:
    ## Create an instance of your Game class
    main_game = Game(phrase)

    ## Start your game by calling the instance method that starts the game loop
    main_game.call_game()


