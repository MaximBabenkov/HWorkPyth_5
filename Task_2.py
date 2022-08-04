# Создайте программу для игры с конфетами человек против человека.

# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход
# друг после друга. Первый ход определяется жеребьёвкой. За один ход можно
# забрать не более чем 28 конфет. Все конфеты оппонента достаются 
# сделавшему последний ход. Сколько конфет нужно взять первому игроку,
# чтобы забрать все конфеты у своего конкурента?

# a) Добавьте игру против бота

# b) Подумайте как наделить бота "интеллектом"

import random
from random import randint

messages = [', your move:', ', go ahead!', ', forward!',
 ', go on!', ", it's your turn:", ', come on!']

def take_numb(name: str, replicas: str, general_amount: int) -> int:
    while True:
        numb = int(input(f'{name}{random.choice(replicas)}\n'))
        if numb in range(1, 29):
            break
        else:
            print('Your amount of sweets is incorrect. Try again!')        
    return numb

def bot(general_amount: int) -> int:
    if general_amount > 28:
        numb = general_amount % 29
        if numb == 0:   
            numb = randint(1, 28)            
    else:
        numb = general_amount
    return numb

def toss_up() -> int: 
    heads_tails = randint(0, 1)
    return heads_tails


# Игра человек против человека

player_1 = input('Enter the name of the first player:\n')
player_2 = input('Enter the name of the second player:\n')

total_sweets = int(input('Enter the total amount of sweets:\n'))

choice = toss_up()
if choice == 0:
    current_player = player_1
    print(f'{player_1} begins to play')
else:
    current_player = player_2
    print(f'{player_2} begins to play')

while total_sweets > 0:
    winner = current_player
    move = take_numb(current_player, messages, total_sweets)
    total_sweets -= move     
    print(f'The rest of sweets: {total_sweets}')   
    current_player = player_2 if current_player == player_1 else player_1  
winner != current_player   
print(f'No sweets left on the table! {winner} gets all the sweets')       
print(f'{winner} won!\nGame over')               

print('-------------------------------------------------------------------')
  
# Игра против бота

player = input('Please enter the name of the player:\n')
print(f'{player}, you will play with bot!')
total_sweets = int(input('Enter the total amount of sweets:\n'))

choice = toss_up()
if choice == 0:    
    print(f'{player} begins to play')
else:
    print(f'Bot begins to play')    
while total_sweets > 0:
    if choice == 0:
        move = take_numb(player, messages, total_sweets)
        total_sweets -= move
        choice = 1         
        print(f'The rest of sweets: {total_sweets}')
        if total_sweets == 0:
            print(f'No sweets left on the table!\n {player} gets all the sweets')       
            print(f'{player} won!\nGame over')
    else:
        move = bot(total_sweets)    
        print(f'Bot moves:\n', move)           
        total_sweets -= move
        choice = 0
        current_player = player           
        print(f'The rest of sweets: {total_sweets}')
        if total_sweets == 0:
            print(f'No sweets left on the table!\n Bot gets all the sweets')      
            print(f'Bot won!\nGame over')   

