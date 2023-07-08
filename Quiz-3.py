import sys

First_number=int(sys.argv[1])
Second_number=int(sys.argv[2])
result=First_number**Second_number
total=result
print("{}^{}={}".format(First_number,Second_number,total),end=" ")
while total>9:
    number=str(total)
    sum=0
    print("=",end=" ")
    Mylist=[]
    for i in number:
        sum= sum + int(i)
        Mylist.append(i)

    a="+".join(Mylist)
    print(a,end=" ")
    total=sum
    print("=",sum,end="")

