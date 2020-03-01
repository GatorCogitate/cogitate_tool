"""
This module is a work in progress intended to fix duplicate username.

Issues from pydriller.
"""

# TODO not used yet, has no impact
def delete_duplicates(data, keys_to_delete):
    """Delete keys from dictionary, keys are sent in a list."""
    dictionary = data
    for key in keys_to_delete:
        print(dictionary[key], " will be removed")
        del dictionary[key]
        print(key in dictionary)
    return dictionary


# TODO not used yet, has no impact
def parse_email(email):
    """Locate @ and + sign in email and returns the string between them."""
    # find the index of @ sign
    plus_index = email.find("+")
    # find the index of + sign
    at_index = email.find("@")
    # slices string accordingly
    revised_email = email[(plus_index + 1) : at_index]
    return revised_email


# NOTE: there are issues with this function, calls have been commented out
# TODO not used yet, has no impact
def check_emails(data):
    """Remove @github email from users and merges data with duplicates."""
    dictionary = data
    # list intended to gather keys with issues
    name_issues = []
    # gather keys that have issues and duplicates in dictionary
    keys_to_delete = []
    # loop through the data and add keys that have @github email to name_issues
    for key in dictionary:
        # checks if the email is a github email
        if "noreply.github.com" in dictionary[key]["EMAIL"]:
            # adds the key to issues list
            name_issues.append(key)
            # send email to parsing function
            new_name = parse_email(dictionary[key]["EMAIL"])
            if new_name in dictionary:
                print(new_name, " name to be merged with ", key)
                dictionary[new_name]["COMMITS"] += dictionary[key]["COMMITS"]
                dictionary[new_name]["ADDED"] += dictionary[key]["ADDED"]
                dictionary[new_name]["REMOVED"] += dictionary[key]["REMOVED"]
                dictionary[new_name]["TOTAL"] += dictionary[key]["TOTAL"]
                keys_to_delete.append(key)
            else:
                print(new_name, " not found in data")

    dictionary = delete_duplicates(dictionary, keys_to_delete)
    return dictionary
