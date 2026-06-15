#main funcrion
def main():
    usr_input=input("ENTER : ")
    print(convert(usr_input))

#function to return emoji
def convert(text):
    return text.replace(":)","🙂").replace(":(","🙁")

if __name__ == '__main__' :
    main()