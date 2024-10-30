class  Bankaccount():
    _transation_hictory = []
    
    def __init__(self,  account_number, balance, account_holder):
        self.account_number = account_number
        self.balance = balance
        self.account_holder = account_holder
    
    def withdraw(self, amount):
        if self.balance - amount >= 0:
            self.balance = self.balance - amount
            print('вы сняли с баланса:', amount) 
            print('на вашем балансе осталось:', self.balance)
            self._transation_hictory.append(['снято:', amount])
        else:
            print('у вас не достаточно средств для операции') 
        print('----------')
    
    def deposit(self, amount):
        self.balance = self.balance + amount 
        self._transation_hictory.append(['внесено:', amount])
        print('внесено:', amount)
        print('ваш баланс:', self.balance)
        print('----------')
        
    def get_transaction_history(self):
        for i, element in enumerate(self._transation_hictory):
            print((i + 1), element)
        print('----------')
        
    def display_balance(self):
        print('ваш баланс:', self.balance)
        print('----------')
        
qwerty = Bankaccount(12345, 9000, 'Me')

qwerty.deposit(123)
qwerty.withdraw(12)
qwerty.display_balance()
qwerty.deposit(1111111)
qwerty.withdraw(1234567890)
qwerty.get_transaction_history()