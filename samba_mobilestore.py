class Phone:
    def __init__(self, name, company, price, noof_units):
        self.name = name
        self.company = company
        self.price = price
        self.noof_units = noof_units
    def __str__(self):
        return "model = "+self.company+" "+self.name+" price "+str(self.price)+" number of units = "+str(self.noof_units)

    def add(self,num):
        self.noof_units +=num


p1=Phone('s10','samsung',20000,5)
p2=Phone('7','apple',30000,10)
p3=Phone('m30','samsung',20000,5)
database=[p1,p2,p3]

istrue=True
while(istrue):
    print("enter 1 to add phone to database \n enter 2 to view for a mobile")
    print("enter 3 to view entire database \n enter 4 to exit the program")
    x=input()
    if(x=='1'):
        print("enter name, company,price amd noofunits")
        name=input()
        company=input()
        price=int(input())
        noofunits=int(input())
        isindatabase = True
        for ele in database:
            if(ele.name==name and ele.company==company):
                ele.add(noofunits)
                print(str(noofunits)+ " units of "+name +" "+company  +" added to database")
                isindatabase = False
                break
        if (isindatabase) :
            phone=Phone(name,company,price,noofunits)
            database.append(phone)
            print("new mobile is added to database")
    if (x=='2'):
        print("enter the name and model of mobile to view ")
        name=input()
        model=input()

        for ele in database:
            if(ele.name==name and ele.company==model):
                print(ele)
                isindatabase=True
                break
    if(x=='3'




    ):
        for ele in database:
            print(ele)

    if (x=='4'):
        istrue=False





