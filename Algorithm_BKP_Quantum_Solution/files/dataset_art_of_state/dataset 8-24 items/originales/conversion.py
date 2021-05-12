import os

def createFileWithFormat(name, n, w, p, o):
    file = open(name+'.txt', 'w')
    file.write(n.strip() + '\n')
    print(name.strip() + '\n')
    for index, wa in enumerate(w):        
        file.write(wa + " " +  p[index] + '\n')
    file.write(o.strip())
    file.close()

nameFilesFolder = os.listdir("./")
#nameFilesFolder = ['ks_8a.dat']

nameFiles = [file for file in nameFilesFolder if ".dat" in file]
for name in nameFiles:
    with open(name) as file:
        print(file.name)
        n = file.readline()
        n.strip('\n')
        #line of weigth
        line = file.readline()
        line.rstrip('\n')
        w = line.split()
        line = file.readline()
        p = line.split()
        line.rstrip('\n')
        o = file.readline()
        o.rstrip('\n')
        createFileWithFormat(file.name.split(".")[0], n, w, p, o)





