# temperature converter
print("\n\n\n\t\t~~~~~~~~~~~~~~~~~~~~~~~~~")
print("\t\t  TEMPERATURE CONVERTER ")
print("\t\t~~~~~~~~~~~~~~~~~~~~~~~~~")

print("\n\n")
while 1 :
    try:
        num=float(input("\nEnter number : "))
        break
    except:
        print("\n\nINVALID NUMBER:")

while 1:
    unit=input("Enter unit (c,k,f) : ").lower()
    if unit not in ('c','k','f'):
        print("\n\nINVALID UNIT: ")
    else :
        break


print("\n\n")
if unit == 'c' :
    c_f=round(((num*9)/5)+32,2)
    c_k=round(num+273.15 ,2)
    print(f"{round(num,2)} °c is equal to {c_f}°f .\n{num} °c is equal to {c_k} k .")

elif unit == 'k' : 
    k_c=round(num-273.15,2)
    k_f=round(((k_c *9)/5)+32,2)
    print(f"{round(num,2)} k is equal to {k_c} °c .\n{num} k is equal to {k_f} °f .")

elif unit == 'f' :
    f_c=round(((num-32) *5)/9,2)
    f_k=round(f_c + 273.15 ,2)
    print(f"{round(num,2)} °f is equal to {f_c} °c .\n{num} °f is equal to {f_k} k .")
print("\n\n")
