import mysql.connector

class DBConnect:
    def __init__(self, host, user, password, database):
        try:
            self.connection = mysql.connector.connect(
                host=host,
                user=user,
                password=password,
                database=database
            )
            self.cursor = self.connection.cursor()
            print("Database connection successful.")
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            self.connection = None
            self.cursor = None

    def close_connection(self):
        if self.connection:
            self.cursor.close()
            self.connection.close()
            print("Database connection closed.")

    def execute_query(self, query, params=None):
        if not self.connection:
            print("No active database connection.")
            return None
        try:
            self.cursor.execute(query, params)
            self.connection.commit()
            print("Query executed successfully.")
        except mysql.connector.Error as err:
            print(f"Error: {err}")

    def fetch_results(self):
        if not self.cursor:
            print("No active cursor available.")
            return None
        return self.cursor.fetchall()




db = DBConnect(
    host='localhost',
    user='root',
    password='1234',
    database='libraryManagementSystem'
)