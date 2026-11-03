class BankAccount:
  def __init__(self,account_number, balance):
    self.__account_number = account_number
    self.__balance = balance

  # \\ getters
  @property
  def get_account_number(self):
      return f"{self.__account_number}" #returns the private value, account_number
    
  @property
  def get_balance(self):
      return f"{self.__balance}" #returns balance

  # \\ setters
  @get_account_number.setter
  def set_account_number(self, new_account_number):
        self.__account_number = new_account_number # allows the account number to be changed through 'indirect means'

  @get_balance.setter
  def set_balance(self, new_balance):
      if self.__balance < 0: #validates the balance
          print("INvalid. Enter a positive value.")
      else:
              self.__balance = new_balance #sets the balance as the new balance while also verifying the new balance

obj = BankAccount(37, 9000) #instantiates object

print("Account 1")
print(f"Account number: {obj.get_account_number}") #uses the get/getters/property command to test code
print(f"Balance: {obj.get_balance}")

new_val = 10000

print(f"\nUpdate balance to {new_val}") #new value for the balance
obj.set_balance = new_val #uses set_balance because it is a setter

print(f"Account number: {obj.get_account_number}")
print(f"Balance: {obj.get_balance}") #set_balance changes the value of the private attribute __balance, and uses get_balance to print it
