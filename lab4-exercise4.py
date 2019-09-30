#!/usr/bin/env python3
import sqlite3
#connect to database file
dbconnect = sqlite3.connect("lab4-exercise4.db");
#If we want to access columns by name we need to set
#row_factory to sqlite3.Row class
dbconnect.row_factory = sqlite3.Row;
#now we create a cursor to work with db
cursor = dbconnect.cursor();
#execute select statement for kitchen
cursor.execute('SELECT * FROM ex4 WHERE zone = "kitchen"');
#print kitchen data
for row in cursor:
    print(row['sensorID'],row['type'],row['zone']);
#execute select statement for door
cursor.execute('SELECT * FROM ex4 where type = "door"');
#print door data
for row in cursor:
    print(row['sensorID'],row['type'],row['zone']);

#close the connection
dbconnect.close();
