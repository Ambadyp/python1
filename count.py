str=input("enter the string value")
count=0
for i in range(0,len(str)):
    if str[i]!= '':
        count+=1
    
print(count)
