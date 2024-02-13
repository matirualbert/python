class Mpesa:
    def __init__(self,account_balance,phone_number):
        self.account_balance = account_balance
        self.phone_number = phone_number
    def send_money(self,amount,receipient):
        if self.account_balance >= amount:
            self.account_balance -= amount
            print(f"{amount} KES sent to {receipient}")
        else:
            print("insufficient amount to send money")

class PersonalMpesa(Mpesa):
    def __init__(self,account_balance,phone_number,id_number):
        super() .__init__(account_balance,phone_number,)
        self.id = id_number
    def buyairtime(self,amount):
        self.account_balance -= amount
        print(f"{amount} KES airtime bought successfully bought.")

class BusinessMpesa(Mpesa):
    def __init__(self,account_balance,phone_number,business_id):
        super().__init__(account_balance,phone_number)
    def Receive_payment(self,amount):
        self.account_balance += amount
        print(f"{amount} KES received from a customer.")

person=PersonalMpesa(100,34344234,314453)
person.send_money(300,578593)
person.buyairtime(150)
person = BusinessMpesa(2000000,54879457,97673)
person.Receive_payment(4000)
