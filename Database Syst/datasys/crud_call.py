from .crud_db import CrudDB


class CrudCall:
    def __init__(self, table):
        self.table = table
        self.__cobj = CrudDB()
        self.__cobj.connection()
        print("Ready To perform Functions")

    def connect(self):
        self.__cobj.connection()

    def insert(self, *args, **kwargs):
        query = "INSERT INTO %s (" % self.table
        keys = kwargs.keys()
        values = tuple(kwargs.values())
        l = len(keys) - 1

        for i, key in enumerate(keys):
            query += key + ""
            if i < l:
                query += ","
        # query = query % args
        query += ")\nVALUE ("
        for i, key in enumerate(keys):
            query += "%s"
            if i < l:
                query += ","
        query += ")"
        query = query % values
        # print(query)
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
        query = "DELETE FROM %s " % self.table
        query += "WHERE %s" % where
        query += " = %s" % args
        # print(query)

        self.__cobj.delete(query)

    def view(self, cond,*args, **kwargs):
        # try:
        #     self.connect()
        # except:
        #     print("error")
        query = f"SELECT {args[0]} FROM `{self.table}` WHERE {cond}"
        # print(query)
        self.__cobj.view(query)
