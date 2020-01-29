from tkinter import *
from PIL import ImageTk, Image
import sqlite3

root = Tk()
root.title("Databases")

# create a db or connect to one
conn = sqlite3.connect('address_book.db')

# create cursor
c = conn.cursor()

'''
# create table
c.execute("""CREATE TABLE addresses (
    first_name text,
    last_name text,
    address text,
    city text,
    state text,
    zipcode integer
    )""")
'''

# delete record funtion
def delete():
    # create a db or connect to one & cursor
    conn = sqlite3.connect('address_book.db')
    c = conn.cursor()

    c.execute("DELETE from addresses WHERE oid = " + delete_box.get())
    delete_box.delete(0,END)

    # commit changes & closing connections
    conn.commit()
    conn.close()

# Submit Funtion
def submit():
    # create a db or connect to one & cursor
    conn = sqlite3.connect('address_book.db')
    c = conn.cursor()

    # insert into table
    c.execute("INSERT INTO addresses VALUES (:f_name, :l_name, :address, :city, :state, :zipcode)",
            {
                'f_name': f_name.get(),
                'l_name': l_name.get(),
                'address': address.get(),
                'city': city.get(),
                'state': state.get(),
                'zipcode': zipcode.get()
            }
    )

    # commit changes & closing connections
    conn.commit()
    conn.close()

    # clear txt boxes
    f_name.delete(0, END)
    l_name.delete(0, END)
    address.delete(0, END)
    city.delete(0, END)
    state.delete(0, END)
    zipcode.delete(0, END)

# Query Funtion
def query():
    # create a db or connect to one & cursor
    conn = sqlite3.connect('address_book.db')
    c = conn.cursor()

    c.execute("SELECT *,oid FROM addresses")
    records = c.fetchall()
    print(records)

    # loop through results
    print_records = ''
    for record in records:
        for item in record:
            print_records += str(item) + " "
        print_records += "\n"
    
    query_label =Label(root, text=print_records)
    query_label.grid(row=10, column=0, columnspan=2)

    # commit changes & closing connections
    conn.commit()
    conn.close()



# creating entries
f_name = Entry(root, width=30)
l_name = Entry(root, width=30)
address = Entry(root, width=30)
city = Entry(root, width=30)
state = Entry(root, width=30)
zipcode = Entry(root, width=30)

# putting in grid (Entries)
f_name.grid(row=0, column=1, padx=20)
l_name.grid(row=1, column=1, padx=20)
address.grid(row=2, column=1, padx=20)
city.grid(row=3, column=1, padx=20)
state.grid(row=4, column=1, padx=20)
zipcode.grid(row=5, column=1, padx=20)

# creating textbox labels
f_name_label = Label(root, text="First Name")
l_name_label = Label(root, text="Last Name")
address_label = Label(root, text="Address")
city_label = Label(root, text="City")
state_label = Label(root, text="State")
zipcode_label = Label(root, text="Zipcode")

# putting in grid (Labels)
f_name_label.grid(row=0, column=0, padx=20)
l_name_label.grid(row=1, column=0, padx=20)
address_label.grid(row=2, column=0, padx=20)
city_label.grid(row=3, column=0, padx=20)
state_label.grid(row=4, column=0, padx=20)
zipcode_label.grid(row=5, column=0, padx=20)

# creating submit buttons & adding to grid
submit_button = Button(root, text="Add Records to Database", command=submit)
submit_button.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

# Query button
query_button = Button(root, text="Show Records", command=query)
query_button.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=137)

# delete button
query_button = Button(root, text="Delete Record", command=delete)
query_button.grid(row=9, column=0, columnspan=2, pady=10, padx=10, ipadx=137)

# delete entry box & label
delete_box = Entry(root, width=30)
delete_box.grid(row=8, column=1)
delete_box_lebel = Label(root, text="ID Number")
delete_box_lebel.grid(row=8, column=0)


# commit changes
conn.commit()
# closes connections
conn.close()

root.mainloop()