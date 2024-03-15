import random
import hangman_words
import hangman_art

def mask(word):
    """Create a masked version of the word to be guessed.

    Args:
        word (str): The word that needs to be guessed.

    Returns:
        dict: A dictionary with keys representing letters in the word
              and values representing underscores or spaces.
    """
    
    dictionary = {}
    
    for char in word:
        
        if char.isalpha():
            dictionary.update({char: "_ "})
            
        elif char.isspace():
            dictionary.update({char: "  "})
            
        else:
            dictionary.update({char: f"{char} "})
            
    return dictionary


def unmask(masked_word, user_guess, mistakes):
    """Unmask a letter in the word based on user input.

    Args:
        masked_word (dict): The masked version of the word.
        user_guess (str, optional): The letter guessed by the player.
        mistakes (int): The number of incorrect guesses.

    Returns:
        dict: The updated dictionary with unmasked letters.
    """
    
    while True:
        
        # Reveals the entire word if the player has made 7 mistakes, indicating game over.
        if mistakes == 7:
            keys = list(masked_word.keys())
            
            for key in keys:
                masked_word.update({key: f"{key} "})
                
            return masked_word
        
        # Reveals a correctly guessed letter in the word.
        elif user_guess.lower() in list(masked_word.keys()):
            key = user_guess.lower()
            masked_word.update({key: f"{key} "})
            return masked_word
        
        # Returns the dictionary unchanged.
        else:
            return masked_word
        
        
def play_again():
    """Prompt the user to play again or exit the game.

    Returns:
        str: The user's choice to play again or exit.
    """
    
    while True:
        user_input = input("Would you like to try again? (y/n): ").lower()
        
        if user_input not in ["y", "n", "exit"]:
            print("Invalid input. Type in \"y\" to play again, or \"n\" or \"exit\" to stop playing.")
            continue
        return user_input


def main():
    """
    Orchestrates the main gameplay loop for the Hangman game.

    Prints the game's title, selects a word for the player to guess,
    initializes the masked word and lists for incorrect guesses, and
    manages the progression of the game until the player wins or loses.
    After each game, prompts the user whether to play again or exit.

    Returns:
        bool: False if the user chooses to exit, otherwise restarts the game.
    """
    print(hangman_art.title)
    
    while True:
        word = random.choice(hangman_words.words)
        masked_word = mask(word)
        incorrect_guesses = []
        mistakes = 0
        
        # Print initial game progress
        print(hangman_art.stages[0])
        
        for char in word:
            print(f"{masked_word.get(char)}", end="")
                
        print()
        
        # Main game loop
        while "_ " in list(masked_word.values()):
            already_guessed = False
            guess = input("\n")
            
            # Validate user input
            if not guess.isalpha() or len(guess) != 1:
                print("Invalid input! Type in a single letter.")
                continue
            
            elif guess.lower() not in list(masked_word.keys()):
                
                if guess not in incorrect_guesses:
                    incorrect_guesses.append(guess)
                    
                mistakes += 1
            
            if f"{guess} " in list(masked_word.values()):
                already_guessed = True
                    
            masked_word = unmask(masked_word, guess, mistakes)
            
            # Print game progress
            print(hangman_art.stages[mistakes])
            
            for char in word:
                print(f"{masked_word.get(char)}", end="")
                    
            print()
            
            if incorrect_guesses:
                # Print incorrect guesses if there are any
                print("Incorrect guesses: ", end="")
                
                for char in incorrect_guesses:
                    print(f"{char} ", end="")
                print()
                
            if already_guessed:
                # Print if guessed letter is already unmasked
                print(f"You have already correctly guessed '{guess}'!")
            
            if mistakes == 7:
                # User has 7 attempts to guess the word
                print(hangman_art.loss)
                choice = play_again()
                
                if choice == "y":
                    pass
                
                else:
                    return False
        
        if mistakes < 7:
            print(hangman_art.win)
            choice = play_again()

            if choice == "y":
                pass
            
            else:
                return False
        

if __name__ == "__main__":
    main()
