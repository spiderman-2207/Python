# a simple calculator

print("\n\n\t\t==========\n\t\tCALCULATOR\n\t\t==========\n\n")



#asking inputs
while 1 :
    operator=input("ENTER A OPERATOR (+,-,*,/) : ")
    if operator not in ('+','-','*','/'):
        print("invalid operator\n")
    else:
        break ;
while 1 :
    try:
        num1=int(input("ENTER NUMBER 1 : "))
        num2=int(input("ENTER NUMBER 2 : "))
        break;
    except:
        print("INVALID")




#calculating result
if operator == '+' :
    result=num1+num2
elif operator == '-' :
    result=num1-num2
elif operator == '*' :
    result=num1*num2
try :
    if operator == '/' :
        result=num1/num2
except ZeroDivisionError :
    print("CANNOT DIVIDE BY ZERO")
    quit()


#printing  result
print("RESULT : ",result)
