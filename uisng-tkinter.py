# Source: https://www.youtube.com/watch?v=ELkaEpN29PU&ab_channel=TraversyMedia
# Source: https://www.geeksforgeeks.org/reading-and-writing-csv-files-in-python/

from tkinter import *
import csv

def populate_list():
  print("Populate")

def add_item():
  print("Add")

def remove_item():
  print("Remove")

def update_item():
  print("Update")

def clear_item():
  print("Clear")

with open('data.csv', mode='r') as file:
  csv_file = csv.reader(file)
  print(csv_file)
  for lines in csv_file:
    print(lines)



# Create window object
app = Tk()

# Part
part_text = StringVar()
part_label = Label(app , text= 'Part Name' , font=('bold', 14) , pady=20)
part_label.grid(row=0,column=0, sticky=W)
part_entry = Entry(app, textvariable=part_text)
part_entry.grid(row=0, column=1)

# Customer
customer_text = StringVar()
customer_label = Label(app , text= 'Customer Name' , font=('bold', 14) , pady=20)
customer_label.grid(row=0,column=2, sticky=W)
customer_entry = Entry(app, textvariable=customer_text)
customer_entry.grid(row=0, column=3)

# Retailer
retailer_text = StringVar()
retailer_label = Label(app , text= 'Retailer Name' , font=('bold', 14) , pady=20)
retailer_label.grid(row=1,column=0, sticky=W)
retailer_entry = Entry(app, textvariable=retailer_text)
retailer_entry.grid(row=1, column=1)

# Price
price_text = StringVar()
price_label = Label(app , text= 'Price Name' , font=('bold', 14) , pady=20)
price_label.grid(row=1,column=2, sticky=W)
price_entry = Entry(app, textvariable=price_text)
price_entry.grid(row=1, column=3)

# List Box
parts_list = Listbox(app, height=8, width=50)
parts_list.grid(row=3,column=0, columnspan=3, rowspan=6, pady=20, padx=20)

# Create scrollbar
scrollbar = Scrollbar(app)
scrollbar.grid(row=3, column=3)

# Set scroll to list
parts_list.configure(yscrollcommand=scrollbar.set)
scrollbar.configure(command=parts_list.yview)

# Button
add_btn =Button(app, text='Add Part', width=12, command=add_item)
add_btn.grid(row=2, column=0 , pady=20)

remove_btn =Button(app, text='Remove Part', width=12, command=remove_item)
remove_btn.grid(row=2, column=1 , pady=20)

update_btn =Button(app, text='Update Part', width=12, command=update_item)
update_btn.grid(row=2, column=2 , pady=20)

clear_btn =Button(app, text='Clear Input', width=12, command=clear_item)
clear_btn.grid(row=2, column=3 , pady=20)

app.title('Part Manager')
app.geometry('700x350')

populate_list()

# Start Program
app.mainloop()