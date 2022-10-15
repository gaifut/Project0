from tkinter import *
from tkinter import filedialog
import sqlite3
import csv
from unittest import result
import os
import requests
import pandas

from dadata import Dadata
token = "08e79df629df8d18b15a8bb40c24c7e1bea9d366"
secret = "40b5d0f8ca50c61f5dbd593fb7c5d4f1a826b15f" 
dadata = Dadata(token, secret)



class GUI():
    def __init__(self):
        self.root = Tk()
        self.root.title("Обрабатыватель данных ГМП")
        self.filename = ""

   
#  button choose file
        button_choose_file = Button (self.root, text = "Choose file", command=self.choose_file)
        button_choose_file.grid(row = 0, column = 0)
        
#  button show orders      
        button_show_orders = Button (self.root, text = "Show orders")
        button_show_orders.grid(row = 0, column = 2)

#  button upload 
        button_upload = Button (self.root, text = "Upload")
        button_upload.grid(row = 0, column = 4)

#  labels epty (separators)
        label_empty1 = Label(self.root, text = "")
        label_empty1.grid(row = 1, column = 0)

#  labels table
        label_customer = Label(self.root, text = "Customer")
        label_customer.grid(row = 2, column = 0)

        label_supplier = Label(self.root, text = "Supplier")
        label_supplier.grid(row = 2, column = 1)

        label_customers_address = Label(self.root, text = "Customer's Address")
        label_customers_address.grid(row = 2, column = 2)

        label_product = Label(self.root, text = "Prodcut")
        label_product.grid(row = 2, column = 3)

        label_quantity = Label(self.root, text = "Quantity")
        label_quantity.grid(row = 2, column = 4)

        label_total_cost = Label(self.root, text = "Total cost")
        label_total_cost.grid(row = 2, column = 5)

        self.root.mainloop()

    def choose_file(self):
        opened_file = filedialog.askopenfilename(initialdir="C:\Python\Project 0", title="Select a file")
        print ("Function open read:")
        print (opened_file)
        self.filename = opened_file

        df_column_customer_address = pandas.read_csv(opened_file, encoding="utf8")
        customer_address_list = df_column_customer_address["Customer address"].tolist()
        print(customer_address_list)

# check data with API

        updated_customer_address_list = []

        for n in customer_address_list:
            address_info_updated = dadata.clean("address", n)["result"], dadata.clean("address", n)["postal_code"]
            updated_customer_address_list.append(address_info_updated)
            print(updated_customer_address_list)

#  using the generated clean list and adding it as a new column to the original CSV file
        df_column_customer_address.insert(3,"Customer address updated",updated_customer_address_list, True)
        print(df_column_customer_address)

        
        open_choose_file_in_GUI = open(opened_file, encoding="UTF8")
        reader_choose_file_in_GUI = csv.reader(open_choose_file_in_GUI)
        data_from_choose_file_in_GUI = list(reader_choose_file_in_GUI)

        
# Grab all column infomration  
        list_in_GUI_data_from_choose_file_in_GUI_customer = []
        for customer in range (1, len(data_from_choose_file_in_GUI)):
                list_in_GUI_data_from_choose_file_in_GUI_customer.append(data_from_choose_file_in_GUI[customer][0])

        var_list_customer = StringVar(value = list_in_GUI_data_from_choose_file_in_GUI_customer)
        customer_list = Listbox (self.root, listvariable = var_list_customer)
        customer_list.grid(row = 3, column = 0)

        list_in_GUI_data_from_choose_file_in_GUI_supplier = []
        for supplier in range (1, len(data_from_choose_file_in_GUI)):
                list_in_GUI_data_from_choose_file_in_GUI_supplier.append(data_from_choose_file_in_GUI[supplier][1])

        var_list_supplier = StringVar(value = list_in_GUI_data_from_choose_file_in_GUI_supplier)
        supplier_list = Listbox (self.root, listvariable = var_list_supplier)
        supplier_list.grid(row = 3, column = 1)      

        var_list_customers_address = StringVar (value = updated_customer_address_list)
        customer_address_list = Listbox (self.root, listvariable = var_list_customers_address)
        customer_address_list.grid(row = 3, column = 2)


GUI()

