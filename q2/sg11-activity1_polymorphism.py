class Patient: # creates the parent class Patient
  def __init__(self,name,bill_amount):
    self.__name = name
    self.__bill_amount = bill_amount # instantiates the name and bill amount, also sets it as private
    
  @property #propertyies for both getting the name and bill amount of a patient
  def get_name(self):
    return self.__name

  @get_name.setter
  def set_name(self, new_name):
    self.__name = new_name
    
  @property
  def get_bill_amount(self):
    return self.__bill_amount
    
  @get_bill_amount.setter
  def set_bill_amount(self,new_bill_amount):
    self.__bill_amount = new_bill_amount
    
  def calculate_bill(self): # calculates the bill amount, much more relevant in child classes
    return self.__bill_amount
    
  def display_patient_type(self):
    print("Regular Patient")

class Senior_Patient(Patient): # senior patient class, uses a 20% discount
  def __init__(self,name,bill_amount):
    super().__init__(name,bill_amount)
    
  def calculate_bill(self):
    return self.get_bill_amount * 0.80 #the bill is set
    
  def display_patient_type(self):
    print("Senior Patient") #specific for each subclass
    

class PhilHealth_Patient(Patient): # philhealth patient class, uses a 15% discount
  def __init__(self,name,bill_amount):
    super().__init__(name,bill_amount)
    
  def calculate_bill(self):
    return self.get_bill_amount * 0.85
    
  def display_patient_type(self):
    print("PhilHealth Patient")    

#testing the patient classes

p1 = Patient("Talis", 1980.0)
p2 = Senior_Patient("River", 1980.0)
p3 = PhilHealth_Patient("Veritas", 1980.0)

print ("-- HOSPITAL BILLING SYSTEM --")

for i in patients:
  print(f"Name: {i.get_name}")
  print(f"Patient Type: {i.display_patient_type()}")
  print(f"Bill: {i.get_bill_amount:.2f}")
  print(f"FINAL Bill: {i.calculate_bill():.2f}")
    
