import builtins


class atm:

    def __init__(self, cardNo, pinNo):
        self.cardNo=cardNo
        self.pinNo=pinNo

    def checkBalnce(self):
        print("The amount you have is 97,778, Indeed you are rich!")

    def withdrawl(self, cashLeft):
        new_val=97,778-cashLeft
        print("You have withdrawn")

    def exit(self, bill):
        print("Here is the exit bill, please come back later for withdarwing, I wont run! ")
        print(bill)


        