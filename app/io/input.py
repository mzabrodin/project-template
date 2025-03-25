import pandas as pd


def input_from_console():
    """Reads text from console.

    Returns:
        str: The text read in the console.
    """
    return input("Enter text: ")


def input_from_file(file_name):
    """Reads text in file using Python built-in methods.

    Args:
        file_name (str): The file name argument.

    Returns:
        str: The text read in the file.

    Raises:
        FileNotFoundError: If the file with the name ‘file_name’ is not found.
    """
    try:
        with open(file_name, 'r') as file:
            return file.read()
    except FileNotFoundError:
        raise FileNotFoundError(f"File named '{file_name}' was not found")


def input_from_file_using_pandas(csv_file_name):
    """Reads text in .csv file using Pandas.

    Args:
        csv_file_name (str): The file name argument.

    Returns:
        pd.DataFrame: The DataFrame that was read in the .csv file.

    Raises:
        FileNotFoundError: If the file with the name ‘file_name’ is not found.
        TypeError: If the file does not have a .csv extension.
    """
    if not csv_file_name.endswith(".csv"):
        raise TypeError("The file must be .csv")

    try:
        return pd.read_csv(csv_file_name)
    except FileNotFoundError:
        raise FileNotFoundError(f"File named '{csv_file_name}' was not found")
