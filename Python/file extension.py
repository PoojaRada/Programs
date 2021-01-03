fname = input("enter the name of file")
a = fname.split('.')
print("The extension is: " + repr(a[-1]))
