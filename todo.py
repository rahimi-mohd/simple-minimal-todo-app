#! /usr/bin/python3

import sqlite3
import sys
conn = sqlite3.connect("database.db")
c = conn.cursor()

def main():
    create_table()
    
    # mainloop
    while True:
        read_todo()
        print()
        print("-" * 20)
        print("1. Add ToDo")
        print("2. Delete ToDo")
        print("3. Exit")
        user_input = input("> ")
        if user_input == "1":
            insert_todo()
            print()
        elif user_input == '2':
            delete_todo()
            print()
        elif user_input == "clean":
            clean()
            print()
        elif user_input == "3":
            sys.exit()

def create_table():
    c.execute("CREATE TABLE IF NOT EXISTS todo(id INTEGER PRIMARY KEY, todo TEXT)")

def insert_todo():
    todo = input("> ")
    c.execute("INSERT INTO todo(todo) VALUES (?)", (todo,))
    conn.commit()

def read_todo():
    c.execute("SELECT * FROM todo")
    for row in c.fetchall():
        print(f"Id-{row[0]}:\t{row[1]}")

def delete_todo():
    delete_todo = input("Select todo's id to delete: ")
    c.execute("DELETE FROM todo WHERE id = (?)", delete_todo,)
    conn.commit()

def clean():
    c.execute("DELETE FROM todo")
    conn.commit()





if __name__ == "__main__":
    main()
