#weight converter

print("\n\n\t\t================")
print("\t\tWEIGHT CONVERTER")
print("\t\t================")

while 1 :
    try :
        weight=float(input("\n\nEnter the weight : "))
        if weight < 0 :
            print("Enter a valid weight : ")
            continue
        else:
            break
    except :
        print("Enter a valid weight : ")
        continue


r_weight=round(weight,2)
while 1 :
    unit=input("Enter the unit (kg or lb) : ").lower()
    if unit == "kg" :
        print(f"{r_weight} kg is equal to {round(weight*2.2046,2)} lb .")
        break
    elif unit == "lb" :
        print(f"{r_weight} lb is equal to {round(weight/2.2046,2)} kg  .")
        break
    else:
        print("Enter a valid unit : ")
        continue   
