from TestCase import TestCase
from Country import Country


class FileEditor:

    def __init__(self, input_file, output_file):
        self.data = []
        self.test_cases = 0
        self.input_file = input_file
        self.output_file = output_file
        open(output_file, 'w').close()

    def parse_file(self):
        with open(self.input_file) as f:
            for line in f:
                for word in line.split():
                    self.data.append(word)

    def set_country(self):
        test_cases = []
        i = 1
        num = int(self.data[0])
        while num != 0:
            test_case = TestCase()
            for j in range(0, num):
                country = Country()
                country.name = self.data[i]
                i += 1
                country.x_min = int(self.data[i])
                i += 1
                country.y_min = int(self.data[i])
                i += 1
                country.x_max = int(self.data[i])
                i += 1
                country.y_max = int(self.data[i])
                i += 1
                test_case.add_country(country)
            test_cases.append(test_case)
            num = int(self.data[i])
            i += 1
        return test_cases

    def read_file(self):
        self.parse_file()
        return self.set_country()

    @staticmethod
    def __sort_result_dict(result):
        return sorted(result.items(), key=lambda x: (x[1],x[0]), reverse=False)

    def write_result(self, num_case, result):
        with open(self.output_file, 'a') as output_file:
            output_file.write('Test case ' + str(num_case) + '\n')
            for country in self.__sort_result_dict(result):
                output_file.write(country[0] + ' ' + str(country[1]) + '\n')
