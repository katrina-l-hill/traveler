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
    "Lisbon, Portugal",
    "Madrid, Spain",
    "Tokyo, Japan",
    "Munich, Germany",
    "Paris, France",
    "Auckland, New Zealand",
    "Sydney, Australia",
    "Seoul, South Korea",
    "Göbekli Tepe",
    "Nan Madol, Micronesia",
    "Newgrange, Ireland",
    "Skellig Islands, Ireland",
    "Oslo, Norway",
    "Brussels, Belgium",
]

travel = Travel(location_list)
travel.locations()

# print(random.choice(location_list))
