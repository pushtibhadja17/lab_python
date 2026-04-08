#read 
src=open("d1.txt","r")
data=src.read()
src.close()

#write
dst=open("p1.txt","w")
dst.write(data)
dst.close()
print("File copied successfully")