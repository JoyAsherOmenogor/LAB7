import os
import sqlite3
import csv
from create_db import db_path, script_dir

def main():
    old_people_list = get_old_people()
    print_name_and_age(old_people_list)
    save_name_and_age_to_csv(old_people_list)

def get_old_people():
    """Queries the Social Network database for all people who are at least 50 years old.

    Returns:
        list: List of dictionaries containing name and age of old people
    """
    con = sqlite3.connect(db_path)
    cur = con.cursor()

    select_old_people_query = """
    SELECT name, age FROM people WHERE age >= 50
    """

    cur.execute(select_old_people_query)
    old_people_list = cur.fetchall()

    con.close()

    # Convert the list of tuples to a list of dictionaries
    old_people_list = [{'name': row[0], 'age': row[1]} for row in old_people_list]

    return old_people_list

def print_name_and_age(name_and_age_list):
    """Prints the name and age of all people in the provided list.

    Args:
        name_and_age_list (list): List of dictionaries containing name and age information
    """
    for person in name_and_age_list:
        name = person['name']
        age = person['age']
        print(f"{name} is {age} years old.")

def save_name_and_age_to_csv(name_and_age_list):
    """Saves the name and age of all people in the provided list to a CSV file.

    Args:
        name_and_age_list (list): List of dictionaries containing name and age information
    """
    csv_path = os.path.join(script_dir, 'old_people.csv')
    
    with open(csv_path, 'w', newline='') as csvfile:
        fieldnames = ['Name', 'Age']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        writer.writeheader()
        writer.writerows(name_and_age_list)

if __name__ == '__main__':
   main()

