from .crud_db import CrudDB


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

        self.__cobj.Database_add(query)

    def update_rec(self, where=None, *args, **kwargs):
        query = "UPDATE %s SET " % self.table
        keys = kwargs.keys()
        value = tuple(kwargs.values())
        # where = where%args
        # query += kwargs[]
        l = len(keys) - 1
        for i, key in enumerate(keys):
            query += key + " = '%s'"
            if i < l:
                query += ","
        query = query
        query += " WHERE %s " % where
        if args:
            query += "= %s"%args
        query = query % value
        print(query)
        # self.__cobj.update_rec(query)

    def delete(self, where=None, *args):
        # query = "DELETE FROM %s " % self.table
        # query += "WHERE %s" % where
        # query += " = %s" % args
        q1 = f"DELETE FROM {self.table} WHERE {where}"
        print(q1)
        # self.__cobj.delete(query)

    def view(self, cond,*args, **kwargs):
        # try:
        #     self.connect()
        # except:
        #     print("error")
        query = f"SELECT {args[0]} FROM `{self.table}` WHERE {cond}"
        # print(query)
        self.__cobj.view(query)
