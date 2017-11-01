from FileEditor import FileEditor


def main():
    file_editor = FileEditor('input_file.txt', 'output_file.txt')
    try:
        test_cases = file_editor.read_file()
    except:
        print('Values in input file are invalid')
    else:
        case_num = 0
        for case in test_cases:
            case_num += 1
            results = case.solve()
            file_editor.write_result(case_num, results)

if __name__ == "__main__":
    main()