import mysql.connector

class DBConnection:
    def __init__(self, host, username, password, database):
        self.host = host
        self.username = username
        self.password = password
        self.database = database
        self.connection = None

    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.username,
                password=self.password,
                database=self.database
            )
            print("Connected to the database")
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            raise

    def disconnect(self):
        if self.connection:
            self.connection.close()
            print("Disconnected from the database")

class DBInteraction:
    def __init__(self, db_connection):
        self.connection = db_connection.connection

    def read_records(self, table, columns=None):
        cursor = self.connection.cursor()
        if not columns:
            columns = '*'
        else:
            columns = ', '.join(columns)
        query = f"SELECT {columns} FROM {table}"
        try:
            cursor.execute(query)
            records = cursor.fetchall()
            return records
        except mysql.connector.Error as err:
            print(f"Error: {err}")
        finally:
            cursor.close()

if __name__ == "__main__":
    db_connection = DBConnection(host='localhost', username='root', password='root', database='python')
    try:
        db_connection.connect()
        db_interaction = DBInteraction(db_connection)
        
        # Reading all records from the 'users' table
        users_data = db_interaction.read_records('users')
        print("Users data:", users_data)
        
    except Exception as e:
        print("Failed to read records:", e)
    finally:
        db_connection.disconnect()
