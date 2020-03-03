"""This program takes the path to the repo and prints the data table."""

from prettytable import PrettyTable
import individual_metrics
import json_handler


def print_individual_in_table(file_name):
    """Create and print the table using prettytable."""
    data_table = PrettyTable()
    current_data = json_handler.get_dict_from_json_file(file_name)
    dictionary = current_data["INDIVIDUAL_METRICS"]
    headings = [
        "Username",
        "Email",
        "Commits",
        "+",
        "-",
        "Total",
        "Modified Lines",
        "Lines/Commit",
        "File Types",
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
                dictionary[key]["FORMAT"],
            ]
        )
    print(data_table)


# NOTE: For the purposes of testing and demo
if __name__ == "__main__":
    FILE_NAME = input("Enter the name of the file : ")
    # FILE_NAME = "contributor_data_template"
    DATA = individual_metrics.calculate_individual_metrics(FILE_NAME)
    if DATA == {}:
        REPO_PATH = input("Enter the path to the repo : ")
        individual_metrics.add_raw_data_to_json(REPO_PATH, FILE_NAME)
        print("processing data again")
        DATA = individual_metrics.calculate_individual_metrics(FILE_NAME)
    print("Adding processed data to selected json file...")
    # Write reformatted dictionary to json
    json_handler.add_entry(DATA, FILE_NAME)
    print_individual_in_table(FILE_NAME)
