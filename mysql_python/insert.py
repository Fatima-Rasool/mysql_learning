from test import DBConnection, DBInteraction

def main():
    # Create a DBConnection instance
    db_connection = DBConnection(host='localhost', username='root', password='root', database='python')

    try:
        # Connect to the database
        db_connection.connect()

        # Create a DBInteraction instance
        db_interaction = DBInteraction(db_connection)

        # Data to insert
        data_to_insert = {'name': 'BBB', 'age': 20, 'email': 'bbb@example.com'}

        # Add data to the 'users' table
        db_interaction.create_record('users', data_to_insert)

    except Exception as e:
        print("Failed to add data to the database:", e)
    finally:
        # Disconnect from the database
        db_connection.disconnect()

if __name__ == "__main__":
    main()
