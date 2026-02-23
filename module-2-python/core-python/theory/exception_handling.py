# try, except 
try:
    getfile = open("my file", "r")
    getfile.write("My file for exception handling")

except IOError:
    print("Unable to open or read data in file")


