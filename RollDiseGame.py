import random

def roll():
    min_value = 1
    max_value = 6
    return random.randint(min_value, max_value)

while True:
    players = input("Enter the number of players from 2 to 4: ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print("Please enter a number from 2 to 4")
    else:
        print("Invalid input. Please try again")

max_score = 50
players_score = [0 for _ in range(players)]

while max(players_score) < max_score:
    for players_idx in range(players):
        current_score = 0
        
        while True:
            should_roll = input("Player {} - Do you want to roll? (y) ".format(players_idx + 1))
            if should_roll.lower() != "y":
                break
            
            value = roll()
            if value == 1:
                print("You rolled a 1. Turn over.")
                current_score = 0
                break
            else:
                current_score += value
                print("You rolled at", value)
                print("Your current score is", current_score)
                players_score[players_idx] += current_score
                print("Your total score is:", players_score[players_idx])
                break

winner = players_score.index(max(players_score)) + 1
print("Player {} wins with a score of {}!".format(winner, max(players_score)))
