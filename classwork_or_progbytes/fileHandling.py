#READ FROM FILE

# myfile = openRead("sample.txt")
myfile = open("quotes.txt", "r")
# x = myFile.readLine()
x = myfile.readline()
print(x)
myfile.close()
