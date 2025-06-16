import random

def fun_game():
  choices : list[str] = ['r','s','p']
  user_choice : str = input('Rock , paper , scissor ? (r/p/s): ').lower()

  comp_choice : str = random.choice(choices)

  print(f'My choice : {user_choice}')
  print(f'Computer choice : {comp_choice}')


  if(user_choice not in ['r','p','s']):
    print('Invalid Choice')
  elif(user_choice == 'r' and comp_choice == 's'):
    print(f'{user_choice} beats {comp_choice} You win! 🎉')
  elif(user_choice == 's' and comp_choice == 'p'):
    print(f'{user_choice} beats {comp_choice} You win! 🎉')
  elif(user_choice == 'p' and comp_choice == 'r'):
    print('{user_choice} beats {comp_choice} You win! 🎉')
  elif(user_choice == comp_choice):
        print(f'{user_choice} Draw {comp_choice} 😎')
  else :
    print(f'{user_choice} beats {comp_choice} You lose! 😔 ')

fun_game()

