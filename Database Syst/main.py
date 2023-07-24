from datasys import CrudDB
from datasys import CrudCall

if __name__ == '__main__':
    a = CrudCall("employee")
    cond = "Dept_ID"
    # a.update_rec(cond, 3, Name="ahmed", Age=18)
    # a.view("2", "*")
    # a.update_rec(cond, 3, Name="ALI", Age=18)
    a.view("2", "*")
    # a.delete("Dept_ID", 6)
    # a.delete("Dept_ID", 6)
    # a.update_rec(cond, 22, Name="'abc 101'")
    # a.update_rec(cond, 3, Name="'abc 101'")
    # a.delete("Dept_ID", 5)
    # a.delete("Emp_ID", 2852)
    # a.delete("Dept_ID", 5)
    # a.delete("Dept_ID", 5)

    # print("VIEW ")
    # a.view("Dept_ID=3", "*")
    # a.view("Dept_ID=3")
    # a.view("Name='Joe'")/

    # a.view("Emp_ID=2847")
    # a.connect()
    # cond = "Dept_ID"

    #
    # while True:
    #     choice = int(input("Enter choice, 0 to exit: \n"))
    #
    #     match choice:
    #         case 1:
    #             # table = input("Which table: ")
    #             a.insert("employee_dept", Dept_Name="'Data Science'")
    #         case 2:
    #             # table = input("Which table: ")
    #             a.update_rec("employee_dept", cond, 9, Dept_Name="'abc 101'")
    #         case 3:
    #             table = input("Which table: ")
    #             a.delete(table, cond, "0")
    #         case 4:
    #             a.view("employee")
    #
    #         case 0:
    #             print("GoodBye")
    #             exit(0)
    #
    #         case _:
    #             print("Bad Choice :D")
    #     # table = input("Which table: ")
    #
    #     if choice == 0:
    #         break

    # print("\nGoodBye")
