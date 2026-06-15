
# main function 
def main():
      
      #ask bill amount 
      dollars=dollars_to_float(input("How much was your meal  ? "))
     
       #ask tip percent 
      percent=percent_to_float(input("How much would you like to tip ? "))
      
      #calculate tip
      tip=dollars*percent
      
      #print tip
      print(f"LEAVE  ${tip:,.2f} ")
      

#functions to convert str to float 
def dollars_to_float(d):
      
      #remove unnecessary things 
      d=d.replace('$' ,'') .strip()
     
       #change bill amount into float and return 
      return float(d)

def percent_to_float(p):
      #remove unnecessary things 
      p=p.replace('%', '').strip()
      #change tip percent into float 
      p=float(p)
      #make percent in decimal form
      p/=100
      #return value
      return p


# if-main block
if __name__ == '__main__' :
      main()