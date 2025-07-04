#!/usr/bin/env python3

import mysql.connector


def create_database():
    try:
        # Connect to MySQL server (adjust credentials)
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='your_password'  # <-- Replace with your MySQL root password
        )

        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store;")
            print("Database 'alx_book_store' created successfully!")

    except mysql.connector.Error as err:
        print(f"Error connecting to MySQL or creating database: {err}")

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection closed.")


if __name__ == "__main__":
    create_database()
