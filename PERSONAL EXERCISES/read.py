import os
f=open("demo1.txt","r")
print(f.read())
print(f.readline())

f=open("demo1.txt","a")
f.write("we will push to the last dot")

#f=open("demo1.txt","w")
#f.write("we will push to the last dot")
f.close()

#os.remove("demo1.txt")
f = open("Alemi.txt", "x")
f = open("Alemi.txt", "a")
f.write("ALEMI BLESS ")
