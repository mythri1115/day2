num1=int(input("enter the first integer number :"))
num2=int(input("enter the second integer number:"))
if(num1==num2):
    print("the numbers are equal")
else:
    print("not equal")
print("-----------------")
a=12
b=15
result="equal" if(a==b) else " not equal"
print(result)
print("---------------------------------------------------------------")
num1=int(input("enter the first integer number :"))
num2=int(input("enter the second integer number:"))
if(num1>num2):
    print("greatest number")
else:
    print("not a greatest number")
print("------------------------------------------------------------------------")
a=12
b=16
result="greast number" if(a>b) else "smallest number"
print(result)
print("-----------------------------------------------------------------------------")
a=7
b=8
if(a<b):
    print("smallest number")
else:
    print("not a smallest number")
print("--------------------------------------------------------------------------")
a=4
b=5
result="smallest" if(a<b) else "not a smallest"
print("------------------------------------------------------------------------------")
a=int(input("enter the a vaue"))
b=int(input("enter the b value"))
c=int(input("enter the c value"))
if((a>b and a<c) or (a<b and a>c)):
    print("a is middle value")
elif((b>a and b<c) or (b<a and b>c)):
    print("b is middle value")
else:
    print("c is middle vlaue")
print("-----------------------------------------------------------------------------------")
a=5
b=6
c=9
