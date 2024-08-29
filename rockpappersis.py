import random
choices=['rock','paper','scissors']
computer_choice=random.choice(choices)
player_choice=input("Choose:rock,paper,scissors:")

if player_choice in choices:
    if player_choice==computer_choice:
        print("It is a Tie!")
    elif(
        (player_choice=='rock'and computer_choice=='scissors') or
        (player_choice=='paper'and computer_choice=='rock') or 
        (player_choice=='scissors'and computer_choice=='paper')
    ):
        print('You Win!')
    else:
        print('Computer wins!')
else:
    print('Invalid Choice.')