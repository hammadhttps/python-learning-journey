import random


def player_num():
    while True:
     players=input("Enter the number of players: ")
     if players.isdigit():
        players=int(players)
        if 2<=players<=4:
            return players
        else:
            print("Must be between 2 and 4 players.")
     else:
        print("Invalid input. Please enter a number.")

def roll_dice():
     print("Rolling the dice...")
     return random.randint(1,6)

max_score=50
player_scores=[0 for _ in range(player_num())]

while max(player_scores)<max_score:
    for player_idx, player_score in enumerate(player_scores):
        print(f"\nPlayer {player_idx + 1}'s turn has just started!")
        print(f"Your total score is: {player_score}\n")
        current_score=0
        while True:
            should_roll=input("Would you like to roll (y/n)? ")
            if should_roll.lower()!="y":
                break
            value=roll_dice()
            if value==1:
                print("You rolled a 1! Turn done!")
                current_score=0
                break
            else:
                current_score+=value
                print(f"You rolled a {value}! Current score: {current_score}")
        player_scores[player_idx]+=current_score
        print(f"Your total score is: {player_scores[player_idx]}")
    winner=player_scores.index(max(player_scores))+1
    print(f"Player {winner} has won the game!")
    break





