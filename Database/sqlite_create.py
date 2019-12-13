# This Python file uses the following encoding: utf-8
import sqlite3

conn = sqlite3.connect('/web/Sqlite-Data/example.db')

c = conn.cursor()
c.execute('''
          CREATE TABLE Customer
          (id INTEGER PRIMARY KEY ASC, name varchar(250) NOT NULL)
          ''')
c.execute('''
          CREATE TABLE Item
          (id INTEGER PRIMARY KEY ASC, name varchar(250), cost_price FLOAT NOT NULL,
           selling_price FLOAT NOT NULL, quantity INTEGER NOT NULL,
           FOREIGN KEY(customer_id) REFERENCES customer(id))
          ''')

c.execute('''
          INSERT INTO customer VALUES(1, 'pythoncentral')
          ''')
c.execute('''
          INSERT INTO item VALUES(1, 'python road', '1', '00000', 1)
          ''')

conn.commit()
conn.close()
