#create list of list
list1D = []

for i in range(imax):
    list1D.append(float(i))
    
mylist = []
for j in range(jmax):
    mylist.append(list1D)

for i in range(imax):
    for j in range(imax):
        #print(mylist[i][j])
        mylist[i][j] = 0.0

for i in range(imax):
    for j in range(jmax):
        #print(mylist[i][j])
        mylist[i][j] = m.sin(i*dx*pi)*m.sin(j*dy*pi)

for i in range(imax):
    for j in range(jmax):
        print(mylist[i][j])
