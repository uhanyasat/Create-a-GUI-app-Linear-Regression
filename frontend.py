
import sqlite3
global year,median,upper,lower
year=[]
median=[]
upper=[]
lower=[]
conn = sqlite3.connect('temperature6.db')
print("Opened database successfully")

cursor = conn.execute("SELECT YEAR,MEDIAN,UPPER,LOWER from TEMPDATA5")
for row in cursor:
   year.append(row[0])
   median.append(row[1])
   upper.append(row[2])
   lower.append(row[3])
    
   print("YEAR = ", row[0])
   print("MEDIAN = ", row[1])
   print("UPPER = ", row[2])
   print("LOWER = ", row[3], "\n")

print("Operation done successfully")
conn.close()
from tkinter import *
import numpy as np
import matplotlib.pyplot as plt

#Create an instance of Tkinter frame
win= Tk()

#Set the geometry of tkinter frame
win.geometry("100x250")

def graph():
   plt.figure()
   plt.plot(year, upper, label = "Upper")
# plotting the line 2 points
   plt.plot(year, median, label = "Median")

   plt.plot(year, lower, label = "Lower")
   # naming the x axis
   plt.xlabel('Years')
# naming the y axis
   plt.ylabel('Temperature in Celsius')
# giving a title to my graph
   plt.title('Average Temperature Anamoly,Global!')
 
# show a legend on the plot
   plt.legend()
 
 
   plt.show()

def graph1():
   plt.figure()
   
   plt.bar(year, upper, color ='r')
   plt.legend('upper')
   plt.bar(year, median, color ='g')
   plt.legend('median')
   plt.bar(year, lower, color ='b')
   plt.legend('lower')
   # naming the x axis
   plt.xlabel('Years')
# naming the y axis
   plt.ylabel('Temperature in Celsius')
# giving a title to my graph
   plt.title('Average Temperature Anamoly,Global!')
 
# show a legend on the plot
   
 
 
   plt.show()
   


from scipy import stats


def graph2():
    global slope,intercept
    x=year
    y=upper
	
    slope, intercept, r, p, std_err = stats.linregress(x, y)

    def myfunc(x):
        return slope * x + intercept

    mymodel = list(map(myfunc,x))
    plt.figure()
    plt.scatter(x, y,color ='g')
    plt.plot(x, mymodel,color ='r')
    plt.legend('Upper')
       # naming the x axis
    plt.xlabel('Years')
    # naming the y axis
    plt.ylabel('Temperature in Celsius for Upper')
    # giving a title to my graph
    plt.title('Linear Regression Graph!')
    plt.show()
    global slope1,intercept1
    x=year
    y=lower
	
    slope1, intercept1, r, p, std_err = stats.linregress(x, y)

    def myfunc1(x):
        return slope1 * x + intercept1

    mymodel1 = list(map(myfunc1,x))
    plt.figure()
    plt.scatter(x, y,color ='g')
    plt.plot(x, mymodel1,color ='r')
    plt.legend('Lower')
       # naming the x axis
    plt.xlabel('Years')
    # naming the y axis
    plt.ylabel('Temperature in Celsius for Lower')
    # giving a title to my graph
    plt.title('Linear Regression Graph!')
    plt.show()
	
    global slope2,intercept2
    x=year
    y=median
	
    slope2, intercept2, r, p, std_err = stats.linregress(x, y)

    def myfunc2(x):
        return slope2 * x + intercept2

    mymodel2 = list(map(myfunc2,x))
    plt.figure()
    plt.scatter(x, y,color ='g')
    plt.plot(x, mymodel2,color ='r')
    plt.legend('Median')
       # naming the x axis
    plt.xlabel('Years')
    # naming the y axis
    plt.ylabel('Temperature in Celsius for MEdian')
    # giving a title to my graph
    plt.title('Linear Regression Graph!')
    plt.show()
	
    

#Create a button to show the plot
Button(win, text= "X-Y Plot", command= graph).pack(pady=20)
Button(win, text= "Bar Graph", command= graph1).pack(pady=20)
Button(win, text= "Linear Regression", command= graph2).pack(pady=20)

win.mainloop()