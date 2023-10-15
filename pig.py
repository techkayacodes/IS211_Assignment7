import random
import sys

# The Die class represents a die with the ability to roll and return a value between 1 and 6.
class Die:
    def __init__(self):
        # Initialize the die with a random value
        self.value = random.randint(1, 6)

    def roll(self):
        # Roll the die to get a new random value
        self.value = random.randint(1, 6)
        return self.value

# The Player class represents a player in the game, with methods to manage the player's turn.
class Player:
    def __init__(self, name, is_human=True):
        self.name = name
        self.is_human = is_human  # Indicates whether the player is human
        self.turn_total = 0  # Points accumulated in the current turn
        self.total_score = 0  # Total points accumulated throughout the game

    def take_turn(self):
        # Reset the turn total at the beginning of the turn
        self.turn_total = 0
        while True:
            # If the player is human, ask for their choice; otherwise, the computer makes a choice.
            if self.is_human:
                choice = input(f"{self.name}, would you like to roll or hold? (r/h): ")
            else:
                # Basic strategy for computer: roll until it has at least 20 points, then hold.
                choice = 'r' if self.turn_total < 20 else 'h'
                print(f"Computer chooses to {'roll' if choice == 'r' else 'hold'}.")

            if choice == 'r':
                roll = Die().roll()  # Roll the die
                print(f"{self.name} rolled a {roll}")
                if roll == 1:
                    self.turn_total = 0  # If a 1 is rolled, the player scores nothing
                    print("No points added, your turn is over.")
                    break
                else:
                    self.turn_total += roll  # Add roll to turn total
                    print(f"Turn total is {self.turn_total} and total score is {self.total_score}")
            elif choice == 'h':
                self.total_score += self.turn_total  # Add turn total to the overall score
                print(f"{self.name} holds. Total score is {self.total_score}")
                break
            else:
                print("Invalid choice. Please enter 'r' to roll or 'h' to hold.")

# The PigGame class manages the game flow, players, and determines when the game ends.
class PigGame:
    def __init__(self, num_players=2, num_computers=1):
        # Initialize human players
        self.players = [Player(f"Player {i+1}") for i in range(num_players)]
        # Initialize computer players
        self.computers = [Player(f"Computer {i+1}", is_human=False) for i in range(num_computers)]
        # Combine all players
        self.all_players = self.players + self.computers
        self.current_player = None  # Track the current player

    def next_player(self):
        # Move to the next player for their turn
        if self.current_player is None:
            self.current_player = self.all_players[0]
        else:
            current_index = self.all_players.index(self.current_player)
            if current_index < len(self.all_players) - 1:
                self.current_player = self.all_players[current_index + 1]
            else:
                self.current_player = self.all_players[0]  # Loop back to the first player

    def play_game(self):
        print("Pig Game Starting!")
        # Continue the game until a player reaches 100 or more points
        while all(player.total_score < 100 for player in self.all_players):
            self.next_player()  # Change to the next player
            print(f"It's {self.current_player.name}'s turn.")
            self.current_player.take_turn()  # Execute the current player's turn

        # Determine the winner with the highest score
        winner = max(self.all_players, key=lambda player: player.total_score)
        print(f"{winner.name} wins with a score of {winner.total_score}!")

# Main execution
if __name__ == "__main__":
    random.seed(0)  # Set the seed for random operations
    num_players = 1  # Default number of human players
    num_computers = 1  # Default number of computer players

    # Check for command-line argument specifying the number of human players
    if len(sys.argv) > 1 and sys.argv[1].startswith("--numPlayers"):
        try:
            num_players = int(sys.argv[1].split('=')[1])  # Parse the number from the argument
        except (IndexError, ValueError):
            print("Invalid number of players. Defaulting to 1 human player.")

    # Initialize and play the game
    game = PigGame(num_players, num_computers)
    game.play_game()
