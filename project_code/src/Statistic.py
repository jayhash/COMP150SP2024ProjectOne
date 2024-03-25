import random

class Statistic:
    def __init__(self, legacy_points: int):
        self.value = self._generate_starting_value(legacy_points)
        self.description = None
        self.min_value = 0
        self.max_value = 100

    def __str__(self):
        return f"{self.value}"

    def increase(self, amount):
        self.value += amount
        if self.value > self.max_value:
            self.value = self.max_value

    def decrease(self, amount):
        self.value -= amount
        if self.value < self.min_value:
            self.value = self.min_value

    def _generate_starting_value(self, legacy_points: int):
        """Generate a starting value for the statistic based on random number and user properties."""
        """This is just a placeholder for now. Perhaps some statistics will be based on user properties, and others 
        will be random."""
        return legacy_points / 100 + random.randint(1, 3)


class Strength(Statistic):

    def __init__(self, legacy_points: int):
        super().__init__(legacy_points)
        self.description = "Strength is a measure of physical power."

# and so on for the other statistics

# Example usage:
if __name__ == "__main__":
    # Create a Strength statistic for a character
    strength_stat = Strength(legacy_points=150)  # Example legacy points

    # Print the initial value and description of Strength
    print("Initial Strength Value:", strength_stat)
    print("Strength Description:", strength_stat.description)

    # Increase the Strength value by 10
    strength_stat.increase(10)
    print("Increased Strength Value:", strength_stat)

    # Decrease the Strength value by 5
    strength_stat.decrease(5)
    print("Decreased Strength Value:", strength_stat)
