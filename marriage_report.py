"""
Authors: Mahenur Master, Sneha Malhotra, Nisharg Patel, Siddharth Patel

Description:
Generates a CSV report containing all married couples in
the Social Network database.

Usage:
python marriage_report.py
"""

import os
import sqlite3
from create_relationships import db_path, script_dir
import pandas as pd

def main():
    # Query the database for a list of married couples
    couples = fetch_married_couples()

    # Save the list of married couples to a CSV file
    csv_output_path = os.path.join(script_dir, 'married_couples.csv')
    save_couples_to_csv(couples, csv_output_path)

def fetch_married_couples():
    """Fetches a list of all married couples from the Social Network database.

    Returns:
        list: (name1, name2, start_date) of married couples 
    """
    con = sqlite3.connect(db_path)
    cur = con.cursor()

    # SQL query to retrieve married couples
    couples_query = """
    SELECT p1.name, p2.name, start_date FROM relationships
    JOIN people p1 ON person1_id = p1.id
    JOIN people p2 ON person2_id = p2.id
    WHERE type = "spouse";
    """
    
    # Execute the query and fetch all results
    cur.execute(couples_query)
    couples_list = cur.fetchall()
    con.close()  # Ensure the connection is closed
    return couples_list

def save_couples_to_csv(couples, csv_path):
    """Saves the list of married couples to a CSV file, including names and anniversary date.

    Args:
        couples (list): (name1, name2, start_date) of married couples
        csv_path (str): Path to the output CSV file
    """
    # Convert the list of couples to a DataFrame
    df = pd.DataFrame(couples, columns=["Person 1", "Person 2", "Anniversary"])
    
    # Write the DataFrame to a CSV file
    df.to_csv(csv_path, index=False)

if __name__ == '__main__':
    main()
