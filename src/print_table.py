"""This program takes the path to the repo and prints the data table."""

from prettytable import PrettyTable
import count_code_lines

# Keys for the dicitionary indeces
EMAILS = 0
COMMITS = 1
ADDED = 2
REMOVED = 3
TOTAL = 4
MODIFIED = 5
RATIO = 6
FILES = 7
FORMAT = 8


def print_in_table(dictionary):
    """Create and print the table using prettytable."""
    data_table = PrettyTable()
    headings = [
        "Username",
        "Email",
        "Commits",
        "+",
        "-",
        "Total",
        "Modified Lines",
        "Lines per Commit",
    ]
    data_table.field_names = headings
    for key in dictionary:
        data_table.add_row(
            [
                key,
                dictionary[key][EMAILS],
                dictionary[key][COMMITS],
                dictionary[key][ADDED],
                dictionary[key][REMOVED],
                dictionary[key][TOTAL],
                dictionary[key][MODIFIED],
                dictionary[key][RATIO],
            ]
        )
    print(data_table)


def main():
    """Call other functions in this module asking for user input."""
    # takes input for the repository local path OR URL
    path_repo = input("Enter the path to the repo : ")
    data = count_code_lines.get_commit_data(path_repo)
    # data = count_code_lines.get_file_types(path_repo)
    # print("data before checking")
    print_in_table(data)
    # print("data after checking")
    # data = check_emails(data)
    # print_in_table(data)


if __name__ == "__main__":
    main()
