import sqlite3
import da

"""CRUD --- Create Read Update Delete"""

""" conn is our connection """
# conn = sqlite3.connect("model.db")

""" Creating a cursor """
# c = conn.cursor()

""" Type of data """
# NULL
# INTEGER
# REAL
# TEXT
# BLOB

""" Creating a table """
# c.execute("""CREATE TABLE customers (
#             First_name TEXT,
#             last_name TEXT,
#             email TEXT
#           )""")


""" Rename a table """
# c.execute("ALTER TABLE customers RENAME TO Allison")

""" inserting a value """
# c.execute("INSERT INTO customers VALUES('Tim', 'Smith', 'TimSmith@hotmail.com')")


""" inserting many values """
# many_customers=[
              #  ('allison','bonfim','Allisonbonfim@hotamil.com'),
              #  ('allison2','bonfim2','Allisonbonfim@hotamil.com')
              # ]
# c.executemany("INSERT INTO customers VALUES (?,?,?)", many_customers)


""" Update values """
# c.execute(""" UPDATE customers SET first_name = 'Allison'
#               WHERE rowid = 1
#           """)



""" Getting collumns name """
# c.execute("SELECT * from sqlite_master")


""" Adding a new collumns """
# c.execute("ALTER TABLE customers ADD COLUMN Address varchar(32)")


""" Getting and printing the ID and the values """
# c.execute("SELECT rowid, * FROM customers ORDER by rowid ASC LIMIT 2")
# print(c.fetchone())
# print(c.fetchmany(2))
# print(c.fetchall())


""" Finding a specefic value """
# c.execute("SELECT rowid, * FROM customers WHERE first_name LIKE '%llison' AND last_name LIKE 'bon%'")
# c.execute("SELECT rowid, * FROM customers WHERE 'age' >= 18")
# print(c.fetchall())


""" Deleting values """
# c.execute("DELETE from customers WHERE rowid = 4")


""" Drop a table """
# c.execute("DROP TABLE customers")
#
# c.execute("DROP")

""" commiting and closing the connection"""
# conn.commit()
# conn.close()

# c.execute("ALTER TABLE Allison DROP COLUMN Address")


class DataBase():
    def __init__(self, data_base_name):
        self.data_base_name = data_base_name
        self.connection = sqlite3.connect(f"{self.data_base_name}.db")   # conn is our connection 
        self.cursor = self.connection.cursor()  # Creating a cursor 
        

#"""""""""""""""""""""""""""" Table modules """"""""""""""""""""""""""""
    def create_instance(self, instance_name, attributes = "Name TEXT"): 
        """ This function create a instance in our database

        Args:
            instance_name (str): the name of the instance
            new_name (str): the name of the attributes of the instance, it will be separeted by comma 
            and their are usually "TEXT" or "REAL" variables
        """      
        self.cursor.execute(f"CREATE TABLE {instance_name} ({str(attributes)})")
        self.connection.commit()


    def rename_instance(self, old_instance_name, new_instance_name):
        self.cursor.execute(f"ALTER TABLE {old_instance_name} RENAME TO {new_instance_name}")
        self.connection.commit()


    def drop_instance(self, table):
        # Droping a table
        self.cursor.execute(f"DROP TABLE {table}")
        self.connection.commit()


#"""""""""""""""""""""""""""" Column modules """"""""""""""""""""""""""""
    def drop_attribute(self, table, column):
        # droping a column
        self.cursor.execute(f"ALTER TABLE {table} DROP COLUMN {column}")
        self.connection.commit()


#"""""""""""""""""""""""""""" Values modules """"""""""""""""""""""""""""
    def insert_value(self, table, values):
        # Inserting values
        self.cursor.execute(f"INSERT INTO {table} VALUES ({values})")
        self.connection.commit()


    def get_values(self, table):
        # Query the DataBase table and return all records
        self.cursor.execute(f"SELECT rowid, * FROM {table}")
        return self.cursor.fetchall()


    def delete_value(self, table, rowid):
        self.cursor.execute(f"DELETE from {table} WHERE rowid = {rowid}")



#"""""""""""""""""""""""""""" Closing connetion """"""""""""""""""""""""""""
    def close_connection(self):
        self.connection.close()




# d1.create_table("tabela")
# d1.insert_value("tabela", 4)
# print(d1.get_values("tabela"))
# d1.delete_value("tabela", 3)

d = da.File(file_name="Testing", extension="db", path ="/home/allison/Desktop/Code/Studing/")
d.delete_file()
# d = DataBase("Testing")
# d.create_instance("Client", attributes="Name TEXT, Idade REAL")
# d.close_connection()