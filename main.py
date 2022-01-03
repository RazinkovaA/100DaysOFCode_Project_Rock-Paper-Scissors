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

#Write your code below this line 👇
import random

hand_signals = [rock, paper, scissors]
player_choise = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n"))
print(hand_signals[player_choise])

comp_choise = random.randint(0, 2)
print(f"Computer choose {hand_signals[comp_choise]}")

if player_choise == 0 and comp_choise == 2:
  print("You win!")
elif player_choise == 2 and comp_choise == 1:
  print("You win!")
elif player_choise == 1 and comp_choise == 0:
  print("You win!")
elif player_choise == comp_choise:
  print("It's a drawn")
else:
  print("You loose")    

 

    



