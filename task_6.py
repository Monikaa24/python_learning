a=input("enter the sentence : ")
b=len(a)
c=b//2
l=0
if b%2==0:
    for i in range(1,c+1):
       l+=i
    print(l)
else:
   for i in range(1,b+1):
       l+=i
   print(l)
    
    
