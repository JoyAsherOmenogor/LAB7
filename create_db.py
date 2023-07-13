import os
import sqlite3
from datetime import datetime
from faker import Faker

# Determine the path of the database
script_dir = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(script_dir, 'social_network.db')

def create_people_table():
    """Creates the people table in the database"""
    con = sqlite3.connect(db_path)
    cur = con.cursor()
    
    create_ppl_tbl_query = """
    CREATE TABLE IF NOT EXISTS people (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        email TEXT NOT NULL,
        address TEXT NOT NULL,
        city TEXT NOT NULL,
        province TEXT NOT NULL,
        bio TEXT,
        age INTEGER,
        created_at DATETIME NOT NULL,
        updated_at DATETIME NOT NULL
    )
    """
    
    cur.execute(create_ppl_tbl_query)
    con.commit()
    con.close()

def populate_people_table():
    """Populates the people table with 200 fake people"""
    con = sqlite3.connect(db_path)
    cur = con.cursor()
    fake = Faker()
    
    for _ in range(200):
        name = fake.name()
        email = fake.email()
        address = fake.address().replace("\n", ", ")
        city = fake.city()
        province = fake.state()
        bio = fake.text()
        age = fake.random_int(min=1, max=100)
        created_at = datetime.now()
        updated_at = datetime.now()
        
        add_person_query = """
        INSERT INTO people (
            name,
            email,
            address,
            city,
            province,
            bio,
            age,
            created_at,
            updated_at
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """
        
        new_person = (name, email, address, city, province, bio, age, created_at, updated_at)
        cur.execute(add_person_query, new_person)
    
    con.commit()
    con.close()

def main():
    create_people_table()
    populate_people_table()

if __name__ == '__main__':
   main()
