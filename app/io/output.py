import pandas as pd


def output_to_console(text):
    """Prints text to console.

    Args:
        text (str): The text to print in console.
    """
    pass


def output_to_file(file_name, text):
    """Writes text to a new .csv file using Python built-in methods.

    Args:
        file_name (str): The file name argument.
        text (str): The text to write in file.

    Raises:
        FileExistsError: If a file with the name ‘file_name’ already exists.
    """
    pass


def output_to_file_using_pandas(file_name, data_frame):
    """Writes text to a new .csv file using Pandas.

    Args:
        file_name (str): The file name argument.
        data_frame (pd.DataFrame): The text to write in file.

    Raises:
        FileExistsError: If a file with the name ‘file_name’ already exists.
        TypeError: If the data_frame is not an instance of DataFrame.
    """
    pass
