class Country:

    def __init__(self):
        self.name = ''
        self.x_min, self.y_min, self.x_max, self.y_max = None, None, None, None
        self.MAX_SIZE = 10
        self.MIN_SIZE = 0

    @staticmethod
    def is_in_interval(min_value, value, max_value):
        if min_value and min_value > value:
            raise ValueError
        if max_value and max_value < value:
            raise ValueError
        return True

    def set_x_min(self, value):
        if Country.is_in_interval(self.MIN_SIZE, value, self.x_max):
            self.x_min = value

    def set_x_max(self, value):
        if Country.is_in_interval(self.x_min, value, self.MAX_SIZE):
            self.x_max = value

    def set_y_min(self, value):
        if Country.is_in_interval(self.MIN_SIZE, value, self.y_max):
            self.y_min = value

    def set_y_max(self, value):
        if Country.is_in_interval(self.y_min, value, self.MAX_SIZE):
            self.y_max = value
