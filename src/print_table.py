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
        "Lines/Commit",
        "Changed_Lines",
    ]
    data_table.field_names = headings
    for key in dictionary:
        data_table.add_row(
            [
                key,
                dictionary[key][0],
                dictionary[key][1],
                dictionary[key][2],
                dictionary[key][3],
                dictionary[key][4],
                dictionary[key][5],
                dictionary[key][6],
            ]
        )
    print(data_table)


def main():
    """Call other functions in this module asking for user input."""
    # takes input for the repository local path OR URL
    path_repo = input("Enter the path to the repo : ")
    data = count_code_lines.get_commit_lines(path_repo)
    data = count_code_lines.get_commit_average(data)
    # print("data before checking")
    print_in_table(data)
    # print("data after checking")
    # data = check_emails(data)
    # print_in_table(data)


if __name__ == "__main__":
    main()
