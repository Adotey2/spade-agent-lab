import random


class DisasterEnvironment:
    def __init__(self):
        # Starting conditions
        self.temperature = 25
        self.smoke = 0
        self.damage_level = 1

    def update_environment(self):
        # Random changes to environment
        self.temperature += random.randint(-1, 3)
        self.smoke += random.randint(0, 2)

        if self.smoke < 0:
            self.smoke = 0

        # Increase damage when conditions worsen
        if self.temperature > 40 or self.smoke > 5:
            self.damage_level = min(5, self.damage_level + 1)

    def sense(self):
        return {
            "temperature": self.temperature,
            "smoke_level": self.smoke,
            "damage_severity": self.damage_level
        }
