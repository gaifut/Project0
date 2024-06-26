import sqlite3
from tkinter import *
from tkinter import Button, Entry, Label

root = Tk()
root.title("Test sample part")

connect_to_DB = sqlite3.connect("products.db")
cursor_DB = connect_to_DB.cursor()
cursor_DB.execute("""CREATE TABLE IF NOT EXISTS products ( 
                product_name text,
                product_price real
                )""")


def submit():
    connect_to_DB = sqlite3.connect("products.db")
    cursor_DB = connect_to_DB.cursor()
    cursor_DB.execute(
        "INSERT INTO products VALUES (:product_name, :product_price)",
        {'product_name': product_name.get(),
         'product_price': product_price.get()})

    # Commit changes and close connection
    connect_to_DB.commit()
    connect_to_DB.close()

    # Clear the text boxes from the previous input
    product_name.delete(0, END)
    product_price.delete(0, END)


def query():
    connect_to_DB = sqlite3.connect("products.db")
    cursor_DB = connect_to_DB.cursor()
    cursor_DB.execute("SELECT *, oid FROM products")
    records = cursor_DB.fetchall()
    # If I need to see that in the terminal then: print(records)

    print_records = ""
    for record in records:
        print_records += str(record[0]) + " " + str(record[1]) + " " + "\t" + str(record[2]) + "\n"

    query_label = Label(root, text=print_records)
    query_label.grid(row=6, column=0)

    # Commit changes and close connection
    connect_to_DB.commit()
    connect_to_DB.close()


def delete():
    connect_to_DB = sqlite3.connect("products.db")
    cursor_DB = connect_to_DB.cursor()
    connect_to_DB.execute(
        "DELETE from products WHERE oid= " + delete_entry.get())

    # Commit changes and close connection
    connect_to_DB.commit()
    connect_to_DB.close()

    delete_entry.delete(0, END)

# Create text box labels
product_name_label = Label(root, text="Product name")
product_name_label.grid(row=0, column=0)
product_price_label = Label(root, text="Product price per 1 unit")
product_price_label.grid(row=1, column=0)

# Create text boxes
product_name = Entry(root, width=30)
product_name.grid(row=0, column=1)
product_price = Entry(root, width=30)
product_price.grid(row=1, column=1)
delete_entry = Entry(root, width=30)
delete_entry.grid(row=4, column=1)

# Create Submit button
Submit_button = Button(
    root, text="Add information to Database", command=submit)
Submit_button.grid(row=3, column=1)

# Create Query button
Query_button = Button(root, text="Show results", command=query)
Query_button.grid(row=5, column=1)

# Create delete button
delete_button = Button(root, text="Delete ID from the DB", command=delete)
delete_button.grid(row=4, column=0)

# Create empty filler
label_empty1 = Label(root, text="")
label_empty1.grid(row=2, column=0)

# Commit changes and close connection
connect_to_DB.commit()
connect_to_DB.close()

root.mainloop()
