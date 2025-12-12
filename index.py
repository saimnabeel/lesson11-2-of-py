file=open("blah.txt", "r")
file1=open("updateblah.txt", "w")
for line in file:
    if not line.startswith("Coding"):
        file1.write(line)
        print(line)
        file1.write("\n line")
file.close()
file1.close()
        
