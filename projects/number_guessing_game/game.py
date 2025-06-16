import random

def number_guessing_game() :
  comp_guessed_number : int = random.randint(1,100)
  while True:
       try :
           user_guessed_number : str = int(input("Guess the number between 1 and 100 :"))
           if(user_guessed_number > comp_guessed_number ):
                  print('Too high')
           elif(user_guessed_number < comp_guessed_number):
                  print('Too low')
           else :
              print('Congratulations! You guessed the number 😎')
              break
       except ValueError :
           print(f'Enter a valid number  😔')

number_guessing_game()