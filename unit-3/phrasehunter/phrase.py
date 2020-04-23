# to create a Phrase class to handle the creation of phrases.

# Create your Phrase class logic here.
from phrasehunter.character import Character

class Phrase:
    
    def __init__(self, phrase):
        self.phrase = phrase
        #create word into list of letters
        list_of_letters = list(self.phrase)
        #recieve letters and create list
        self.letter_list = []
        for letter in list_of_letters:
            self.letter_list.append(Character(letter))

    def eval_guess(self, guess_input):
        eval_guess_num = False
        eval_guess_val = False
        for character in self.letter_list:
            eval_guess_num = character.user_entry(guess_input)
            if eval_guess_num:
                eval_guess_val = True
            else:
                continue
        return eval_guess_val
    
    def return_letters(self):
        return_list = []
        for letters in self.letter_list:
            return_list.append(letters.show_letter())
        return return_list
    
    def eval_phrase(self):
        word_list = []
        for letter in self.letter_list:
            word_list.append(letter.show_letter())
        return "_" not in word_list

