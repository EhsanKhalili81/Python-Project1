N=int(input("Enter Your Number Of Person :"))
Name=[]
LName=[]
Tel=[]
contact={}
for i in range(0,N):
    Name.append(input("Enter Your Name:"))
    LName.append(input("Enter Your LastName:")) 
    Tel.append(int(input("Enter Your Tel:")))
    contact.update({"Name":Name,"LastName":LName,"Tel":Tel})  

for j in range(0,len(contact)):
    print(contact["Name"][j],contact["LastName"][j],contact["Tel"][j])   

 