from app.io.input import input_from_console, input_from_file, input_from_file_using_pandas
from app.io.output import output_to_console, output_to_file, output_to_file_using_pandas


def main():
    console_text = input_from_console()
    file_text = input_from_file("data/input.txt")
    pandas_file_text = input_from_file_using_pandas("data/pandas_input.csv")

    output_to_console(console_text)
    output_to_console(file_text)
    output_to_console(pandas_file_text.to_string())

    output_to_file("data/output.txt", file_text)
    output_to_file_using_pandas("data/pandas_output.csv", pandas_file_text)


if __name__ == "__main__":
    main()
