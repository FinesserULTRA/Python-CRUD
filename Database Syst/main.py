from datasys import CrudDB
from datasys import CrudCall

if __name__ == '__main__':
    # initialize CrudCall for using crud_call
    a = CrudCall("employee")
    cond = "Dept_ID"


    while True:
        choice = int(input("Enter choice, 0 to exit: \n"))

        match choice:
            case 1:
                # table = input("Which table: ")
                a.insert("Adil", 20, 1232312, 14)
            case 2:
                # table = input("Which table: ")
                a.update_rec("Dept_ID=5", Name="'Dani'", Dept_ID=17, Contact=123123)
            case 3:
                # table = input("Which table: ")
                a.delete("Dept_ID=0")
            case 4:
                a.view("2", "*")

            case 0:
                print("GoodBye")
                exit(0)

            case _:
                print("Bad Choice :D")
        # table = input("Which table: ")

        if choice == 0:
            break

    print("\nGoodBye")
