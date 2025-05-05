# Python Scripting: Database initiation
import sqlite3
import pandas as pd


#use SQLite3 to create and connect your process to a new database STAFF using the following statements.
conn = sqlite3.connect('STAFF.db')

# Create and Load the Staff table
table_name = 'INSTRUCTOR'
attribute_list = ['ID', 'FNAME', 'LNAME', 'CITY', 'CCODE']

# Reading the CSV file
file_path = './INSTRUCTOR.csv'
df = pd.read_csv(file_path, names = attribute_list)

# Loading the data to a table
df.to_sql(table_name, conn, if_exists = 'replace', index =False)
print('Table is ready')

#Running basic queries on data
# 1: Viewing all the data in the table.
query_statement = f"SELECT * FROM {table_name}"
query_output = pd.read_sql(query_statement, conn)
print(query_statement)
print(query_output)

# 2: Viewing only FNAME column of data.
query_statement = f"SELECT FNAME FROM {table_name}"
query_output = pd.read_sql(query_statement, conn)
print(query_statement)
print(query_output)

# 3: Viewing the total number of entries in the table.
query_statement = f"SELECT COUNT(*) FROM {table_name}"
query_output = pd.read_sql(query_statement, conn)
print(query_statement)
print(query_output)

# 4: Appending some data to the table - create the dataframe of the new data.
data_dict = {'ID' : [100],
            'FNAME' : ['John'],
            'LNAME' : ['Doe'],
            'CITY' : ['Paris'],
            'CCODE' : ['FR']}
data_append = pd.DataFrame(data_dict)

# append the data to the INSTRUCTOR table.
data_append.to_sql(table_name, conn, if_exists = 'append', index =False)
print('Data appended successfully')

# add the command to close the connection to the database after all the queries are executed.
conn.close()