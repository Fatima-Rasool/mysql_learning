import mysql.connector
from test import DBConnection, DBInteraction
class DBInteraction:
    def __init__(self, db_connection):
        self.connection = db_connection.connection

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

if __name__ == "__main__":
    db_connection = DBConnection(host='localhost', username='root', password='root', database='python')
    try:
        db_connection.connect()
        db_interaction = DBInteraction(db_connection)
        
        # Deleting record with id 4 from the 'users' table
        db_interaction.delete_record('users', 3)
    except Exception as e:
        print("Failed to delete record:", e)
    finally:
        db_connection.disconnect()
