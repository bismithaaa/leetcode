# n=int(input("Enter your limit:"))
# sum=0
# for i in range(1,n+1):
#     sum=sum+i
# print(sum)


# num=int(input("Enter the number:"))
# for i in range(1,11):
#     print(num,"*",i,"=",num*i)

# for i in range(1,51):
#     if i%2==0:
#         print(i)

# num=int(input("Enter your digit :"))
# sum=0
# while num!=0:
#     r=num%10
#     num=num//10
#     sum=sum+r
# print(sum)

# total=0
# while True:
#   num=int(input("Enter your number:"))
#   total=total+num
#   if num==0:
#     break
# print("sum of numbers is:",total)

# num=int(input("Enter a no :"))
# if num == 1:
#     print("Neither prime nor composite")
# else:
#     for i in range(2,num):
#         if num%i==0:
#             print("Not Prime")
#             break
#     else:
#         print("Prime")

# num=int(input("Enter the no:"))
# sum=0
# for i in range(1,num):
#     if num%i==0:
#         sum=sum+i
# if num==sum:
#     print("Perfect no")
# else:
#     print("Not Perfect")

# rows=0
# while rows<=7:
#     if(rows%2==0):
#         print("*" * rows)
#     else:
#         print(rows*2*"*")
#     rows+=1    


# rows = 1
# while rows <= 10:
#     count = 0
#     i = 1
#     while i <= rows:
#         if rows % i == 0:
#            count += 1
#         i += 1
#     if count == 2:
#         print("*" * (rows + 1))
#     else:
#         print("*" * rows)
#     rows += 1

# num=int(input("Enter a no :"))
# temp=num
# sum=0
# while num>0:
#     rem=num%10
#     sum=sum+rem**3
#     num=num//10
# if sum==temp:
#     print("Armstrong")
# else:
#     print("Not Armstrong")

# num=int(input("Enter the no:"))
# temp=num
# sum=0
# while num>0:
#     fact=1
#     rem=num%10  
#     for i in range(1,rem+1):
#         fact=fact*i
#     num=num//10
#     sum=sum+fact
# if sum==temp:
#     print("Strong")
# else:
#     print("Not")

# name="bismi"
# print(name[1:5])

# name="bismi"
# city="alapy"
# print("My name is {} and my city is {}".format(name,city))

# name="bismi"
# city="alapy"
# print(f"My name is {name} and my city is {city}")

# num1,num2=map(int,input("ENter 2 no :").split())
# print(num1+num2)

# num1,num2=input("ENter 2 name :").split()
# print("my name is",num1)
# print("my name is",num2)

# my_list=[1,2,3,4,5]
# print(my_list)

# my_list=[1,2,3,4,5]
# print(my_list[1:5])

#my_list=["apple","orange","kiwi","mango"]
# my_list.append("apple")
# my_list.insert(1,"apple")
# my_list.remove("apple")
# my_list.pop(2)
# my_list.reverse()
# for i in range(len(my_list)):
#     if my_list[i]=="apple":
#         print(i)

# list1=["apple","orange","kiwi","banana",2]
# list2=["red","blue","green","orange",3]
# result=[]
# for i in list1:
#     for j in list2:
#         if i==j:
#             result.append(i)
# print(result)
            
# list=["apple","orange","apple","mango"]
# my_list = []
# for i in list:
#     if i not in my_list:
#         my_list.append(i)
# print(my_list)

# list1=["apple","orange","kiwi","banana"]
# result = []
# # print(list1[::-1])
# for i in range(len(list1)-1,-1,-1):
#     result.append(list1[i])
# print(result)

# list=[1,3,7,4,8,2,9]
# even=[]
# odd=[]
# for i in list:
#     if i%2==0:
#         even.append(i)
#     else:
#         odd.append(i)
# print("Count of even:",len(even))
# print("Count of odd:",len(odd))

# list=[25,10,38,26,30]
# largest=list[0]
# for i in list:
#       if i>largest:
#         largest=i
# print("largest no is :",largest)

#list=[25,10,38,26,30]
# lowest=list[0]
# for i in list:
#       if i<lowest:
#         lowest=i
# print("lowest no is :",lowest)

# list=[10,15,20,25]
# sum=0
# for i in list:
#     sum=sum+i
# print("sum :",sum)

# num=[1,-3,7,-4,8,-2,9]
# pos=[]
# neg=[]
# for i in num:
#     if i>0:
#         pos.append(i)
#     else:
#         neg.append(i)
# print("Count of pos:",len(pos))
# print("Count of neg:",len(neg))

# list=[10,10,15,20,25]
# sum=0
# for i in list:
#     sum=sum+i
# avg=sum/len(list)
# print("avg :",avg)

# num=[1,2,1,3,4,1]
# result=[]
# element=1
# for i in num:
#     if i==element:
#         result.append(i)
# print(len(result))

# list=[10,10,15,20,25,26]
# sum=0
# result=[]
# for i in list:
#     sum=sum+i
# avg=sum/len(list)
# for i in list:
#     if i>avg:
#         result.append(i)
# print(result)

# num = [0, 5, 15, 0, 33, 0, 2, 0, 1]
# count = num.count(0)
# while 0 in num:
#     num.remove(0)
# for i in range(count):
#     num.append(0)
# print(num)

# s=input("enter a string:")
# if len(s)<2:
#     print("Empty string")
# else:
#     result=s[:2]+s[-2:]
# print("result")

# s=input("Enter a string: ")
# first_char=s[0]
# result=first_char+s[1:].replace(first_char,'$')
# print(result)

# s="restart"
# ret=""
# for i in range(0,len(s)):
#     if i==0:
#         ret+=s[i]
#         continue
#     elif s[i]!=s[0]:
#         ret+=s[i]
#     else:
#         ret+="$"
# print(ret)

# string="restart"
# first=string[0]
# result=string[0]
# for i in string[1:]:
#     if first==i:
#         result+="$"
#     else:
#         result=result+i
# print(result)

# s1=input("Enter first string: ")
# s2=input("Enter second string: ")
# new_s1=s2[:2] + s1[2:]
# new_s2=s1[:2] + s2[2:]
# result=new_s1 + " " + new_s2
# print("Result:", result)

# s="string"
# if len(s)<3:
#     print(s)
# elif s[-3:]!="ing":
#     print(s+"ing")
# else:
#     print(s+"ly")

# s=input("enter a list of words : ")
# max=len(s[0])
# temp=""
# for i in s.split():
#     if max<len(i):
#         max=len(i)
#         temp=i
# print(temp)

# s=input("Enter a string:")
# result=""
# for i in range(len(s)):
#     if i%2==0:
#         result+=s[i].upper()
#     else:
#         result+=s[i].lower()
# print(result)

# s=input("Enter a sentence: ")
# dup=[]
# for i in s.split(","):
#     if i not in dup:
#         dup.append(i)
# dup.sort()
# print(dup)

# s=input("enter a string: ")
# for i in s.split():
#     if i.isdigit():
#         print(i)

# s=input("Enter a string: ")
# result=""
# for i in s.split():
#     if len(i)<5:
#         result=result+i+" "
#     else:
#         result=result+"#"*len(i)+" "
# print(result)  

# s=input("enter str : ")
# res=""
# for i in s.split():
#     for j in range(len(i)):
#         if j == 0:
#             res+=i[j].upper()
#         else:
#             res+=i[j].lower()
#     res=res+" "
# print(res)    

# s=input("enter str : ")
# res=""
# for i in range(0,len(s)):
#     if s[i].isupper():
#         res=res+" "+s[i]
#     else:
#         res=res+s[i]
# print(res)

# samp=['Red','Green','White','Black','Pink','Yellow']
# res=[]
# for i in range(0,len(samp)):
#     if i==0 or i==4 or i==5:
#         continue
#     res.append(samp[i])
# print(res)

# my_tuple=("apple","kiwi","watermelon")
# result=list(my_tuple)
# print(result)

# list1=[1,5,3]
# temp=True
# for i in list1:
#     if i<=1:
#         temp=False
#         break
#     for j in range(2,i):
#         if i%j==0:
#             temp=False
#     if temp == False:
#         break
# print(temp)

# list1=['python','list','exercises','practice','solution']
# leng=int(input("enter a no : "))
# list2=[]
# for i in list1:
#     if len(i)==leng:
#         list2.append(i)
# print(list2)

# list1=[1,1,3,4,4,5,6,7]
# list2=[0,1,2,3,4,4,5,7,8]
# list3=list1+list2
# sum=0
# for i in list3:
#     sum=sum+i
# avg=sum/len(list3)
# print(avg)

# list1=[6,3,9,5]
# res=sorted(list1)
# if res==list1:
#     print("True")
# else:
#     print("False")

# my_tuple=(10,20,30,40,20,50,60,40)
# tup=list(my_tuple)
# print(tup)
# dup=[]
# pdt=1
# for i in my_tuple:
#     if i not in tup:
#         dup.append(i)
# for i in tup:
#     pdt=pdt*i
# print(pdt)

# tuple1 = ('e', 'x', 'e', 'r', 'c', 'i', 's', 'e', 's')
# result = ""
# for i in tuple1:
#     result += i
# print(result)

# lst = [10, 20, 4, 5, 'b', 70, 'a']
# total = 0
# for i in lst:
#     if isinstance(i, int):
#         for digit in str(i):
#             total += int(digit)
# print(total)

# my_set={"apple","orange","banana","apple"}
# my_set.add("kiwi")
# my_set.update({"watermelon","grapes"})
# my_set.discard("apple")
# my_set.remove("appley")
# print(my_set)

# set2={"apple","orange","kiwi"}
# print(my_set | set2)
# print(my_set & set2)

# my_set=frozenset({"apple","kiwi","orange"})
# my_set.add("banana")
# print(my_set)

##DICTIONARY##

# my_dict={
#     "name":"Gopika",
#     "city":"ekm",
#     "course":"python"
# }
# print(my_dict["name"])
# print(my_dict.keys())
# print(my_dict.values())
# print(my_dict.items())

# my_dict={
#     "person1":{
#         "name":"Gopika",
#         "city":"ekm",
#         "course":"python"
#     },
#     "person2":{
#         "name":"bis",
#         "city":"alapy",
#         "course":"py"
#     }
# }
# print(my_dict["person1"]["name"])

# my_list=["apple","banana","apple"]
# res=list(set(my_list))
# print(res)

# str1=input("Enter a string : ")
# dic={"vow":0,"cons":0}
# vowels="aeiou"
# for i in str1:
#     if i in vowels:
#         dic["vow"]+=1
#     else:
#         dic["cons"]+=1
# print(dic)

# dic1={"a":10,"b":20,"c":30}
# dic2={"b":40,"c":40,"d":50}
# common=[]
# # a=(dic1.keys())
# # b=(dic2.keys())
# for key in dic1:
#     if key in dic2:
#         common.append(key)
# print(common)

# sen=input("enter a string : ")
# freq={}
# for i in sen:
#     if i in freq:
#         freq[i]+=1
#     else:
#         freq[i]=1
# # print(freq)
# max=0
# max_freq=""
# for i in freq:
#     if freq[i]>max:
#         max=freq[i]
#         max_freq=i
# print(max_freq,":",max)

# n=int(input("Enter terms : "))
# dic={}
# for i in range(1,n+1):
#     dic[i]=i*2
# print(dic)

# words=['apple','ant','bat','ball','cat']
# dict={}
# for i in words:
#     first=i[0]
#     if first in dict:
#         dict[first].append(i)
#     else:
#         dict[first]=[i]
# print(dict)

# dic1={"a":100, "b":200, "c":300}
# dic2={"b":200, "c":200, "d":500}
# for key in dic2:
#     if key in dic1:
#         dic1[key]+=dic2[key]
#     else:
#         dic1[key]=dic2[key]
# print(dic1)


# for i in range(1,10):
#         if i<=5:
#             print(i*'*'+((5-i)*2*" ")+i*"*")
#         else:
#               print((10-i)*"*"+(i-5)*2*" "+(10-i)*"*")
              
# for i in range(1,8):
#       if i<=4:
#             print((5-i)*"*"+(i-1)*2*" "+(5-i)*"*")
#       else:
#             print((i-3)*"*"+(7-i)*2*" "+(i-3)*"*")

# login={
#     "admin":"adm123"
# }
# pro=input("Are you a new user to the system?(yes/no)")
# if pro=="yes":
#     while pro=="yes":
#         name=input("Enter username : ")
#         if name in login:
#             print("Username already exists")
#             continue
#     email=input("Enter email : ")
#     passw=input("Enter password : ")
#     conf=input("confirm password : ")
# if conf!=passw:
#     print("error")

# def my_fn(a):
#     return "hello"+a
# print(my_fn("gopika"))

# def is_perfect(num):
#     sum=1
#     for i in range(2,num//2+1):
#         if num%i==0:
#             sum+=i
#     return sum==num
# if is_perfect(6):
#     print("perfect")
# else:
#     print("not")

# num=int(input("enter a num: "))
# sum=0
# pdt=1
# while num!=0:
#     r=num%10
#     num=num//10
#     sum=sum+r
#     pdt=pdt*r
# # print(sum)
# # print(pdt)
# if sum==pdt:
#     print("spy")
# else:
#     print("not")
 
# def selfdiv(lef,rig):
#     li=[]
#     for i in range(lef,rig+1):
#         temp=i
#         flag=True
#         while i!=0:
#             rem=i%10
#             if rem!=0:
#                 div=temp%rem
#             else:
#                 flag=False
#                 break
#             if div!=0:
#                 flag=False
#                 break
#             i=i//10
#         if flag:
#             li.append(temp)
#     return(li)
# print(selfdiv(47,85))


# def is_perfect(num):
#     sum=1
#     for i in range(2,num//2+1):
#         if num%i==0:
#             sum+=i
#     return sum==num
# def is_armstrong(num):
#     temp=num
#     sum=0
#     while num>0:
#         rem=num%10
#         sum=sum+rem**3
#         num=num//10
#     return sum==temp
# def is_prime(num):
#     if num == 1:
#         print("Neither prime nor composite")
#     else:
#         for i in range(2,num):
#             if num%i==0:
#                 break
#         else:
#             print("prime")
# li=[1,2,3,7,6,17,23,28,153,121]
# for i in li:
#     if is_perfect(i):
#         print("Perfect no : ",i)
#     if is_armstrong(i):
#         print("Armstrong no : ",i)
#     if is_prime(i):
#         print("Prime no : ",i)

