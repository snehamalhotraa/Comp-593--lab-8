"""
Authors: Mahenur Master, Sneha Malhotra, Nisharg Patel, Siddharth Patel

Description:
This script creates the 'relationships' table in the Social Network database
and populates it with 100 fake relationships.

Usage:
python create_relationships.py
"""

import os
import sqlite3
from faker import Faker
from random import randint, choice

# Establish connection to the database
con = sqlite3.connect('social_network.db')
cur = con.cursor()

# Define the path of the database
script_dir = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(script_dir, 'social_network.db')

def main():
    create_relationships_table()
    populate_relationships_table()
    con.close()

def create_relationships_table():
    """Sets up the 'relationships' table in the database."""
    # SQL statement to create the 'relationships' table
    create_relationships_tbl_query = """
        CREATE TABLE IF NOT EXISTS relationships
        (
            id INTEGER PRIMARY KEY,
            person1_id INTEGER NOT NULL,
            person2_id INTEGER NOT NULL,
            type TEXT NOT NULL,
            start_date DATE NOT NULL,
            FOREIGN KEY (person1_id) REFERENCES people (id),
            FOREIGN KEY (person2_id) REFERENCES people (id)
        );
    """
    # Execute the SQL statement to create the table
    cur.execute(create_relationships_tbl_query)
    con.commit()

def populate_relationships_table():
    """Inserts 100 fake relationship records into the 'relationships' table."""
    # SQL statement to insert data into the 'relationships' table
    add_relationship_query = """
        INSERT INTO relationships
        (
            person1_id,
            person2_id,
            type,
            start_date
        )
        VALUES (?, ?, ?, ?);
    """
    
    fake = Faker()
    for _ in range(100):
        # Randomly select the first person in the relationship
        person1_id = randint(1, 200)

        # Randomly select the second person in the relationship, ensuring it's not the same as the first
        person2_id = randint(1, 200)
        while person2_id == person1_id:
            person2_id = randint(1, 200)

        # Randomly select a type of relationship
        rel_type = choice(['friend', 'spouse', 'partner', 'relative'])

        # Randomly select a start date for the relationship within the last 50 years
        start_date = fake.date_between(start_date='-50y', end_date='today')

        # Create a tuple with the new relationship data
        new_relationship = (person1_id, person2_id, rel_type, start_date)

        # Insert the new relationship into the database
        cur.execute(add_relationship_query, new_relationship)

    con.commit()

if __name__ == '__main__':
    main()
