import MySQLdb

#taking the path of the stored img (ex:computer) and mobile number from the server:
#assuming taking it from the user through the terminal
path = raw_input('Enter path: ')
mobile_number = raw_input('Enter mobile phone: ')


# Open database connection ( If database is not created don't give dbname)
db = MySQLdb.connect("localhost","Marwanibrahim","eshtaholdings","eshta" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

# For creating create db
# Below line  is hide your warning 
cursor.execute("SET sql_notes = 0; ")
# create db here.... if we need to
#cursor.execute("create TABLE IF NOT EXISTS Eshta")

#'CREATE DATABASE chom'

# create table 
cursor.execute("SET sql_notes = 0; ")
cursor.execute("create TABLE IF NOT EXISTS Subject2 (photo_path varchar(70),mobile_phone varchar(20));")
cursor.execute("SET sql_notes = 1; ")

#insert data
#cursor.execute("insert into test (photo_path,mobile_phone) values('test@gmail.com','test')")
insert_stmt = (
  "INSERT INTO Subject2 (photo_path, mobile_phone) "
  "VALUES (%s, %s)"
)
data = (path,mobile_number)
cursor.execute(insert_stmt, data)

# Commit your changes in the database
db.commit()

# disconnect from server
db.close()
