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
            # Optionally, raise the exception to handle it elsewhere
            raise

    def disconnect(self):
        if self.connection:
            self.connection.close()
            print("Disconnected from the database")

# Example usage to check connection
if __name__ == "__main__":
    db_connection = DBConnection(host='localhost', username='root', password='root', database='python')
    try:
        db_connection.connect()
        # If connection is successful, continue with further operations
        # For example:
        # db_interaction = DBInteraction(db_connection)
        # db_interaction.read_records('users')
    except Exception as e:
        print("Failed to connect to the database:", e)
    finally:
        db_connection.disconnect()
        

      #####################################################################################
class DBInteraction:
    def __init__(self, db_connection):
        self.connection = db_connection.connection

    def create_record(self, table, data):
        cursor = self.connection.cursor()
        columns = ', '.join(data.keys())
        values_template = ', '.join(['%s'] * len(data))
        query = f"INSERT INTO {table} ({columns}) VALUES ({values_template})"
        try:
            cursor.execute(query, list(data.values()))
            self.connection.commit()
            print("Record inserted successfully")
        except mysql.connector.Error as err:
            print(f"Error: {err}")
        finally:
            cursor.close()

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

    def delete_record(self, table, record_id):
        cursor = self.connection.cursor()
        query = f"DELETE FROM {table} WHERE id = %s"
        try:
            cursor.execute(query, (record_id,))
            self.connection.commit()
            print("Record deleted successfully")
        except mysql.connector.Error as err:
            print(f"Error: {err}")
        finally:
            cursor.close()

# Example usage to perform CRUD operations
if __name__ == "__main__":
    db_connection = DBConnection(host='localhost', username='root', password='root', database='python')
    try:
        db_connection.connect()
        
        # Perform CRUD operations
        db_interaction = DBInteraction(db_connection)
        
        # Create a record
        data_to_insert = {'name': 'John', 'age': 30, 'email': 'john@example.com'}
        db_interaction.create_record('users', data_to_insert)

        # Read records
        records = db_interaction.read_records('users')
        print("Records:", records)

        # Update a record
        record_id_to_update = 1
        data_to_update = {'name': 'Jane', 'age': 25, 'email': 'jane@example.com'}
        db_interaction.update_record('users', record_id_to_update, data_to_update)

        # Delete a record
        record_id_to_delete = 1
        db_interaction.delete_record('users', record_id_to_delete)
        
    except Exception as e:
        print("Failed to perform database operations:", e)
    finally:
        db_connection.disconnect()