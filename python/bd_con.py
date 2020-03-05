import matplotlib.pyplot as plt
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="root",
  database="testdb"
)
#virtualenv -p python3 sqlenv


mycursor = mydb.cursor()

mycursor.execute("SELECT qty FROM Book")
quantities = mycursor.fetchall()

mycursor.execute("SELECT title FROM Book")
titles = mycursor.fetchall()

# mycursor.execute("SELECT title FROM Book")

# titles = mycursor.fetchall()

# print(type(myresult))
# myresult = list()

q = []
title = []
# for i in quantities:     
#   qty.append(i)

for x in quantities:
  q.append(x[0])
  print(x)

for x in titles:
  title.append(x[0])  

print(q)
print(title)

name = title
data = q

plt.pie(data, labels=name, autopct='%.3f', startangle=90, shadow=True)
plt.axis('equal')
plt.show()
 