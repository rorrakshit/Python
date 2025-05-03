try:
    fn = 'task4.1.txt'
    file1 = open(fn,'r')
    reading_line = file1.readlines()
    print("Reading file content:")
    print("Line1:",reading_line[0])
    print("Line2:", reading_line[1])
    file1.close()
except FileNotFoundError:
    print("The file",fn,"not found")