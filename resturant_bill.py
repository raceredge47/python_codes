#Restuarant Bill
import datetime
import os
try:
    date=str(datetime.datetime.now().date())
    os.mkdir('C:/Users/amans/Desktop/Python/ducat/'+ date)
    os.chdir(os.getcwd()+"/"+date)
except:
    print("Current DateTime Folder Already Exists ")
    
class Bill:
    def __init__(self):
        print("----------Menu----------")
        print("S.No.\tItems      \tPrice")
        print("1.\tBurger        \t40")
        print("2.\tPizza         \t60")
        print("3.\tCoke          \t50")
        print("4.\tPaneer Tikka  \t80")
        print("------------------------")
        self.id=int(input("Enter Customer Id:"))
        self.name=input("Enter Customer Name:")
        self.phone=int(input("Enter Customer Phone Number:"))
        print("Enter Your Order:")
        print("Burger")
        self.burq=int(input("Enter A Quantity"))
        print("Pizza")
        self.pizzq=int(input("Enter A Quantity"))
        print("Coke")
        self.cokeq=int(input("Enter A Quantity"))
        print("Paneer Tikka")
        self.pannq=int(input("Enter A Quantity"))
    def calc(self):
        self.res=40*self.burq+60*self.pizzq+50*self.cokeq+80*self.pannq
        self.gst=(self.res*18)/100
        return self.res    
    def display(self):
        
        f=open(str(self.id)+'.txt','w+')
        f.write("---------------------Bill--------------\n")
        f.write(f"Customer Id             :    {self.id}\n")
        f.write(f"Customer Name           :    {self.name}\n")
        f.write(f"Customer Phone          :    {self.phone}\n")
        f.write(f"---------------------------------------\n")
        f.write(f"Items        \tQuantity     \tPrice \n")
        f.write(f"Burger        \t{self.burq}        \t{(40*self.burq)}\n")
        f.write(f"Pizza         \t{self.pizzq}       \t{(60*self.pizzq)}\n")
        f.write(f"Coke          \t{self.cokeq}       \t{(50*self.cokeq)}\n")
        f.write(f"Paneer Tikka  \t{self.pannq}       \t{(80*self.pannq)}\n")
        f.write("---------------------------------------\n")
        f.write(f"Price Is                :       {obj.calc()}\n")
        f.write(f"GST 18%                 :       {self.gst}\n")
        f.write("---------------------------------------\n")
        f.write(f"Net Payable Amount      :       {(self.gst+self.res)}\n")
        f.write("---------------------------------------\n") 
        f.seek(0)
        print(f.readlines())
        f.close()
obj=Bill()
obj.display()
