class Publication: # creates class Publication
  def __init__(self, title, author): # the class has a title and author
    self.__title = title
    self.__author = author

  @property # since the author and title are private, there should be indirect access through getters and setters, hence:
  def get_title(self):
    return f"{self.__title}"

  @get_title.setter # .setter of get_title which allows the __title to be changed
  def set_title(self, new_title):
    self.__title = new_title

  @property # same as the previous property-setter decorators
  def get_author(self):
    return f"{self.__author}"
    
  @get_author.setter
  def set_author(self, new_author):
    self.__author = new_author
    
  def display_info(self):
    print(f"Author: {self.get_author} || Title: {self.get_title}") #displays using get_

## New class
class Book(Publication): # Book(Publication) is a child class of Publication
  def __init__(self,title,author,number_of_pages):
    super().__init__(title,author)
    self.__number_of_pages = number_of_pages # the number of pages is private
    
  @property
  def get_number_of_pages(self): #same as before, uses getters and setters
    print(self.__number_of_pages)
    
  @get_number_of_pages.setter
  def set_number_of_pages(self, new_number_of_pages):
    if new_number_of_pages > 0:
      self.__number_of_pages = new_number_of_pages #makes sures it's positive 
    else:
      print("Must be a positive number.")
      
  def display_info(self):
    print(f"Author: {self.get_author} | Title: {self.get_title} | Number of Pages: {self.__number_of_pages}")

## Magazine subclass
class Magazine(Publication):
  def __init__(self,title,author,issue_number):
    super().__init__(title,author)
    self.__issue_number = issue_number # private

  @property 
  def get_issue_number(self): #get_issue number is private so there's getters and setters
    print(self.__issue_number)
    
  @get_issue_number.setter # sets
  def set_issue_number(self, new_issue_number):
    self.__issue_number = new_issue_number
  
  def display_info(self):
    print(f"Author: {self.get_author} | Title: {self.get_title} | Issue Number: {self.__issue_number}") #displays using get_ from the parent class and __issue_number from the subclass

##testing
pub1 = Publication("Wanderer's Journal","Ellina the Chronicller") 
book1 = Book("Book 1", "Bill Cipher", 320) #adds the page numbers
mag1 = Magazine("Vogue", "Lauren Lopez", 202) #adds the issue number

print("Publication Information: ")
pub1.display_info() #prints the author, and title

print("\nBook Information:") #information on the literature
book1.display_info() #prints the book details. author, title, and number of pages
print(book1.get_number_of_pages) #prints the number of pages

print("\nMagazine Information:") 
mag1.display_info() #prints the magazine details. the author, title and issue number
print(mag1.get_issue_number) #prints just the issue number
