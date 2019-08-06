fo = open("test.txt","w+")
fo.write("Test file\n")
fo.close()

fo = open("test.txt","a+")
anim_list = ["cat","tiger","bear","elephant","mouse","dear"]

for animal in anim_list:
    print(animal)
    fo.write(animal+"\n")

fo.close()
print()

fo = open("test.txt","r")
str = fo.read()
fo.close()
print()
print(str)
