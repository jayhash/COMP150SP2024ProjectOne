from typing import List

from project_code.src.Character import Character
from project_code.src.Event import Event
from project_code.src.Location import Location

class Game:
    def __init__(self):
        self.characters: List[Character] = []
        self.locations: List[Location] = []
        self.events: List[Event] = []
        self.party: List[Character] = []
        self.current_location = None
        self.current_event = None
        self.continue_playing = True
        self._initialize_game()

    def add_character(self, character: Character):
        """Add a character to the game."""
        self.characters.append(character)

    def add_location(self, location: Location):
        """Add a location to the game."""
        self.locations.append(location)

    def add_event(self, event: Event):
        """Add an event to the game."""
        self.events.append(event)

    def _initialize_game(self):
        """Initialize the game with characters, locations, and events."""
        # Example initialization
        self.add_character(Character("Warrior"))
        self.add_character(Character("Mage"))
        self.add_location(Location("Forest", "A dense brush forest with towering dry paint brushes."))
        self.add_location(Location("Cave", "A dark clay cave with jagged clay spikes."))
        self.add_event(Event("Monster Encounter", "You encounter a group of paint globs!"))

    def start_game(self):
        return self._main_game_loop()

    def _main_game_loop(self):
        """The main game loop."""
        while self.continue_playing:
            self.current_location = self.locations[0]  # Example: Set the current location to the first one
            self.current_location.describe()
            self.current_location.explore()  # Example: Explore the current location
            # Additional game logic can go here
            self.continue_playing = False  # For the sake of the example, we'll end the game loop
        return "Game Over"

# Example usage
game = Game()
result = game.start_game()
print(result)  # This should print "Game Over"








