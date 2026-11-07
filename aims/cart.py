"""Shopping-cart operations for the AIMS command-line demo."""
MAX_NUMBERS_ORDERED = 20


class Cart:
    def __init__(self):
        self.items = []

    def add_digital_video_disc(self, dvd):
        if len(self.items) > MAX_NUMBERS_ORDERED:
            return False
        self.items.append(dvd)
        print("The disc has been added")
        return True

    def remove_digital_video_disc(self, dvd):
        try:
            self.items.remove(dvd)
        except ValueError:
            return False
        return True

    def total_cost(self):
        return round(sum(dvd.cost for dvd in self.items), 2)
