import random

items = ["Rock", "Paper", "Scissors"]
begin = input("Rock\nPaper\nScissors \nChoose from the above: ")
bot_action = random.choice(items)

if begin == ("Rock"):
  print(bot_action)
  if bot_action == ("Paper"):
    print("You lost!")
  elif bot_action == ("Scissors"):
    print("You won!")
  elif bot_action == ("Rock"):
    print("Tie")

if begin == ("Scissors"):
  print(bot_action)
  if bot_action == ("Rock"):
    print("You lost!")
  elif bot_action == ("Paper"):
    print("You won!")
  elif bot_action == ("Scissors"):
   print("Tie")

if begin == ("Paper"):
  print(bot_action)
  if bot_action == ("Scissors"):
    print("You lose!")
  elif bot_action == ("Rock"):
    print("You won!")
  elif bot_action == ("Paper"):
    print("Tie")

