#compound intrest calculator 

#title
print("\n\n\t ===========================")
print("\t COMPOUND INTEREST CALCULATOR")
print("\t ===========================\n\n")



# this loops the entire process
while True :



    #principal amount
    while True :
        try:
            principal=float(input("\nEnter principal amount : ₹"))
            if principal < 1 :
                print("\nPrincipal amount can't be less than 1.")
                continue
            else:
                break
        except ValueError :
            print("\n~~~INVALID INPUT~~~")
            




    # annual intrest rate
    while True :
        try:
            a_rate=float(input("\nEnter annual intrest rate (in %) : "))
            if a_rate < 1 :
                print("\nannual intrest rate can't be less than 1.")
                continue
            else:
                break
        except ValueError :
            print("\n~~~INVALID INPUT~~~")
            continue




    #no. of times intrest compounds per year
    while True :
        try:
            n=float(input("\nEnter number of times interest compounds per year : "))
            if n < 1 :
                print("\ncompounding frequency can't be less than 1. ")
                continue
            else:
                break
        except ValueError :
            print("\n~~~INVALID INPUT~~~")
            continue




    #total period
    while True :
        try:
            time=float(input("\nEnter time period in years :  "))
            if time < 1 :
                print("\natleast one year have to be calculated .")
                continue
            else:
                break
        except ValueError:
            print("\n~~~INVALID INPUT~~~")
            continue





#calculating and printing amounts
    a_rate/=100
    f_amt=principal*((1+(a_rate/n))**(n*time))
    e_amt=f_amt-principal
    print("\n\n~~~~~~~~~~~~~~~~~~~~~~~~~")
    print(f"Final amount: ₹{f_amt:,.2f}")
    print(f"Amount earned: ₹{e_amt:,.2f}")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~\n\n")




#asking if user want to leave or continue
    choice=input("Do you want to continue (y/n) [default:n] : ").lower()
    if choice != 'y' :
        break
