#Server Connection to MySQL:

import MySQLdb
conn = MySQLdb.connect(host= "localhost",
                  user="Marwanibrahim",
                  passwd="eshtaholdings",
                  db="eshta")
x = conn.cursor()

data="img/yaleDatabase/subject2.sleepy"

try:
   x.execute("INSERT INTO subject2 VALUES (%s,%s)",(data,123456789))
   conn.commit()
except:
   conn.rollback()

conn.close()

#sql =  "INSERT INTO PERSON (F_NAME, L_NAME, Age, Gender) VALUES (%s, %s, %s, %s)" %(f_name, l_name, age, gender) 
