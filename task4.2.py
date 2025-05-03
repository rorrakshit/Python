
def fwrite(a,fn):
    file1 = open(fn,'w')
    file1.write(a)
    file1.close()
def fappend(b,fn):
    file1 = open(fn,'a')
    file1.write('\n'+b)
    file1.close()
def fread(fn):
    file1 = open(fn,'r')
    lines = file1.readlines()
    print(lines[0])
    print(lines[1])
fn = 'task4.2.txt'
a = input("Enter text to write to the file:\t")
print("Data successfully written to",fn)
fwrite(a,fn)
b=  input("Enter additional text to append: ")
print("Data successfully appended.")
fappend(b,fn)
print(f"Final content of {fn}:")
fread(fn)

