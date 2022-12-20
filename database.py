# -*- coding: utf-8 -*-
"""
Created on Mon Oct 11 14:46:42 2021

@author: Sathish
"""
import sqlite3

conn = sqlite3.connect('temperature6.db')
print("Opened database successfully")

conn.execute('''CREATE TABLE TEMPDATA5
         (YEAR INT PRIMARY KEY     NOT NULL,
         MEDIAN           FLOAT    NOT NULL,
         UPPER            FLOAT     NOT NULL,
         LOWER        FLOAT);''')
print("Table created successfully")

conn.close()
y=[]
m=[]
u=[]
lo=[]
l1=[]
with open('temperature.txt') as f:
    lines=f.readlines()



  
for i in range(1,len(lines)):
    
   
        l1=lines[i].split()
        y.append(int(l1[0]))
        m.append(float(l1[1]))
        u.append(float(l1[2]))
        lo.append(float(l1[3]))
print(y[1])

import sqlite3

print("Opened database successfully")

for i in range(len(lines)-1):
    conn = sqlite3.connect('temperature6.db')
    
    yy=y[i]
    mm=m[i]
    uu=u[i]
    loo=lo[i]
    conn.execute("INSERT INTO TEMPDATA5 (YEAR,MEDIAN,UPPER,LOWER) \
                    VALUES (?, ?, ?, ?)",(yy, mm, uu, loo))
    conn.commit()
       
    conn.close()
    

print("Records created successfully")