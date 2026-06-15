#main function
def main():
      
      user_input=input("What is the answer to the Great Question of Life, the Universe and Everything  ").lower().strip()
      print(check(user_input))

#function to check whether it's 42
def check(inpt):
      if inpt in ('42','forty two','forty-two'):
            return "yes"
      else:
             return "no"


# if-main block
if __name__ == '__main__' :
      main()