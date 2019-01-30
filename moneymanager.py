class MoneyManager():
    user_account_number = '0'
    user_pin_number = ''
    user_balance = 0.0
    type_ = ''
    list_of_transaction = []

        
    def user_entry(self, money, type_):
        '''Function to add and entry an amount to the tool. Raises an
        exception if it receives a value for amount that cannot be cast to float. Raises an exception
        if the entry_type is not valid - i.e. not food, rent, bills, entertainment or other'''
        try:
            money_and_type = float(money)
            if( money_and_type > self.user_balance):
                raise Exception('The entry is not valid!!')
            self.user_balance = float(self.user_balance) -  money_and_type   
            transaction = ('Withdrawal', money_and_type)
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

        f = open(str(bank_account.user_account_number) +'.txt',"w+")

        f.write(bank_account.account_number + '\n')

        f.write(bank_account.user_pin_number + '\n')

        f.write(str(bank_account.user_balance) + '\n')

        f.write(str(bank_account.interest_rate) + '\n')

        for a in bank_account.transaction_list:

            file.write(str(a[0]) + '\n')

            file.write(str(a[1]) + '\n')

        file.close()
    



