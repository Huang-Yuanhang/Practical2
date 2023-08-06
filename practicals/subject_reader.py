"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    data = get_data()
    display_subject_info(data)


def get_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    input_file = open(FILENAME, "r")
    data = []  # Initialize an empty list to store the data
    for line in input_file:
        line = line.strip()
        parts = line.split(',')
        parts[2] = int(parts[2])
        data.append(parts)  # Append the parts list to the data list
    input_file.close()
    return data


def display_subject_info(data):
    """Display subject information."""
    for subject_data in data:
        code, teacher, students = subject_data
        print(f"{code} is taught by {teacher} and has {students} students")


main()
