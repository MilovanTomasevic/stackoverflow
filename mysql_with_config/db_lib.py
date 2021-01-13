from mysql.connector import (
    MySQLConnection as db,
    errorcode,
    Error
)


class MySQLDataBase:
    def connection(self, db_config):
        try:
            print('Connecting to MySQL database...')
            conn = db(**db_config)
            print("Connection established.")
            return conn
        except Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password!")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist!")
            else:
                print(err)
        else:
            conn.close()
            print("Conncetion is closed.")
