num1=int(input("enter num1 : "))
num2=int(input("enter num2 : "))
num3=int(input("enter num3 : "))

for i in range (1,num3+1):
    if (i%num1==0 and i%num2==0):
        print(i)
