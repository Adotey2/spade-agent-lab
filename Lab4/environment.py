import random

class DisasterEnvironment:
    """
    Simulated disaster environment.
    Generates changing sensor values.
    """

    def __init__(self):
        self.temperature = 25
        self.smoke_level = 1
        self.damage_severity = 1

    def update(self):
        """
        Randomly change values to simulate a dynamic environment.
        """

        # Increase or decrease temperature
        self.temperature += random.randint(-1, 3)

        # Smoke slowly rises
        self.smoke_level += random.randint(0, 2)

        # Damage can worsen
        self.damage_severity += random.choice([0, 0, 1])

        # Clamp values (keep reasonable)
        self.temperature = max(20, min(self.temperature, 80))
        self.smoke_level = max(0, min(self.smoke_level, 10))
        self.damage_severity = max(1, min(self.damage_severity, 5))

    def get_state(self):
        """
        Return current percepts.
        """

        return {
            "temperature": self.temperature,
            "smoke_level": self.smoke_level,
            "damage_severity": self.damage_severity
        }
