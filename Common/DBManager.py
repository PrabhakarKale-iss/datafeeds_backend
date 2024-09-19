from flask_mysqldb import MySQL
from flask import jsonify

class DBManager:
    def __init__(self, app):
        """Initialize DBManager with the Flask app context."""
        self.conn = None
        self.cursor = None
        self.mysql = MySQL(app)
    
    def connect(self):
        try:
            self.conn = self.mysql.connection
            self.cursor = self.conn.cursor()
            print("Database connection successful.")
        except Exception as e:
            print(f"Error connecting to the database: {e}")
            
    def disconnect(self):
        """Close the cursor."""
        if self.cursor:
            self.cursor.close()
            print("Database cursor closed.")
            
    def fetch_all(self, query, params=None):
        """Fetch all rows from the executed query."""
        try:
            self.connect()
            if params:
                self.cursor.execute(query, params)
            else:
                self.cursor.execute(query)
            result = self.cursor.fetchall()
            self.disconnect()
            return result
        except Exception as e:
            print(f"Error fetching data: {e}")
            return None

    def fetch_one(self, query, params=None):
        """Fetch a single row from the executed query."""
        try:
            self.connect()
            if params:
                self.cursor.execute(query, params)
            else:
                self.cursor.execute(query)
            result = self.cursor.fetchone()
            self.disconnect()
            return result
        except Exception as e:
            print(f"Error fetching data: {e}")
            return None

    def insert_update_delete(self, query, params):
        """Perform insert, update, or delete operation."""
        try:
            self.connect()
            self.cursor.execute(query, params)
            self.conn.commit()
            self.disconnect()
            print("Insert/Update/Delete operation successful.")
        except Exception as e:
            print(f"Error executing operation: {e}")
            
    
    def fetch_data_to_json(self, query, params=None):
        try:
            self.connect()
            if params:
                self.cursor.execute(query, params)
            else:
                self.cursor.execute(query)
            columns = [description[0] for description in self.cursor.description]
            datafeeds = self.cursor.fetchall()
            result = []
            if datafeeds:
                result = [dict(zip(columns, row)) for row in datafeeds] 
            self.disconnect()
            return result
        
        except Exception as e:
            print(f"Error fetching data: {e}")
            return None
        