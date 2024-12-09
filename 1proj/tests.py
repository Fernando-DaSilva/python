# BACKUP:


def how_many_rows():
    try:
        x_rows = int(input("How many rows do you want to save? "))
        if x_rows < 1:
            raise ValueError("The number of rows must be at least 1.")
    except ValueError as e:
        print(f"Invalid input: {e}")
        return

    print("\nEnter the data for each row. Type 'EXIT' to stop the loop.")

    i = 1
    while i <= x_rows:
        try:
            row = []
            print(f"\nRow {i}:")
            for col in header:
                value = input(f"  {col}: ")
                if value.upper() == "EXIT":
                    print("Process interrupted.")
                    exit()
                row.append(value)  # Adds the info to the file [H]
            write(",".join(row))  # Saves the info in the file
            i += 1  # Increase the row
            print(f"\nData successfully saved to datafile.csv.")

        except KeyboardInterrupt:
            print("\nProcess interrupted.")
            exit()

    # Maybe: for y in range(:, x_rows)???


def retrieve_rows():
    try:
        asked_row = int(input("What row do you want to retrieve? "))  # Requests  the desired row
        if asked_row < 1:
            raise ValueError("The row number must be greater than 0.")

        with open("datafile.csv", "r") as file:  # Reads from the file
            rows = file.readlines()  # Reads all the rows
            if asked_row >= len(rows):
                print(f"Row {asked_row} does not exist. The file has only {len(rows) - 1} rows (excluding header).")
            else:
                print(f"Row #{asked_row}: {rows[asked_row]}")  # Shows the row [H]
    except ValueError as e:
        print(f"Invalid input: {e}")
    except FileNotFoundError:
        print("The file does not exist.")


def show_my_menu():
    my_option = show_menu()
    if int(my_option) == 9:
        print('EXIT')
        exit()
