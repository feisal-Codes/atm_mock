from datetime import date , datetime
import random
allowedUsers= {"feisal":"passwordf","love":"passwordl" , "mike":"passwordm"}
print(allowedUsers)
def atm():

    global allowedUsers
    print("enter 1 to log-in or any other to register ")
    choice=int(input())
    if(choice==1):
        print("input your details to login ")
        login()
    else:
        print("input your details to register")

        register()



def login():
  global allowedUsers
  name = input("Enter your name? \n")
  
  if (name in allowedUsers.keys()):
    password=input("your password? \n")
    checkPassword(password,name)

  else:
    print('name not found, register')
    register()
    return

def checkPassword(password,name):
    global allowedUsers

    if (password == allowedUsers[name]):
        greeting(name)
        selectedOption=int(input("please select an option"))
        if (selectedOption == 1):
            withdraw=int(input("How much would you like to withdraw?"))
            print("You have withdrawn %s " % withdraw)
        elif (selectedOption == 2):
            currentBalance=int(input("How much would you like to deposit?"))
            print("your Current balance is %s " % currentBalance)
        elif (selectedOption == 3):
            complaint=input("enter complaint")
            print("Thank you for contacting us!")
        else:
            print("Invalid selected option , please try again")
    else:
        print("password incorrect, please try again")





def greeting(name):
        today =date.today()
        now= datetime.now()

        print(now.strftime("%H:%M:%S"))
        print(today.strftime("%d-%m-%Y"))

        print("Welcome %s" % name)
        print("These are the available options:")
        print("1: Withdraw ")
        print("2: Cash Deposit ")
        print("3: Complaint ")

def register():
  global allowedUsers
  name= input("what is your name? \n")
  password=input("Choose a password(password must be atleast 8 characters)")
  if (len(password) < 8):
      print(" 8 digit password required")
      password=input("Choose a password(password must be atleast 8 characters)")

  allowedUsers[name]=password
  print("...........")
  print("registration successfull")
  print("...........")

  AccountNumber=generateAccountNumber()
  print("your accountNumber is %s " %AccountNumber )
  login()
def generateAccountNumber():
   accounts=[]
   for i in range(5):
    number=random.randint(1000000,5000000)
    if number not in accounts: 
        accounts.append(str(number))
        return  ''.join(accounts)

if __name__=="__main__":
  atm()




