from Land import Land


class TestCase:

    def __init__(self):
        self.countries = []
        self.result = ()

    def add_country(self, country):
        self.countries.append(country)

    def solve(self):
        land = Land()
        land.set_test_case(self)
        land.create_land()
        return land.solve()

    def write_result(self):
        pass
