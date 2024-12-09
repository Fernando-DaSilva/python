def show_menu():
    print('=========================')
    print('=== 1) CREATE FILE ======')
    print('=== 2) INSERT XYZ  ======')
    print('=== 3) READ        ======')
    print('=== 4) SHOW MENU   ======')
    print('=== 5) PULL ROW    ======')
    print('=== 9) EXIT        ======')
    option = input('Enter your option:')
    try:
        int_option = int(option)

    except:
        int_option = 0

    return int_option

def show_hello(name):
    print(f"Hello! Welcome to my system, {name}.")
