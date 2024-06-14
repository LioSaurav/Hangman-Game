# import random

# def select_word():
#     word_list = ['apple', 'banana', 'grape', 'orange', 'mango', 'melon']
#     return random.choice(word_list)

# def show_word_progress(word, guessed_chars):
#     return ' '.join(char if char in guessed_chars else '_' for char in word)

# def hangman():
#     word_to_guess = select_word()
#     guessed_characters = set()
#     attempts_remaining = 6

#     print("Welcome to Hangman!")
#     print("Try to guess the word one letter at a time.")
#     print(show_word_progress(word_to_guess, guessed_characters))

#     while attempts_remaining > 0:
#         guess = input("Guess a letter: ").lower()

#         if guess in guessed_characters:
#             print("You have already guessed that letter. Try again.")
#         elif guess in word_to_guess:
#             guessed_characters.add(guess)
#             print("Good guess!")
#         else:
#             guessed_characters.add(guess)
#             attempts_remaining -= 1
#             print(f"Wrong guess! You have {attempts_remaining} attempts left.")

#         current_progress = show_word_progress(word_to_guess, guessed_characters)
#         print(current_progress)

#         if '_' not in current_progress:
#             print("Congratulations! You've guessed the word correctly!")
#             break
#     else:
#         print(f"Game over! The word was '{word_to_guess}'.")

# if __name__ == "__main__":
#     hangman()



import random 
print ("Welcome to Hangama")
print ("---------------------------------------------------")

wordDictionary=["sunflowerr"," house","diamond","memes","yeet","hello","ilend","hello","like"]
# choose a random word 
randomwords= random.choice(wordDictionary)
for x in randomwords:
    print("_" ,end = " ")
def print_Hangama(wrong):
    if(wrong==0):
        print("\n+---+")
        print("    |")
        print("    |")
        print("    |")
        print("    ===")
    elif(wrong ==1):
        print("\n+---+")
        print("    |")
        print("    |")
        print("    |")
        print("    ===")
    elif(wrong ==2):
        print("\n+---+")
        print("o   |")
        print("    |")
        print("    |")
        print("    ===")
    elif(wrong ==3):
         print("\n+---+")
         print("o    |")
         print("|   |")
         print("    |")
         print("    ===")
    elif(wrong ==4):
        print("\n+---+")
        print("o    |")
        print("/|\  |")
        print("     |")
        print("    ===")
    elif(wrong ==5):
        print("\n+---+")
        print("o   |")
        print("/|\ |")
        print("/   |")
        print("   ===")
    elif(wrong ==6): 
        print("\n+---+")
        print("o    |")
        print("/|\  |")
        print("/ \  |")
        print("    ===")
def printword(gussedLetters):
    counter=0
    rightLetter=0
    for char in randomwords:
        if(char in gussedLetters):
            print(randomwords[counter], end=" ")
            rightLetter+=1
        else:
            print(" ",end=" ")
        counter+=1
    return rightLetter
def printLines():
    print("\r")
    for char in randomwords:
        print("\u203E", end="   ")
        
length_of_word_to_guess =len(randomwords)
amount_of_times_wrong =0
current_guess_index=0
current_letters_guessed=[]
current_letters_right=0

while(amount_of_times_wrong != 6 and current_letters_right != length_of_word_to_guess):
    print("\nLetters guessed so far: ")
    for letter in current_letters_guessed:
        print(letter,end=" ")
    # Prompt user for input
    letterGuessed =input("\nGuess a letter: ")
    # IF USER is right 
    if(randomwords[current_guess_index] == letterGuessed):
        print_Hangama(amount_of_times_wrong)
        # print word
        current_guess_index+=1
        current_letters_guessed.append(letterGuessed)
        current_letters_right = printword(current_letters_guessed)
        printLines()
    # user was wrong of
    else:
        amount_of_times_wrong+=1
        current_letters_guessed.append(letterGuessed)
        # update the drawing 
        print_Hangama(amount_of_times_wrong)
        # print word
        current_letters_right = printword(current_letters_guessed)
        printLines()
print("Game is over! Thank you for Playing a Game : ")
        
        
    
    
            
        