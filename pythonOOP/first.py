class Atm:
    #constructor 

    def __init__(self) -> None:
        self.pin=''
        self.balance=0
        self.menu()

    def menu(self):
        user_input=input("""
                Hi how can i help you?
                1.Press 1 to create pin 
                2.Press 2 to change pin     
                3.Press 3 to check balance
                4.Press 4 to to withdraw
                5.Anything else to exit
 """)
        if user_input=="1":
            self.create_pin()
        elif user_input=='2':
            self.change_pin()
        elif user_input=='3':
            self.check_balance() 
        elif user_input=='4':
            self.withdraw()
        else:
            exit()

    def create_pin(self):
        user_pin=input("enter your pin:")
        self.pin=user_pin 
        user_balance=int(input("Enter your balance:"))
        self.balance=user_balance

        print("Pin created successfully")
        self.menu()
    def change_pin(self):
        old_pin=input("enter old pin:")
        if old_pin==self.pin:
            new_pin=input("enter new pin:")
            self.pin=new_pin 
            print('pin changes successfully')
            self.menu()

    def check_balance(self):
        user_pin=input("enter the pin")
        if(user_pin==self.pin):
            print('Your balance is',self.balance)
        else:
            print('I think pin is wrong')

    def withdraw(self):
        user_pin=input('Enter the pin')  
        if(user_pin==self.pin):
            amount=input("Enter the amount")
            if(amount<self.balance):
                self.balance-=amount 
                print("withdraw successfully.balance is",self.balance)
            else:
                print('not sufficient balance')
        else:
            print("pin is wrong")
        self.menu()
        
obj=Atm()

