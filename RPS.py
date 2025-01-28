print("Welcome to the Rock, Paper, Scissors Game!")

player1 = input("Please enter first player's name: ")
player2 = input("Please enter second player's name: ")

choices = ["rock", "paper", "scissors"]

score = {player1: 0, player2: 0}

def decide_winner(choice1, choice2):
    beats = {"rock": "scissors", "scissors": "paper", "paper": "rock"}
    
    if choice1 == choice2:
        return "draw"
    elif beats[choice1] == choice2:
        return player1
    else:
        return player2

def get_choice(player):
    choice = ""
    while choice not in choices:
        choice = input(f"{player}, choose (rock/paper/scissors): ").lower()
    return choice

for game in range(3):
    p1_choice = get_choice(player1)
    p2_choice = get_choice(player2)
    
    winner = decide_winner(p1_choice, p2_choice)
    
    if winner != "draw":
        score[winner] += 1

    print(f"Score after game {game+1} is "
      f"{player1}: {score[player1]} - "
      f"{player2}: {score[player2]}")


    if score[player1] == 2 or score[player2] == 2:
        break

if score[player1] == score[player2]:
    print("The game is a draw!")
elif score[player1] > score[player2]:
    print(f"{player1} wins!")
else:
    print(f"{player2} wins!")
    
print("Thank you for playing!") 