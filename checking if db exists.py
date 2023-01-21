import pandas as pd
import mysql.connector
from mysql.connector import Error


# Connect to MYSQL Server and create DB
try:
    conn = mysql.connector.connect(host = 'localhost', user = 'root', 
    password = 'Lenin5416770', database = 'test_gmp')
    if conn.is_connected():
        cursor_MYSQL = conn.cursor()
        print ('Connected to DB')
except:
        conn = mysql.connector.connect(host = 'localhost', user = 'root', 
    password = 'Lenin5416770')
        cursor_MYSQL = conn.cursor()
        cursor_MYSQL.execute("CREATE DATABASE test_gmp")
        print ("Created DB")