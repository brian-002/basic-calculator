print("this is python preview on operators")
#operators
hesabu=input("enter first number:")
op=input("enter your operator:")
weka=input("enter second number:")
def culculator():
     if op =="+":
         count=float(hesabu)+float(weka)
     elif op=="/":
         count=float(hesabu)/float(weka)
     elif op=="*":
         count=float(hesabu)*float(weka)
     elif op=="-":
         count=float(hesabu)-float(weka)
     elif op=="%":
         count=float(hesabu)%float(weka)
     print(count)
print(culculator())
