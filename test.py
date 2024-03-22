# # import pymysql
# # # mypass = 7568

# # # mydatabase="db"

# # con = pymysql.connect(host="localhost",user="root",password=7568,database="db")

# import pymysql
# import hashlib

# # Check if the password is properly encoded
# password = "7568"
# encoded_password = password.encode('utf-8')

# # Assuming mypass and mydatabase are properly defined elsewhere in your code
# con = pymysql.connect(host="localhost", user="root", password=encoded_password, database="db")

# # Rest of your code...
import pymysql

# Connect to MySQL database
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='7568',
                             database='db')

try:
    # Create a cursor object
    with connection.cursor() as cursor:
        # SQL query to describe the table
        sql_query = "DESCRIBE books_issued"

        # Execute the SQL query
        cursor.execute(sql_query)

        # Fetch all the results
        table_description = cursor.fetchall()

        # Print the table description
        for column in table_description:
            print(column)

finally:
    # Close the connection
    connection.close()
