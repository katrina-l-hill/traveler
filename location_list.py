"""Import random module."""
import random


class Travel:
    """Create a new member."""

    def __init__(self, location_list):
        self.location_list = location_list

    def locations(self):
        """Print location list."""
        print(self.location_list)


location_list = [
    "Lisbon",
    "Madrid",
    "Tokyo",
    "Munich",
    "Paris",
    "Auckland",
    "Sydney",
    "Seoul",
    "Göbekli Tepe",
    "Nan Madol",
    "Newgrange",
    "Skellig Islands",
    "Oslo",
    "Brussels",
]

travel = Travel(location_list)
travel.locations()

print(random.choice(location_list))
