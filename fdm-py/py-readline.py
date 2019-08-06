file1 = open("peak.csv","r")
file2 = open("testwrite.csv","w+")
file2.write("x, fx\n")

for line in file1:
    #print(line)
    fields = line.split(",")
    field1 = fields[0]
    field2 = fields[1]
    print(field1, field2)
    str = field1+"\t "+field2
    file2.write(str)

file1.close()
file2.close()

