list=[]
n=int(input("enter the number  of elemnets  of the list"))
for i in range(0,n):
    element=input("enter the element"+str(i+1)+":")
    list.append(element)
max=len(list[0])
temp=list[0]
for i in list:
    if(len(i)>max):
        max=len[i]
        temp=i
print("longest word is:",temp)
