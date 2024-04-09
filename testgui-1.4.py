import csv
import mysql.connector
import os
import os.path
import pandas
import sqlite3
from dadata import Dadata
from dotenv import load_dotenv
from itertools import zip_longest
from mysql.connector import Error
from tkinter import *
from tkinter import Button, Label, Listbox, StringVar, OptionMenu, filedialog

load_dotenv()

# Constants:
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

token = os.getenv('TOKEN')
secret = os.getenv('SECRET')

dadata = Dadata(token, secret)
numbers_list = list(range(0, 100))

#  Create connection to DB with prices and products
db_path = os.path.join(BASE_DIR, "products.db")
with sqlite3.connect(db_path) as db:
    connect_to_DB = sqlite3.connect("products.db")
print("Connected to products database successfully")

# Connect to MYSQL Server and create DB
try:
    conn = mysql.connector.connect(
        host=os.getenv('HOST'), user=os.getenv('USER'),
        password=os.getenv('PASSWORD'), database=os.getenv('DATABASE'))
    if conn.is_connected():
        cursor_MYSQL = conn.cursor()
        print('Connected to DB')
except:
    conn = mysql.connector.connect(
        host=os.getenv('HOST'), user=os.getenv('USER'),
        password=os.getenv('PASSWORD'))
    cursor_MYSQL = conn.cursor()
    cursor_MYSQL.execute("CREATE DATABASE test_gmp")
    print("Created DB")

#  Create cursor
cursor_DB = connect_to_DB.cursor()

#  Query 1: bring the products list from the DB
query = "SELECT product_name FROM products"
r_set = connect_to_DB.execute(query)
my_list = [r for r, in r_set]


class GUI():
    def __init__(self):
        self.root = Tk()
        self.root.title("Обрабатыватель данных ГМП")
        self.filename = ""

#  button choose file
        button_choose_file = Button(
            self.root, text="Choose file", command=self.choose_file)
        button_choose_file.grid(row=0, column=0)

#  button upload
        button_upload = Button(self.root, text="Upload", command=self.upload)
        button_upload.grid(row=0, column=4)

#  labels epty (separators)
        label_empty1 = Label(self.root, text="")
        label_empty1.grid(row=1, column=0)

#  labels table
        label_no = Label(self.root, text="No")
        label_no.grid(row=2, column=0)

        label_customer = Label(self.root, text="Customer")
        label_customer.grid(row=2, column=1)

        label_supplier = Label(self.root, text="Supplier")
        label_supplier.grid(row=2, column=2)

        label_customers_address = Label(self.root, text="Customer's Address")
        label_customers_address.grid(row=2, column=3)

        label_product = Label(self.root, text="Prodcut")
        label_product.grid(row=2, column=4)

        label_quantity = Label(self.root, text="Quantity")
        label_quantity.grid(row=2, column=5)

        label_price_per_unit = Label(self.root, text="Price Per 1 unit")
        label_price_per_unit.grid(row=2, column=6)

        label_total_cost = Label(self.root, text="Total cost")
        label_total_cost.grid(row=2, column=7)

#  buttons and labels for adding products
        clicked1 = StringVar(self.root)
        clicked1.set("Select entry ID")
        drop1 = OptionMenu(self.root, clicked1, *numbers_list)
        drop1.grid(row=10, column=0)

        options = StringVar(self.root)
        options.set("Select product")
        drop3 = OptionMenu(self.root, options, *my_list)
        drop3.grid(row=10, column=1)

        clicked2 = StringVar(self.root)
        clicked2.set("Select qty")
        drop2 = OptionMenu(self.root, clicked2, *numbers_list)
        drop2.grid(row=10, column=2)

#  saving result
        def save_result():
            save_result_list = []

            save_result_list.append(clicked1.get())
            save_result_list.append(options.get())
            save_result_list.append(clicked2.get())

            search_value = save_result_list[0]
            amend_value_product = save_result_list[1]
            amend_value_qty = save_result_list[2]
            print(search_value)
            print(amend_value_product)
            print(amend_value_qty)

            opened_file2 = filedialog.askopenfilename(
                initialdir="C:\Python\Project 0.1", title="Select a file")
            print("Function open read:")
            print(opened_file2)
            self.filename = opened_file2

# get the price from products DB based on the chosen product and add it to the list save+result_list
            query2 = "SELECT product_price FROM products WHERE product_name=?"
            cursor_DB.execute(query2, (amend_value_product,))
            find_price = cursor_DB.fetchall()
            find_price_str = str(find_price).strip('[]')
            amend_value_price_per_1_unit = find_price_str.replace(
                "(","").replace(',','').replace(')','')
            print(amend_value_price_per_1_unit)

            save_result_list.append(amend_value_price_per_1_unit)
            print(save_result_list)

# creating empty lists for product update
            List_for_amendments_CSV_file_No = []
            List_for_amendments_CSV_file_Customer = []
            List_for_amendments_CSV_file_Supplier = []
            List_for_amendments_CSV_file_Customer_address = []
            List_for_amendments_CSV_file_Product = []
            List_for_amendments_CSV_file_Quantity = []
            List_for_amendments_CSV_file_Price_Per_1_unit = []
            List_for_amendments_CSV_file_Total_cost = []

            open_choose_file_in_GUI = open(opened_file2, encoding="UTF8")
            main_CSV_file_read_to_be_amended = csv.DictReader(
                open_choose_file_in_GUI
            )

# iterating over each row and append values to empty list
            for col in main_CSV_file_read_to_be_amended:
                List_for_amendments_CSV_file_No.append(col['No'])
                List_for_amendments_CSV_file_Customer.append(col['Customer'])
                List_for_amendments_CSV_file_Supplier.append(col['Supplier'])
                List_for_amendments_CSV_file_Customer_address.append(
                    col['Customer address'])
                List_for_amendments_CSV_file_Product.append(col['Product'])
                List_for_amendments_CSV_file_Quantity.append(col['Quantity'])
                List_for_amendments_CSV_file_Price_Per_1_unit.append(
                    col['Price Per 1 unit'])
                List_for_amendments_CSV_file_Total_cost.append(
                    col['Total cost'])

            print('No', List_for_amendments_CSV_file_No)
            print('Product',  List_for_amendments_CSV_file_Product)
            print('Quantity', List_for_amendments_CSV_file_Quantity)
            print(
                 'Price Per 1 unit',
                 List_for_amendments_CSV_file_Price_Per_1_unit
                )

            search_value_No_index_in_old_CSV_file = List_for_amendments_CSV_file_No.index(search_value)
            print(search_value_No_index_in_old_CSV_file)

            List_for_amendments_CSV_file_Product = (List_for_amendments_CSV_file_Product[:search_value_No_index_in_old_CSV_file]
                +[amend_value_product]+List_for_amendments_CSV_file_Product[search_value_No_index_in_old_CSV_file+1:])
            List_for_amendments_CSV_file_Quantity = (List_for_amendments_CSV_file_Quantity[:search_value_No_index_in_old_CSV_file]
                +[amend_value_qty]+List_for_amendments_CSV_file_Quantity[search_value_No_index_in_old_CSV_file+1:])
            List_for_amendments_CSV_file_Price_Per_1_unit = (List_for_amendments_CSV_file_Price_Per_1_unit
                [:search_value_No_index_in_old_CSV_file]+[amend_value_price_per_1_unit]+List_for_amendments_CSV_file_Price_Per_1_unit
                        [search_value_No_index_in_old_CSV_file+1:])

            print(List_for_amendments_CSV_file_Product)
            print(List_for_amendments_CSV_file_Quantity)
            print(List_for_amendments_CSV_file_Price_Per_1_unit)

            d = [
                List_for_amendments_CSV_file_No,
                List_for_amendments_CSV_file_Customer,
                List_for_amendments_CSV_file_Supplier,
                List_for_amendments_CSV_file_Customer_address,
                List_for_amendments_CSV_file_Product,
                List_for_amendments_CSV_file_Quantity,
                List_for_amendments_CSV_file_Price_Per_1_unit,
                List_for_amendments_CSV_file_Total_cost
            ]

            export_data = zip_longest(*d, fillvalue='')

            with open(
                 'Updated 3.3 qty and ppu.csv', 'w',
                 encoding="utf8", newline=''
                 ) as myfile:
                wr = csv.writer(myfile)
                wr.writerow((
                     "No", "Customer","Supplier","Customer address", "Product",
                     "Quantity", "Price Per 1 unit", "Total cost"))
                wr.writerows(export_data)
                myfile.close

            save_result_list.clear
            print(save_result_list)

        myButton2 = Button(self.root, text="Save", command=save_result)
        myButton2.grid(row=11, column=0)

        self.root.mainloop()

    def choose_file(self):
        global df_dataALL_global
        opened_file = filedialog.askopenfilename(
            initialdir="C:\Python\Project 0.1", title="Select a file")
        print("Function open read:")
        print(opened_file)
        self.filename = opened_file

        df_dataALL = pandas.read_csv(opened_file, encoding="utf8")
        customer_address_list = df_dataALL["Customer address"].tolist()
        print(customer_address_list)

# check data with API
        updated_customer_address_list = []

        for n in customer_address_list:
            address_info_updated = dadata.clean(
                 "address", n)["result"], dadata.clean(
                      "address", n)["postal_code"]
            updated_customer_address_list.append(address_info_updated)
            print(updated_customer_address_list)

#  using generated clean list and adding it as a new column to the original CSV file
        df_dataALL.insert(
             4, "Customer address updated", updated_customer_address_list, True
            )
        print(df_dataALL)

        df_dataALL = pandas.read_csv(opened_file, encoding="utf8")
        print(df_dataALL['Quantity'])
        print(df_dataALL['Price Per 1 unit'])
        df_dataALL["Total cost"] = df_dataALL['Quantity']*df_dataALL['Price Per 1 unit']
        print(df_dataALL)

        open_choose_file_in_GUI = open(opened_file, encoding="UTF8")
        reader_choose_file_in_GUI = csv.reader(open_choose_file_in_GUI)
        data_from_choose_file_in_GUI = list(reader_choose_file_in_GUI)

# Grab all column infomration
        list_in_GUI_data_from_choose_file_in_GUI_no = []
        for no in range(1, len(data_from_choose_file_in_GUI)):
            list_in_GUI_data_from_choose_file_in_GUI_no.append(
                data_from_choose_file_in_GUI[no][0])

        var_list_no = StringVar(
            value=list_in_GUI_data_from_choose_file_in_GUI_no)
        no_list = Listbox(self.root, listvariable=var_list_no)
        no_list.grid(row=3, column=0)

        list_in_GUI_data_from_choose_file_in_GUI_customer = []
        for customer in range(1, len(data_from_choose_file_in_GUI)):
            list_in_GUI_data_from_choose_file_in_GUI_customer.append(
                data_from_choose_file_in_GUI[customer][1])

        var_list_customer = StringVar(
            value=list_in_GUI_data_from_choose_file_in_GUI_customer)
        customer_list = Listbox(self.root, listvariable=var_list_customer)
        customer_list.grid(row=3, column=1)

        list_in_GUI_data_from_choose_file_in_GUI_supplier = []
        for supplier in range(1, len(data_from_choose_file_in_GUI)):
            list_in_GUI_data_from_choose_file_in_GUI_supplier.append(
                data_from_choose_file_in_GUI[supplier][2])

        var_list_supplier = StringVar(
             value=list_in_GUI_data_from_choose_file_in_GUI_supplier)
        supplier_list = Listbox(self.root, listvariable=var_list_supplier)
        supplier_list.grid(row=3, column=2)

        var_list_customers_address = StringVar(
             value=updated_customer_address_list)
        customer_address_list = Listbox(
             self.root, listvariable=var_list_customers_address)
        customer_address_list.grid(row=3, column=3)

        list_in_GUI_data_from_choose_file_in_GUI_product = []
        for product in range(1, len(data_from_choose_file_in_GUI)):
            list_in_GUI_data_from_choose_file_in_GUI_product.append(
                 data_from_choose_file_in_GUI[product][4])

        var_list_product = StringVar(
             value=list_in_GUI_data_from_choose_file_in_GUI_product)
        product_list = Listbox(self.root, listvariable=var_list_product)
        product_list.grid(row=3, column=4)

        list_in_GUI_data_from_choose_file_in_GUI_quantity = []
        for quantity in range(1, len(data_from_choose_file_in_GUI)):
            list_in_GUI_data_from_choose_file_in_GUI_quantity.append(
                 data_from_choose_file_in_GUI[quantity][5])

        var_list_quantity = StringVar(
             value=list_in_GUI_data_from_choose_file_in_GUI_quantity)
        quantity_list = Listbox(self.root, listvariable=var_list_quantity)
        quantity_list.grid(row=3, column=5)
        print(var_list_quantity)

        # price per 1 unit = ppu
        list_in_GUI_data_from_choose_file_in_GUI_ppu = []
        for ppu in range(1, len(data_from_choose_file_in_GUI)):
            list_in_GUI_data_from_choose_file_in_GUI_ppu.append(
                 data_from_choose_file_in_GUI[ppu][6])

        var_list_ppu = StringVar(
             value=list_in_GUI_data_from_choose_file_in_GUI_ppu)
        ppu_list = Listbox(self.root, listvariable=var_list_ppu)
        ppu_list.grid(row=3, column=6)

        list_in_GUI_data_from_choose_file_in_GUI_total_cost = df_dataALL["Total cost"].values.tolist()
        print(list_in_GUI_data_from_choose_file_in_GUI_total_cost)

        var_list_total_cost = StringVar(
             value=list_in_GUI_data_from_choose_file_in_GUI_total_cost)
        print(var_list_total_cost)
        total_cost_list = Listbox(self.root, listvariable=var_list_total_cost)
        total_cost_list.grid(row=3, column=7)

        df_dataALL_global = df_dataALL

    def upload(self):
        try:
            conn = mysql.connector.connect(
                host=os.getenv('HOST'), user=os.getenv('USER'),
                password=os.getenv('PASSWORD'), database=os.getenv('DATABASE'))
            if conn.is_connected():
                cursor_MYSQL = conn.cursor()
                cursor_MYSQL.execute("select database();")
                record = cursor_MYSQL.fetchone()
                print("You're connected to database: ", record)
                cursor_MYSQL.execute('DROP TABLE IF EXISTS gmp_orders;')
                print('Creating table....')
                cursor_MYSQL.execute("""CREATE TABLE gmp_orders (no int primary key, customer VARCHAR(255),
                 supplier VARCHAR (255), customers_address VARCHAR (255), product VARCHAR (255), quantity int (255),
                price_per_1_unit int (255), total_cost int (255))""")
                print("Table is created....")

                for i, row in df_dataALL_global.iterrows():
                    sql = "INSERT INTO test_gmp.gmp_orders VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
                    cursor_MYSQL.execute(sql, tuple(row))
                    print("Record inserted")
                    conn.commit()
        except Error as e:
            print("Error while connecting to MySQL", e)


GUI()
