namefile=input("Please enter the file name: ")
filee=open(namefile,'r')
i=1
for line in filee:
    if i % 2 == 0 :
        print(line)
    i += 1

