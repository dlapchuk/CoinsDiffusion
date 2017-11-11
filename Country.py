class Country:

    def __init__(self):
        self.name = ''
        self.x_min, self.y_min, self.x_max, self.y_max = None, None, None, None

    def set_x_min(self, value):
        if self.x_max:
            if self.x_max >= value > 0:
                self.x_min = value
                return
        else:
            if value > 0:
                self.x_min = value
                return
        raise ValueError

    def set_x_max(self, value):
        if self.x_min:
            if 10 >= value >= self.x_min:
                self.x_max = value
                return
        else:
            if value <= 10:
                self.x_max = value
                return
        raise ValueError

    def set_y_min(self, value):
        if self.y_max:
            if self.y_max >= value > 0:
                self.y_min = value
                return
        else:
            if value > 0:
                self.y_min = value
                return
        raise ValueError

    def set_y_max(self, value):
        if self.y_min:
            if 10 >= value >= self.y_min:
                self.y_max = value
                return
        else:
            if value <= 10:
                self.y_max = value
                return
        raise ValueError

