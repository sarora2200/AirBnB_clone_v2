import MySQLdb

# Establish a connection to the MySQL database
connection = MySQLdb.connect(
    user="hbnb_test",
    passwd="hbnb_test_pwd",
    host="localhost",
    db="hbnb_test_db"
)

# Create a cursor object to execute queries
cursor = connection.cursor()

# Execute a query to get the updated number of records
cursor.execute("SELECT COUNT(*) FROM states")
result = cursor.fetchone()  # Fetch the first row of the result

# Get the count from the result
updated_record_count = result[0]

# Close the cursor and the database connection
cursor.close()
connection.close()
