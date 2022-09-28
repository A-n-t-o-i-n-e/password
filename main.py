# import of lists
from string import (
    ascii_letters,
    ascii_lowercase,
    ascii_uppercase,
    digits,
    punctuation,
    whitespace
)
from random import (
    randint,
    choice
)


class Password:
    def __init__(
        self, password = 'password', 
        minimum_number_character = 7,
        maximum_number_character = 12,
        obligatory_lowercase = False,
        obligatory_uppercase = False,
        obligatory_number = False,
        obligatory_punctuation = False
        ):

        # var
        self.password = password
        self.minimum_number_character = minimum_number_character
        self.maximum_number_character = maximum_number_character
        self.obligatory_lowercase = obligatory_lowercase
        self.obligatory_uppercase = obligatory_uppercase
        self.obligatory_number = obligatory_number
        self.obligatory_punctuation = obligatory_punctuation
        

        # fix
        self.list_letters = ascii_letters
        self.list_lowercase = ascii_lowercase
        self.list_uppercase = ascii_uppercase
        self.list_number = digits
        self.list_punctuation = punctuation
        self.list_space = whitespace
  

    def GetPassword(self):
        return self.password


    def GetStrings(self):
        return  (self.list_lowercase,
        self.list_uppercase,
        self.list_number,
        self.list_punctuation,
        self.list_space
        )


    def GetConditions(self):
        return (self.minimum_number_character,
        self.maximum_number_character,
        self.obligatory_lowercase,
        self.obligatory_uppercase,
        self.obligatory_number,
        self.obligatory_punctuation
        )


    def RankPassword():
        pass


    def RespectCondition(self, password):
         # variable declaratiopn : number of uppercase, lowercase, number, and punctuation
        lc , uc, dg, pt = 0, 0, 0, 0


        # checks that the number of characters is between min and max
        if len(password) < self.minimum_number_character or len(password) > self.maximum_number_character:
            return False

        # does as many loops as there are letters in the password
        for i in range(len(password)):

            # checks that the n th character isn't a space
            if password[i] in whitespace:
                return False
                
            # checks that the n th character is a lowercase
            elif password[i] in ascii_lowercase:
                lc += 1

            # checks that the n th character is an uppercase
            elif password[i] in ascii_uppercase:
                uc += 1
            
            # checks that the n th character is a number
            elif password[i] in digits:
                dg += 1

            # checks that the n th character is a punctuation
            elif password[i] in punctuation:
                pt += 1

            else:
                return False

        #checks if the 4 previous conditions are respected
        if lc == 0 and self.obligatory_lowercase == True:
            return False
        elif uc == 0 and self.obligatory_uppercase == True:
            return False
        elif dg == 0 and self.obligatory_number == True:
            return False
        elif pt == 0 and self.obligatory_punctuation == True:
            return False

        # all is fine
        else:
            return True


    def SuggestPassword(self):
        password = ''
        characters = [*ascii_letters, *digits, *punctuation]
        password = [
            choice(characters) for i in range(
                randint(
                    self.minimum_number_character,
                    self.maximum_number_character
                    )
                )
            ]
        return ''.join(password)

