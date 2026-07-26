#file handling

# f=open("my_file.py","w")
# f.write("print('Hello World')")
# f.close()

# import os
# name=input("Enter name : ")
# print("1.Create\n2.Read\n3.Delete\n4.Prescribtion")
# choice=int(input("Enter your choices:"))
# def add():
#     f=open(name+".txt","w")
#     f.write(input("Enter age : \n"))
#     f.write(input("Enter place : \n"))
#     f.write(input("Enter ph no : \n")) 
# def view():
#     f=open(name+".txt","r")
#     print(f.read())
#     f.close()
# def delete():
#     os.remove(name+".txt")
#     print("File deleted")
# def prescribe():
#     f=open(name+".txt","a")
#     f.write(input("Enter your stymptoms : \n"))
#     f.write("\ncancer\n")
#     f.write("letrozole\ncapecitabine\n")
# if choice==1:
#     add()
# elif choice==2:
#     view()
# elif choice==3:
#     delete()
# elif choice==4:
#     prescribe()

# list1=["happy","sad","good"]
# list2=["sad","happy","good"]
# list3=[]
# def least(list1,list2):
#     min=(len(list1)-1)+(len(list2)-1)
#     list3=[]
#     for i in range(len(list1)):
#         for j in range (len(list2)):
#             if list1[i]==list2[j]:
#                 if (i+j)<min:
#                     min=i+j
#                     list3=[list1[i]]
#                 elif i+j==min:
#                     list3.append(list1[i])                                       
#     return list3
# print(least(list1,list2))

# f=open("number.txt", "w")
# for i in range(5):
#     num=input("Enter a number: ")
#     f.write(num +"\n")
# f.close()
# f=open("number.txt","r")
# sum=0
# for i in range(5):
#     line=f.readline()
#     n=int(line)
#     if i==0:
#         largest=n
#         smallest=n
#     else:
#         if n>largest:
#             largest=n
#         if n<smallest:
#             smallest=n
#     sum=sum+n
# average=sum/5
# f.close()
# print("Largest =",largest)
# print("Smallest =",smallest)
# print("Sum =",sum)
# print("Average =",average)       

# s="leetcode"
# count=""
# for i in s:
#     if i in count:
#         count[i]+=1  
#     else:
#         count[i]=1

# class Student():
#     def __init__(self):
#         self.name="gopika"
# s1=Student()
# print(s1.name)

# class Student():
#     def __init__(self,name):
#         self.name=name
#     def attendence(self):
#         return "present"
# s1=Student("gopika")
# print(s1.name)
# print(s1.attendence())

# class Product():
#     def __init__(self,id,name,price,qty):
#         self.pdtid=id
#         self.pdtname=name
#         self.pdtprice=price
#         self.pdtqty=qty
#     def addstock(self,amt):
#         self.pdtqty+=amt
#         print(amt,"stock added")
#     def removestock(self,amt):
#         if self.pdtqty>=amt:
#             self.pdtqty-=amt
#             print(amt,"removed")
#         else:
#             print("insufficient stock")
#     def checkstock(self,amt):
#         if self.pdtqty>=amt:
#             print("stock available")
#         else:
#             print("insufficient stock")
# p1=Product(101,"Lipstick",250,20)
# p2=Product(102,"fan",200,10)
# print("Product 1 : ",p1.pdtid,p1.pdtname,p1.pdtprice,p1.pdtqty)
# print("Product 2 : ",p2.pdtid,p2.pdtname,p2.pdtprice,p2.pdtqty)
# p1.addstock(20)
# p1.removestock(5)
# p1.checkstock(5)
# p2.addstock(20)
# p2.removestock(5)
# p2.checkstock(5)

# class Library():
#     def __init__(self,id,name,author,price,status):
#         self.bid=id
#         self.bname=name
#         self.bauthor=author
#         self.bprice=price
#         self.bstatus=status
#     def details(self):
#         print("Price:",self.bprice)
#         print("Availability:",self.bstatus)
#     def available(self):
#         if self.bstatus:
#             self.bstatus=False
#             print(f"{self.bname} has been taken")
#         else:
#             print(f"{self.bname} is unavailable")
#     def returnb(self):  
#         self.bstatus=True
#         print(f"{self.bname} has been returned")
# b1=Library(1,"Alchemist","Paulo Coelo",450,"yes")
# b2=Library(2,"2 States","Chetan Bhagat",500,"no")
# b1.details()
# b1.available()
# b1.returnb()


