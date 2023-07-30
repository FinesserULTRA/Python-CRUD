from .crud_db import CrudDB
import csv


class CrudCall:
    def __init__(self, table):
        self.table = table
        self.__cobj = CrudDB()
        self.__cobj.connection()
        print("Ready To perform Functions")

    def __del__(self):
        self.__cobj.close()

    def connect(self):
        self.__cobj.connection()

    def insert(self, *args, **kwargs):
        query = f"INSERT INTO `employee` (`Name`,`Age`,`Contact`,`Dept_ID`) VALUES {tuple(args)}"

        self.__cobj.database_add(query)

    def create_table(self, file_path, file_name):
        if self.__cobj.check_table(file_name):
            pass
        else:
            with open(file_path) as csv_file:
                csvfile = csv.reader(csv_file, delimiter=(','))
                column_name = []
                for i in csvfile:
                    col = (i[0], i[1], i[2], i[3])
                    column_name.append(col)
                    query = f"create table `{file_name}`(`{i[0]}` INT primary key auto_increment, `{i[1]}` varchar(50),`{i[2]}` INT, `{i[3]}` INT)"
                    break
                # print(query)
                self.__cobj.create_table(query)

    def update_rec(self, where=None, *args, **kwargs):
        # NEED TO UPDATE THIS QUERY, to one line, work in progress
        query = f"UPDATE {self.table} SET "
        for i, key in enumerate(kwargs.keys()):
            query += "`" + key + "`=%s"
            if i < len(kwargs.keys()) - 1:
                query += ","
        query = query % tuple(kwargs.values())
        query += f" WHERE {where}"
        self.__cobj.update_rec(query)

    def delete(self, where=None):
        # query = "DELETE FROM %s " % self.table
        # query += "WHERE %s" % where
        # query += " = %s" % args
        q1 = f"DELETE FROM {self.table} WHERE {where}"
        # print(q1)
        self.__cobj.delete(q1)

    def view(self, cond, *args, **kwargs):
        # try:
        #     self.connect()
        # except:
        #     print("error")
        query = f"SELECT {args[0]} FROM `{self.table}` WHERE {cond}"
        # print(query)
        self.__cobj.view(query)

    # def viewone(self,cond,*args):
    #
    #     query = f"SELECT {args[0]} FROM `{self.table}` WHERE {cond}"

    def check(self, tablename):
        table = tablename

        self.__cobj.check_table(table)
