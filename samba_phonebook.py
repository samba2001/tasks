phonebook=[]
class Contact:
    def __init__(self,c_name,c_number,c_email=""):
        self.c_number=c_number
        self.c_name=c_name
        self.c_email=c_email
    def __str__(self):
        return self.c_name+" : "+self.c_number
    def __lt__(self,other):
        return self.c_name<other.c_name
    def __gt__(self,other):
        return self.c_name<other.c_name


istrue=True
while(istrue):
    print("enter 1 to add contact \n enter 2 to view contact details \n enter 3 to view all contacts \n enter 4 to delete contact")
    print("enter five to exit")
    x=input()
    if (x==1 or x=='1' or  x=="one"):
        print("enter the name, phone number and gmail of the user")
        name=input()
        number=input()
        email=input()
        c1=Contact(name,number,email)
        phonebook.append(c1)
        print("contact has been saved into phone book")
    if(x==2 or x== '2'):
        name=input("enter the name to view contact detais")
        for ele in phonebook:
            if(ele.c_name==name):
                print(ele)
    if(x==3 or x=='3'):
        for ele in sorted(phonebook):
            print(ele)
    if(x==4 or x=='4'):
        name=input(("enter the name to delete contact "))
        for ele in phonebook:
            if(ele.c_name==name):
                phonebook.remove(ele)
                print(ele)
                print("is deleted")
    if x=='5' or x==5 or x=='five':
        istrue=False
