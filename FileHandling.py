"""
Docstring for FileHandling

FileHandling in Python :
File handling is an important part of programming as it allows us to read from and write to files.

Syntax : 
file=open("filename.txt","Mode")
file=open("sample.tx","r")
open() : Basically Opens the file

Modes of File Handling :
- 'r' : Read mode - Opens a file for reading (default mode). The file
- 'w' : Write - opened file can be overwrite
- 'a' : append -appends the text or element inside the file
- 'r+' : read-write
- 'rb' : Read binary it is used to read binary files (images/pdf).


Methods : 
open() : Loads the file in an Variable.
read() : reads the content present in the file.
readline() : read a single line.
readlines() : reads all lines and returns a list value. 
"""

# Reading a File :
f=open("sample.txt",'r')
data=f.read()
print(data)
f.close() 

# Using Readlines : 
f=open("sample.txt",'r')
data=f.readlines()
print(data)
f.close() 

# Writing a File 
f=open("sample.txt",'w')
f.write("This is a sample text file.\nThis file is used to demonstrate file handling in Python.")
f.close()

# Append a file 
f=open("sample.txt","a")
f.write("\nThis line is appended to the file.")
f.writelines(["\nAppending multiple lines.\nLine 2 of appended text."])
f.close()

# Using 'with' statement to handle files
"""
We do not need to explicitly close the file when using 'with' statement.
"""
with open("sample.txt",'r') as f:
    data=f.read()
    print(data)
    # cursor()
    f.seek(5)  # Move the cursor to the beginning of the file
    first_line=f.readline()
    print("First Line:", first_line)
    # tell()

# Reading a binary file
f=open("sampleimg.jpg",'rb')
data=f.read()
print(data)
f.close()