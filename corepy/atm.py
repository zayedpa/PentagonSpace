import time
balance=20000
password=1234
print("welcome to the canara bank atm")
print("select your language")
print("1.english\n 2.hindi\n 3.malayalam")
lang=int(input())
if lang==1:
      print("insert your card")
      print("1.yes\n 2.no")
      card=int(input())
      if card==1:
            print("enter your pin")
            pin=int(input())
            if password==pin:
                  print("select the option")
                  print("1.balance enquiry\n 2.withdrawal")
                  option=int(input())
                  if option==1:
                        print("your balance is",balance)
                  elif option==2:
                        print("enter the amount you want to withdraw")
                        amt=int(input())
                        if amt%100==0 and amt<balance:
                              print("transaction completed")
                              time.sleep(2)
                              print("please collect your cash and card")
                              time.sleep(2)
                              print("you want to check balance")
                              print("1.yes\n 2.no")
                              want=int(input())
                              if want==1:
                                    print("your balance is",balance-amt)
                              else:
                                    print("thank you visit again")
                        else:
                              print("enter the correct amount")
                    
                  else:
                        print("select the correct option")
            else:
                  print("enter your pin correctly")
      else:
            print("insert your card properly")
else:
    print("select the option 1")




