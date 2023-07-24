from .crud_db import CrudDB


class CrudCall:
    __cobj = CrudDB()

    def connect(self):
        self.__cobj.connection()

    def insert(self, table, *args, **kwargs):
        query = "INSERT INTO %s (" % table
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

    def update_rec(self, table, where=None, *args, **kwargs):
        query = "UPDATE %s SET " % table
        keys = kwargs.keys()
        value = tuple(kwargs.values())
        # where = where%args
        # query += kwargs[]
        l = len(keys) - 1
        for i, key in enumerate(keys):
            query += key + " = %s"
            if i < l:
                query += ","
        query = query
        query += " WHERE %s" % where
        if args:
            query += "=%s" % args
        query = query % value
        # print(query)
        self.__cobj.update_rec(query)

    def delete(self, table, where=None, *args):
        query = "DELETE FROM %s " % table
        query += "WHERE %s" % where
        query += " = %s" % args
        # print(query)

        self.__cobj.delete(query)

    def view(self, table, *args, **kwargs):
        query = "SELECT * FROM `%s`" % table

        # print(query)
        self.__cobj.view(query)
