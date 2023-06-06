import random

i = 0
options = ['Gun', 'Snake', 'Water']

while i < 10:
    computer_choice = random.choice(options)
    user_input = input('(Snake, Gun, Water) choose: ')
    
    if computer_choice == user_input:
        print('Tie, computer has chosen', computer_choice)
    elif computer_choice == 'Snake' and user_input == 'Water':
        print('You lost, computer has chosen', computer_choice)
    elif computer_choice == 'Gun' and user_input == 'Snake':
        print('You lost, computer has chosen', computer_choice)
    elif computer_choice == 'Water' and user_input == 'Gun':
        print('You lost, computer has chosen', computer_choice)           
    else:
        print('You win, computer has chosen', computer_choice)
    
    i = i + 1
    print('\n')
