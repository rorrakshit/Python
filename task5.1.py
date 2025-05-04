dic = {'a':80,'b':90,'c':56}
inp = input("Enter the name: ")
if inp in dic:
    print("{}`s marks: {}".format(inp,dic[inp]))
else:
    print("Student not found.")