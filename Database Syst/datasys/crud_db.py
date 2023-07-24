import mysql.connector
from mysql.connector import errorcode


class CrudDB:

    def __init__(self, host='localhost', user='root', password='', database='crud_db'):
        self.__host = host
        self.__user = user
        self.__password = password
        self.__database = database
        self.__instance = None
        self.__connection = None
        self.__session = None

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
        # self.connection()
        if self.__connection.is_connected():
            self.__session.execute(query)
            self.__connection.commit()
        self.__close()
        print("record inserted.")

    def update_rec(self, query):
        if self.__connection.is_connected():
            self.__session.execute(query)
            self.__connection.commit()

        # Obtain rows affected
        update_rows = self.__session.rowcount
        self.__close()
        print("Record Updated")

        return update_rows

    def delete(self, query):
        if self.__connection.is_connected():
            self.__session.execute(query)
            self.__connection.commit()

        # Obtain rows affected
        self.__close()
        print("Deleted Record")

    def view(self, query):
        # self.connection()

        # if self.__connection.is_connected():
        if self.__connection.is_connected():
            self.__session.execute(query)
            # self.__connection.commit()
            # self.__connection.commit()
            data = self.__session.fetchall()

            print("All Records are shown: ")
            for i in data:
                print(f"Emp_ID: {i[0]}, Name: {i[1]}, Age: {i[2]}, Contact:{i[3]}, Dept_ID: {i[4]}")

            self.__connection.commit()
            self.__close()

    # def view_one(self,query):
    #     self.__session.execute(query)
    #
    #     data = self.__session.fetchall()
    #     for i in data:
    #         if i == 0:
    #             print(f"Record of {i[0]} is shown: ")
    #         print(f"Emp_ID: {i[0]}, Name: {i[1]}, Age: {i[2]}, Contact:{i[3]}, Dept_ID: {i[4]}")

    # self.__connection.commit()
    # self.__close()
