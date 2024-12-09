def write(content_to_write):
    f = open("datafile.csv", "a")
    f.write(content_to_write + "\n")
    f.close()

def create():
    f = open("datafile.csv", "w")

    header = ("X", "Y", "Z") # Creates the header (list with 3 columns)
    write(",".join(header))  # Saves the header in the file

    f.close()

def read():
    f = open("datafile.csv", "r")
    for x in f:
        print(x)
    f.close()
