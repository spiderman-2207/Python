import time
import os

while True :
    try:
        time_h=int(input("ENTER hour : "))
        time_m=int(input("ENTER minute "))
        time_s=int(input("ENTER seconds "))
        choice=input("press ENTER to start timer or 'Q' to quit").lower()
        if choice == 'q':
            break
    except ValueError:
        print("~~~~~INVALID INPUT~~~~~")
    seconds=(time_h*60*60)+(time_m*60)+time_s
    i=0
    while i < seconds :
        print(f"{time_h} : {time_m} : {time_s}")
        if time_s > 0 :
            time_s-=1
        else:
            time_s=59

        if time_m != 0 and  time_s == 59 :
            time_m-=1
        if time_h !=0 and time_m == 59 and time_s== 59 :
            time_h -= 1
        time.sleep(0.009e+10)
        os.system('clear')
        i-=1
    break
