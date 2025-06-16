import random
def rolling_dice():

  while (True):
    choice_input : str = (input('Roll the dice ? (y/n) ')).lower()
    if (choice_input not in ['y','n',]):
        print(f'Invalid Choice!')
    elif (choice_input == 'y'):
       generate_item1 = random.randint(1,5)
       generate_item2 = random.randint(1,10)
       print(f'{generate_item1 , generate_item2 }')
    else :
          print(f'Thanks for playing!')
          break


rolling_dice()

