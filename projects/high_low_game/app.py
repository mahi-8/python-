import random

my_number : int = random.randint(0,99)

print('Guess My Number')

# It is better approach , we use try-except :
while True :
  guessed_number : int = int(input("I am thinking of a number between 0 and 99... 🤔 Enter a guess:  "))

  if guessed_number > my_number :
    print(f'Your guess is too high 🤦‍♀️')
  elif guessed_number < my_number :
    print(f'Your guess is too low 😮')
  else :
    print(f'Congrats! The number was {my_number} 😎')
    break