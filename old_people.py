import os
import sqlite3
import csv
from create_db import db_path, script_dir

def main():
    old_people_list = get_old_people()
    print_name_and_age(old_people_list)

    old_people_csv = os.path.join(script_dir, 'old_people.csv')
    save_name_and_age_to_csv(old_people_list, old_people_csv)

def get_old_people():
    """Queries the Social Network database for all people who are at least 50 years old.

    Returns:
        list: List of tuples containing (name, age) of old people 
    """
    con = sqlite3.connect(db_path)
    cur = con.cursor()

    select_old_people_query = """
    SELECT name, age FROM people WHERE age >= 50
    """

    cur.execute(select_old_people_query)
    old_people_list = cur.fetchall()

    con.close()
    return old_people_list

def print_name_and_age(name_and_age_list):
    """Prints name and age of all people in the provided list.

    Args:
        name_and_age_list (list): List of tuples containing (name, age) of people
    """
    for person in name_and_age_list:
        name, age = person
        print(f"{name} is {age} years old.")

def save_name_and_age_to_csv(name_and_age_list, csv_path):
    """Saves name and age of all people in the provided list to a CSV file.

    Args:
        name_and_age_list (list): List of tuples containing (name, age) of people
        csv_path (str): Path of the CSV file
    """
    with open(csv_path, 'w', newline='') as csvfile:
        fieldnames = ['Name', 'Age']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for person in name_and_age_list:
            writer.writerow({'Name': person[0], 'Age': person[1]})

if __name__ == '__main__':
   main()
