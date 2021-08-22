import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game_imgs = [rock,paper,scissors]

print(" Welcome to the Game ")

user_choice = int(input(" Enter 0 for rock , 1 for paper and 2 for scissors \n"))

print(game_imgs[user_choice])

computer_choice = random.randint(0,2)

print(f"computer choose :  ")
print(game_imgs[computer_choice])

if user_choice >= 3 or user_choice < 0:
  print("u have entered a invalid number , u lose! ") 
elif user_choice == 0 and computer_choice == 2:
  print("You  Win! ")
elif user_choice == 2 and computer_choice == 0:
  print("You  Lose! ")
elif computer_choice > user_choice:
  print("You lose")
elif user_choice > computer_choice:
  print("You Win !")
elif computer_choice == user_choice:
  print("It's a Draw")
else:
  print(" you typed a invaled Number Loser !")
    
