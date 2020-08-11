from string_operations import StringOperations
from files.file_operations import FileOperations
from handlers.console_input import InputHandler
from case_operations import CaseOperations


def main():
    # Problem 1
    input_handler = InputHandler()
    print(input_handler.read_inputs())
    # Problem 2
    operations = StringOperations()
    print(operations.string_alternative("Good evening"))
    # Problem 3
    file_opearations = FileOperations()
    file_opearations.count_words("input.txt","output.txt")
    CaseOperations.change_case("testing for function")

if __name__ == "__main__":
    main()
