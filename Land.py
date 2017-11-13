from City import City


class Land:
    def __init__(self):
        self.width = 10
        self.height = 10
        self.land = ()
        self.test_case = None
        self.solved = False
        self.is_country_full_dict = {}
        self.results = {}

    def set_test_case(self, test_case):
        self.test_case = test_case
        for country in test_case.countries:
            self.is_country_full_dict[country.name] = False

    def create_land(self):
        self.land = [[0 for x in range(self.width)] for y in range(self.height)]
        for country in self.test_case.countries:
            for i in range(country.x_min, country.x_max+1):
                for j in range(country.y_min, country.y_max+1):
                    self.land[j-1][i-1] = City(country, self.test_case)

    def solve(self):
        counter = 0
        if len(self.test_case.countries) == 1:
            for country in self.test_case.countries:
                self.results[country.name] = 0
                return self.results
        while not self.solved:
            counter += 1
            self.make_exchange(counter)
        return self.results

    @staticmethod
    def make_transaction(self_city, neighbor_city):
        for key, value in self_city.coins_amount.items():
            amount = self_city.coins_amount[key] // 1000
            self_city.set_coins_changes(key, -amount)
            neighbor_city.set_coins_changes(key, amount)

    def make_exchange(self, counter):
        self.solved = True
        for country in self.test_case.countries:
            for j in range(country.x_min-1, country.x_max):
                for i in range(country.y_min-1, country.y_max):
                    if self.land[i][j]:
                        if self.land[i-1][j]:
                            self.make_transaction(self.land[i][j], self.land[i-1][j])
                        if self.land[i+1][j]:
                            self.make_transaction(self.land[i][j], self.land[i+1][j])
                        if self.land[i][j-1]:
                            self.make_transaction(self.land[i][j], self.land[i][j-1])
                        if self.land[i][j+1]:
                            self.make_transaction(self.land[i][j], self.land[i][j+1])

        for country in self.test_case.countries:
            full_first_time = True
            for j in range(country.x_min-1, country.x_max):
                for i in range(country.y_min-1, country.y_max):
                    self.land[i][j].change_coins_amount()
                    if not self.is_country_full_dict[country.name]:
                        if full_first_time:
                            full_first_time = self.land[i][j].check_exit()
                    else:
                        full_first_time = False
            if full_first_time:
                self.results[country.name] = counter
                self.is_country_full_dict[country.name] = True

        for key, value in self.is_country_full_dict.items():
            if self.solved:
                self.solved = self.is_country_full_dict[key]
