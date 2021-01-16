class contact:
    def __init__(self,name,contact):
        self.name = name
        self.contact=contact
    def display(self):
        print(self.name,"\t\t",self.contact)
        
print("\nAll entered data will be displayed at last")
data=[]
other="yes"
another="yes"
aa="1"
while (aa=="1" or aa=="2"):
    aa=input("\nPress 1 to enter data\nPress 2 to search data\n:")
    
    if aa=="1":
        while (another=="yes"):
            j=0
            nm=1
            c=[]    
            while(nm==1):
                nm=0
                name=input("Enter name of person: ")
                for obj in data:
                    if obj.name==name:
                        print("*name already exist")
                        nm=1
                if nm==0:
                    name1=name


            i=input("How many phone numbers do you want to save into this name ? ")
            while (j<int(i)):
                valid=-1
                number=input("Enter phone number : ")
                if len(number)!=10:
                  print("\n*enter valid number with length 10\n")
                  j-=1
                else:
                    for b in c:
                        if b==number:
                            print("\n*Don't repeat number\n")
                            valid=1
                  
                    for obj in data:
                        for b in range(len(obj.contact)):
                            if obj.contact[b]==number:
                                print("\n*Number already exist\n")
                                valid=1
                    if valid==-1:
                        c.append(number)
                    else:
                        j-=1

                j+=1
            data.append(contact(name1,c))
            print("\nYour data has been saved\n")
            another=input("Do you want to enter another data ? type yes or no :")
        for i in range(len(data)): 
            for j in range(i+1,len(data)):
                if(data[i].name>data[j].name):
                    data[i],data[j]=data[j],data[i]
    if aa=="2":
        while(other=="yes"):
            
                mystr= input("\nEnter name or part of name to search :") 
                if(len(data)==0):
                    print("\nNo data ! Please enter some data first....\n")
                    break
                count=0
                for obj in data:
                    m=obj.name.find(mystr)
                    if(m!=-1):
                        obj.display()
                    else:
                        count+=1
                if count==len(data):
                  print("\nSuch name or part of doesn't exist\n")
            
                other=input("Type yes for more search otherwise type no: ")
        
                
    q=input("\nPress 3 if you want to quit program otherwise Press 4: ")
    if(q=="3"):
        aa="3"
    else:
        aa="1"
        another="yes"
        other="yes"
                
                  
        





print("\nName \t\t Contacts ")
for i in range(len(data)): 
    data[i].display()
    