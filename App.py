from flask import Flask, jsonify
from flask_cors import CORS
from flask_mysqldb import MySQL
from config import Config

app = Flask(__name__)

app.config['MYSQL_HOST'] = Config.MYSQL_HOST
app.config['MYSQL_USER'] = Config.MYSQL_USER
app.config['MYSQL_PASSWORD'] = Config.MYSQL_PASSWORD
app.config['MYSQL_DB'] = Config.MYSQL_DB
# app.config['MYSQL_CURSORCLASS'] = Config.MYSQL_CURSORCLASS

# Initialize MySQL
mysql = MySQL(app)


# API to retrieve all datafeeds
@app.route('/api/datafeeds', methods=['GET'])
def get_datafeeds():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM datafeed_table')  # Replace with your table name
    datafeeds = cur.fetchall()
    cur.close()
    return jsonify(datafeeds)



if __name__ == '__main__':
    app.run(debug=True)

# import mysql.connector
# Configure MySQL using config.py

# # Database connection details
# hostname = "central.discoveryco.com"
# username = "pkale"
# password = "rtSuT7yG6RYB8mCV"
# database = "pkale"

# try:
#     # Establish a connection to the database
#     connection = mysql.connector.connect(
#         host=hostname,
#         user=username,
#         password=password,
#         database=database
#     )

#     if connection.is_connected():
#         print("Connected to MySQL database")

#         # Create a cursor to execute SQL queries
#         cursor = connection.cursor()

#         # Write the query to retrieve data
#         query = "SELECT * FROM client_company"

#         # Execute the query
#         cursor.execute(query)

#         # Fetch all the rows from the executed query
#         results = cursor.fetchall()

#         # Loop through the results and print each row
#         for row in results:
#             print(row)

# except mysql.connector.Error as err:
#     print(f"Error: {err}")

# finally:
#     if connection.is_connected():
#         cursor.close()
#         connection.close()
#         print("MySQL connection is closed")