import mysql.connector
from mysql.connector import Error, errorcode

db_config = {
    "user": "root",
    "password": "pwd",
    "host": "localhost",
    "port": "8083",
    "database": "users",
}

# Create a connection to the MySQL database
sql_connection = mysql.connector.connect(**db_config)

# Create a cursor to interact with the database
cursor = sql_connection.cursor()


def insert_users(user_info):
    try:
        # insert statement
        insert_statement = "INSERT INTO user_info (first_name, last_name, dob, gender, name_character_count) VALUES (%s, %s, %s, %s, %s)"

        # insert each user into db

        data = (
            user_info["first_name"],
            user_info["last_name"],
            user_info["dob"],
            user_info["gender"],
            user_info["name_char_count"],
        )
        cursor.execute(insert_statement, data)

        sql_connection.commit()
    except mysql.connector.Error as err:
        # if user already exists in database, ignore and continue
        if err.errno == errorcode.ER_DUP_ENTRY:
            print(
                f"User {user_info['first_name']} {user_info['last_name']} already exists in database. Skipping..."
            )
        else:
            print(f"Error inserting user: {user_info}")
