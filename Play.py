import random

def play_round():
  """Plays a single round of Rock-Paper-Scissors."""

  player_choice = input("Choose Rock, Paper, or Scissors: ").lower()

  if player_choice not in ["rock", "paper", "scissors"]:
    print("Invalid choice. Please choose Rock, Paper, or Scissors.")
    return

  computer_choice = random.choice(["rock", "paper", "scissors"])

  print(f"You chose {player_choice}.")
  print(f"Computer chose {computer_choice}.")

  if player_choice == computer_choice:
    print("Tie!")
  elif (player_choice == "rock" and computer_choice == "scissors") or \
       (player_choice == "paper" and computer_choice == "rock") or \
       (player_choice == "scissors" and computer_choice == "paper"):
    print("You win!")
  else:
    print("You lose!")

def play_game():
  """Plays multiple rounds of Rock-Paper-Scissors."""

  while True:
    play_round()

    play_again = input("Play again? (y/n): ").lower()

    if play_again != "y":
      break

if __name__ == "__main__":
  play_game()
       

