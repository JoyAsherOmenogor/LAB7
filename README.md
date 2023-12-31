# LAB7
 import sqlite3
from faker import Faker
from datetime import datetime

# Create a faker object for generating fake data
fake = Faker()

# Open a connection to the database
con = sqlite3.connect('social_network.db')
cur = con.cursor()

# Create the people table if it doesn't exist
create_ppl_tbl_query = """
CREATE TABLE IF NOT EXISTS people
(
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
);
"""
cur.execute(create_ppl_tbl_query)

# Generate and insert fake data into the people table
for _ in range(200):
    name = fake.name()
    email = fake.email()
    address = fake.address()
    city = fake.city()
    province = fake.state()
    bio = fake.text()
    age = fake.random_int(min=1, max=100)
    created_at = datetime.now()
    updated_at = datetime.now()

    add_person_query = """
    INSERT INTO people (name, email, address, city, province, bio, age, created_at, updated_at)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?);
    """
    cur.execute(add_person_query, (name, email, address, city, province, bio, age, created_at, updated_at))

# Commit the changes and close the connection
con.commit()
con.close()

