import sqlite3
import yfinance as yf
import pandas as pd
import os
from dotenv import load_dotenv

# Assuming you have a DBHandler class
class DBHandler:
    def __init__(self, db_url):
        self.db_url = db_url.replace("sqlite:///", "")
        self.connection = sqlite3.connect(self.db_url)
        self.cursor = self.connection.cursor()

    def create_table_if_not_exists(self):
        # Create the table if it doesn't exist already
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS stock_data (
            id INTEGER PRIMARY KEY,
            symbol TEXT,
            date TEXT,
            open REAL,
            high REAL,
            low REAL,
            close REAL,
            adj_close REAL,
            volume INTEGER
        );
        ''')
        self.connection.commit()

    def insert_stock_data(self, df):
        # Flatten the multi-index DataFrame for easier insertion into the database
        df.reset_index(inplace=True)

        # Insert data into the database
        for index, row in df.iterrows():
            self.cursor.execute('''
            INSERT INTO stock_data (symbol, date, open, high, low, close, adj_close, volume)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?);
            ''', (row['Symbols'], row['Date'], row['Open'], row['High'], row['Low'], row['Close'], row['Adj Close'], row['Volume']))

        self.connection.commit()

    def close_connection(self):
        # Close the connection to the database
        self.connection.close()

    def fetch_all_data(self):
        # Fetch all the data for testing purposes
        self.cursor.execute("SELECT * FROM stock_data")
        return self.cursor.fetchall()
