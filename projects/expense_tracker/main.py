# Expense Tracker Project

# lists of dictionary 

expenses = []

print('====== Welcome to the Expense Tracker ======')

try :
  while True :
    print('=== Menu ===')
    print('1. Add Expense ')
    print('2. View All Expenses')
    print('3. View Total Expense')
    print('4. Exit')

    choice = int(input('Enter your choice :'))

  # 1- Add Expense
    if(choice == 1):
      date = input('Please enter the date : ')
      category = input('Please enter the category (food , health , clothes , cosmetics , Study) :')
      description = input('Add some detail ...')
      amount = float(input('Enter the total amount : '))
    
      expense = {
          "date" : date ,
          "category" : category ,
          "description" : description ,
          "amount" : amount
      }

      expenses.append(expense)
      print(f'Expense is added sucessfully ...')

  # 2- View All Expenses 
    elif(choice == 2):
      if( len(expenses) == 0 ):
            print('No Expense Added . Empty Cart')
      else:
            print(' ===== Your Expenses ===== ')
            count = 1 
            for total_expense in expenses:
              print(f'{count} : {total_expense["date"]} ') 
              print(f'{total_expense["category"]}')
              print(f' {total_expense["description"]} ')
              print(f' {total_expense["amount"]} ')
              count = count + 1

  # 3- View Total Expense 
    elif(choice == 3 ):
      total = 0 
      for total_spending in expenses:
        total = total + total_spending["amount"]
      print(f'Total : {total}')

  # 4- Exit
    elif(choice == 4):
      print('Thankyou')
      break

    else :
      print('Invalid Number')

except ValueError:
        print('Invalid input! Please enter a number where required.')
except Exception as e:
        print(f'An unexpected error occurred: {e}')