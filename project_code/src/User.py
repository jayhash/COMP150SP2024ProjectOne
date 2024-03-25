from project_code.src.Game import Game

class User:

    def __init__(self, username: str, password: str, legacy_points: int = 0):
        self.username = username
        self.password = password
        self.legacy_points = legacy_points
        self.current_game = self._get_retrieve_saved_game_state_or_create_new_game()

    def _get_retrieve_saved_game_state_or_create_new_game(self) -> Game:
        # Placeholder method for retrieving saved game state or creating a new game
        new_game = Game()
        return new_game

    def save_game(self):
        # Placeholder method for saving game state
        pass


# Example usage:
if __name__ == "__main__":
    # Creating a new user
    user = User(username="player1", password="password123")

    # Accessing the user's current game
    game = user.current_game

    # Starting the game
    result = game.start_game()
    print(result)  # This will depend on the game logic and how it's implemented

