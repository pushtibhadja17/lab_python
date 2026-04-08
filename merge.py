d1=open("d1.txt","r")
data1=d1.read()
d1.close()

p1=open("p1.txt","r")
data2=p1.read()
p1.close()


merged=open("p1.txt","w")
merged.write(data1)
merged.write("\n")
merged.write(data2)
merged.close()

print("files merge into successfully")