def swap(a):
    start=a[0]
    end=a[-1]
    x=a[1:-1]
    y=end+x+start
    return y
a=input("enter a string")
n=swap(a)
print("THe exchanged string",n)
