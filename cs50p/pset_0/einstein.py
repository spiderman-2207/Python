#main function
def main():
    mass=float(input("\n Enter mass (in kg) :  "))
    print(f"Energy  :  {convert(mass):,.0f}  joules .")
    
#function to convert mass into energy
def convert(quantity):
    return quantity*((3e8)**2)

if __name__ == '__main__' :
    main()