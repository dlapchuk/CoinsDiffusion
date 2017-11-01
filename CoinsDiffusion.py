from FileReader import FileReader


def main():
    file_reader = FileReader('input_file.txt', 'output_file.txt')
    try:
        test_cases = file_reader.read_file()
    except:
        print('Values in input file are invalid')
    else:
        case_num = 0
        for case in test_cases:
            case_num += 1
            results = case.solve()
            file_reader.write_result(case_num, results)

if __name__ == "__main__":
    main()