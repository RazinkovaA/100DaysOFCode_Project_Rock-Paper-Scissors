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
player_choose = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n"))
print(hand_signals[player_choose])

comp_choose = random.randint(0, 2)
print(hand_signals[comp_choose])

if player_choose == 0 and comp_choose == 2:
  print("You win!")
elif player_choose == 2 and comp_choose == 1:
  print("You win!")
elif player_choose == 1 and comp_choose == 0:
  print("You win!")
elif player_choose == comp_choose:
  print("It's a drawn")
else:
  print("You loose")    
# if player_choose == 0 and comp_choose == 0:
#   print("It's a drawn")
# elif player_choose == 0 and comp_choose == 2:
#   print("You win")
# else:
#   print("You loose")

# if player_choose == 1 and comp_choose == 1:
#   print("It's a drawn")
# elif player_choose ==   

    



