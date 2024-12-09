from menu import show_menu, show_hello
from filecontrol import create, write, read
from rows_control import how_many_rows, retrieve_rows

def write_to_file(content_to_write):
    write(content_to_write)

def read_from_file():
    read()

def show_my_menu():
    my_option = show_menu()
    if int(my_option) == 9:
        print('EXIT')
        exit()

    show_hello(f"Your option: {my_option}")

    if my_option == 1:
        create()
    if my_option == 2:
        how_many_rows()
    if my_option == 3:
        read_from_file()
    if my_option == 4:
        show_my_menu()
    if my_option == 5:
        retrieve_rows()

def main():
    while 1 == 1:
        show_my_menu()

main()
