class City:
    def __init__(self, country, test_case):
        self.coins_amount = {}
        self.coins_changes = {}
        self.INITIAL_COINS_VALUE = 1000000
        self.country = country
        self.init_coins_amount(test_case)

    def init_coins_amount(self, test_case):

        for country in test_case.countries:
            if country == self.country:
                self.coins_amount[country.name] = self.INITIAL_COINS_VALUE
            else:
                self.coins_amount[country.name] = 0
            self.coins_changes[country.name] = 0

    def change_coins_amount(self):
        for (key, value) in self.coins_changes.items():
            self.coins_amount[key] += self.coins_changes[key]
            self.coins_changes[key] = 0

    def set_coins_changes(self, name, delta):
        self.coins_changes[name] += delta

    def check_exit(self):
        for key, value in self.coins_amount.items():
                if self.coins_amount[key] == 0:
                    return False
        return True
