import mysql.connector
from mysql.connector import errorcode


class CrudDB:
    __instance = None
    __host = None
    __user = None
    __password = None
    __database = None
    __session = None
    __connection = None

    def __init__(self, host='localhost', user='root', password='', database='crud_db'):
        self.__host = host
        self.__user = user
        self.__password = password
        self.__database = database

    def connection(self):

        try:
            cnx = mysql.connector.connect(host='127.0.0.1', user='root', database='crud_db')
            self.__connection = cnx
            self.__session = cnx.cursor()

        except mysql.connector.Error as err:
            print("Database Connection Successful")
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)
        else:
            print("Database Connection Successful")

    def __close(self):
        self.__session.close()
        self.__connection.close()

    def Database_add(self, query):

        self.connection()
        self.__session.execute(query)
        self.__connection.commit()
        self.__close()
        print("record inserted.")

    def update_rec(self, query):
        self.connection()
        self.__session.execute(query)
        self.__connection.commit()

        # Obtain rows affected
        update_rows = self.__session.rowcount
        self.__close()
        print("Record Updated")

        return update_rows

    def delete(self, query):
        self.connection()
        self.__session.execute(query)
        self.__connection.commit()

        # Obtain rows affected
        update_rows = self.__session.rowcount
        self.__close()
        print("Deleted Record")
        return update_rows

    def view(self, query):
        self.connection()
        self.__session.execute(query)

        print("All Records are shown: ")
        data = self.__session.fetchall()
        for i in data:
            print(i)

        self.__connection.commit()
