import random


def get_choices():
    player_choice = input("Enter a choice (rock, paper, scissors): ")
    options = ["rock", "paper", "scissors"]
    computer_choice = random.choice(options)
    choices = {"player": player_choice, "computer": computer_choice}
    return choices

def check_win(player, computer):
    print(f"You chose {player}, computer chose {computer}")
    wins = {"rock": "scissors", "paper": "rock", "scissors": "paper"}
    if player == computer:
        return "It's a tie!"
    elif wins[player] == computer:
        return f"You win! {player} beats {computer}"
    else:
        return f"You lose. {computer} beats {player}"

choices = get_choices()
result = check_win(choices["player"], choices["computer"])
print(result)