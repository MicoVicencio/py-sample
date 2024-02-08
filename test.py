import random
player_name=[]
player_num = 0
player_score = []

def p_verification(player_choice):
    if player_choice == 1:
      print("You Chosen Rock")
    elif player_choice == 2:
      print("you Chosen Paper")
    elif player_choice == 3:
      print("You Chosen Scissor")

def e_verification(enemy_choice):
    if enemy_choice == 1:
      print("Enemy Chosen Rock")
    elif enemy_choice == 2:
      print("Enemy Chosen Paper")
    elif enemy_choice == 3:
      print("Enemy Chosen Scissor") 

def choice_check(player_choice, enemy_choice):
   if player_choice == 1:
     if enemy_choice == 1:
       return "Draw! Both are Rock!"
     elif enemy_choice == 2:
       return "Player lose! Paper beat Rock!"
     elif enemy_choice == 3:
       return "Player Win! Rock beat Scissor"
       
   elif player_choice == 2:
     if enemy_choice == 1:
       return "Player Win! Paper beat Rock!"
     elif enemy_choice == 2:
       return "Draw! Both are Paper!"
     elif enemy_choice == 3:
       return "Player lose! Scissor beat Paper!"
       
   elif player_choice == 3:
     if enemy_choice == 1:
       return "Player Lose! Rock beat Scissor"
     elif enemy_choice == 2:
       return "Player Win! Scissor beat Paper"
     elif enemy_choice == 3:
      return "Draw! Both are Scissor"
   
   
      
def main():
  playerlives = 1
  game_round = 1
  x = input("Enter your Name:")
  player_name.append(x)
  print("Round numer " + str(game_round))
  print("Welcome " + player_name[player_num] + "!")
  print("Choose your Choice:")
  print("1.Rock")
  print("2.Paper")
  print("3.Scissor")
  player_choice = int(input("Choice:"))
  enemy_choice = random.randint(1,3)
  p_verification(player_choice)
  e_verification(enemy_choice)
  print("The Result of the battle is: " + choice_check(player_choice, enemy_choice))
  
  
  
print("Welcome to Rock, Paper and Scissor Game!")
main()


  


      




  
  
  
  
  
