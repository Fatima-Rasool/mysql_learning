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

    def update_record(self, table, record_id, data):
        cursor = self.connection.cursor()
        set_values = ', '.join([f"{key} = %s" for key in data.keys()])
        query = f"UPDATE {table} SET {set_values} WHERE id = %s"
        try:
            cursor.execute(query, list(data.values()) + [record_id])
            self.connection.commit()
            print("Record updated successfully")
        except mysql.connector.Error as err:
            print(f"Error: {err}")
        finally:
            cursor.close()

if __name__ == "__main__":
    db_connection = DBConnection(host='localhost', username='root', password='root', database='python')
    try:
        db_connection.connect()
        db_interaction = DBInteraction(db_connection)
        
        # Data to update in the 'users' table for record with id 4
        data_to_update = {'name': 'Updated Name', 'age': 40, 'email': 'updated@example.com'}

        # Updating record with id 4 in the 'users' table
        db_interaction.update_record('users', 6, data_to_update)
        
    except Exception as e:
        print("Failed to update record:", e)
    finally:
        db_connection.disconnect()
