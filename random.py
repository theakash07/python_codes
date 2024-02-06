import random

target_num = random.randint(1, 10)
guess_num = 0
print(target_num)
while target_num != guess_num:
    try:
        guess_num = int(input('Guess a number between 1 and 10 until you get it right: '))
    except ValueError:
        print('Invalid input! Please enter a valid number.')
        continue

print('Well guessed!')
#code for number guessing game
