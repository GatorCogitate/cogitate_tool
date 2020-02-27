"""This program takes the path to the repo and prints the data table."""

from prettytable import PrettyTable
import count_code_lines


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
        "Lines/Commit",
        "Files",
    ]
    data_table.field_names = headings
    for key in dictionary:
        data_table.add_row(
            [
                key,
                dictionary[key]["EMAIL"],
                dictionary[key]["COMMITS"],
                dictionary[key]["ADDED"],
                dictionary[key]["REMOVED"],
                dictionary[key]["TOTAL"],
                dictionary[key]["MODIFIED"],
                dictionary[key]["RATIO"],
                dictionary[key]["FILES"],
            ]
        )
    print(data_table)


if __name__ == "__main__":
    # takes input for the repository local path OR URL
    PATH_REPO = input("Enter the path to the repo : ")
    DATA = count_code_lines.get_commit_data(PATH_REPO)
    # data = count_code_lines.get_file_types(path_repo)
    # print("data before checking")
    print_in_table(DATA)
    # print("data after checking")
    # data = check_emails(data)
    # print_in_table(data)
