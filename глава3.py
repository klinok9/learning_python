import random

#
# # 0- камень, 1- бумага 2- ножницы
# random_choice = random.randint(0, 2)
# if random_choice == 0:
#     computer_choice = "камень"
# elif random_choice == 1:
#     computer_choice = "бумага"
# else:
#     computer_choice = "ножницы"
# player_choice = input("камень, ножницы, бумага? ")
# print(computer_choice, player_choice)
# if random_choice == 0 and player_choice == 0:
#     print("ничья")
# elif random_choice
winner = ''
player_choice = input('введи: камень, ножницы или бумага: ')
choices = ['камень', 'ножницы', 'бумага']
computer_choice = random.choice(choices) # знакомство с функцией random.choice
if computer_choice == player_choice:
    winner = 'ничья!'

elif computer_choice == "бумага" and player_choice == 'камень':
    winner = 'комп'
elif computer_choice == "камень" and player_choice == 'ножницы':
    winner = 'комп'
elif computer_choice == "ножницы" and player_choice == 'бумага':
    winner = 'комп'
else:
    winner = 'ты'
if winner == 'ничья!':
    print('победила дружба')
else:
    print('Победил' , winner)

