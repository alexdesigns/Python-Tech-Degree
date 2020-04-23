# Create your Character class logic in here.
# help a Phrase determine how an individual character should display itself.
class Character:
    def __init__(self, char, guess_try = False):
        self.char = char
        self.guess_try = guess_try

    def show_letter(self):
        if self.guess_try:
            return self.char
        elif self.char == " ":
            return " "
        else:
            return "_"

    def user_entry(self, guess_letter):
        if self.char.upper() == guess_letter.upper():
            self.change_guess()
            return True
        else:
            return False

    def change_guess(self):
        self.guess_try = True
    

