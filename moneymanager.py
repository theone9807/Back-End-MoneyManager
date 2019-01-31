class MoneyManager():
    user_account_number = ''
    user_pin_number = ''
    user_balance = 0.0
    type_ = ''
    interest_rate = 0.0
    list_of_transaction = []


    def __init__(self):
        '''Constructor to set username to '', pin_number to an empty string,
        balance to 0.0, and transaction_list to an empty list.'''
        self.user_account_number = ''
        self.user_pin_number = ''
        self.user_balance  = 0.0
        self.list_of_transaction = []

        
    def user_entry(self, money, type_):
        '''Function to add and entry an amount to the tool. Raises an
        exception if it receives a value for amount that cannot be cast to float. Raises an exception
        if the entry_type is not valid - i.e. not food, rent, bills, entertainment or other'''
        type_valid = ['food', 'rent', 'bills', 'entertainment','other']
        try:
            money_ = float(money)
            if( money_ > self.user_balance) or (type_ not in type_valid) :
                raise Exception('The entry is not valid!!')
            self.user_balance = float(self.user_balance) -  money_   
            transaction = ('Withdrawal', money_, type_)
            self.list_of_transaction.append(transaction)
            
        except Exception as e:
            print(repr(e))
      
    

    def take_money(self, Amount):
        '''Function to deposit an amount to the user user_balance. Raises an
        exception if it receives a value that cannot be cast to float. '''
        try:
            amount_deposit = float(Amount)
            self.user_balance = float(self.user_balance) + amount_deposit
            transaction = ('Deposit',amount_deposit)
            self.list_of_transaction.append(transaction)
            
        except Exception as error:
            print(repr(error))

      
    def get_details(self):
        '''Function to create and return a string of the transaction list. Each transaction
        consists of two lines - either the word "Deposit" or the entry type - food etc - on
        the first line, and then the amount deposited or entry amount on the next line.'''
        #transaction = self.transaction_list[-1]
        transaction_string = ''
        transaction = self.list_of_transaction
        
        for index, t in enumerate(self.list_of_transaction):
            transaction_string = transaction_string + str(t[0])+'\n'+str(t[1])+'\n'
        return transaction_string

    def save_to_a_file(self):
        '''Function to overwrite the user text file with the current user
        details. user number, pin number, and balance (in that
        precise order) are the first four lines - there are then two lines
        per transaction as outlined in the above 'get_transaction_string'
        function.'''

        f = open('details.txt',"w+")

        f.write(str(self.user_account_number) + '\n')

        f.write(self.user_pin_number + '\n')

        f.write(str(self.user_balance) + '\n')

        f.write(str(self.interest_rate) + '\n')

        for a in self.list_of_transaction:

            f.write(str(a[0]) + '\n')

            f.write(str(a[1]) + '\n')

        f.close()
    



m= MoneyManager()

m.take_money(400)

# # print(m.user_balance)
m.user_entry(200, 'rent')
print(m.list_of_transaction)
print(m.get_details())

# print(m.save_to_a_file())