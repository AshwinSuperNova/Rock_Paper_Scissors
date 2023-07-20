import random
choices1=["rock","paper","scissors"]
def get_choices(choices):
  
  player=input("Enter the choices 1 : rock 2 : paper 3 : scissors : ")
  computer=random.choice(choices)
  dict={
    "player":player,"computer":computer
  }
  return dict


def check_win(player,computer):
  print(f"the player chosen [{player}] ,and the computer chosen [{computer}]")
  if player==computer:
    print("oops! both players are in tie")
  elif player=="rock"  :
    if computer=="paper":
      print("paper covers rock! you lose 😓")
    else:
      print("rock smashes scissors you win 😁")
  elif player=="paper"  :
    if computer=="scissors":
      print("scissors cuts paper! you lose 😓")
    else:
      print("paper covers rock! you win 😁")  
  elif player=="scissors"  :
    if computer=="paper":
      print("scissors cuts paper! you win 😁")
    else:
      print("rock smashes scissors  you lose 😓")    


choices=get_choices(choices1)
check_win(choices["player"],choices["computer"])
  
  
  
