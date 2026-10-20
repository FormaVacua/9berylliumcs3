class Publication:
  def __init__(self, title, author):
    self.__title = title
    self.__author = author

  @property
  def get_title(self):
    return f"{self.__title}"

  @get_title.setter
  def set_title(self, new_title):
    self.__title = new_title

  @property
  def get_author(self):
    return f"{self.__author}"
    
  @get_author.setter
  def set_author(self, new_author):
    self.__author = new_author
    
  def display_info(self):
    print(f"Author: {self.get_author} || Title: {self.get_title}")

##
class Book(Publication):
  def __init__(self,title,author,number_of_pages):
    super().__init__(title,author)
    self.__number_of_pages = number_of_pages
    
  @property
  def get_number_of_pages(self):
    return f"{self.__number_of_pages}"
    
  @get_number_of_pages.setter
  def set_number_of_pages(self, new_number_of_pages):
    self.__number_of_pages = new_number_of_pages
    
  def display_info(self):
    print(f"Author: {self.get_author} | Title: {self.get_title} | Number of Pages: {self.__number_of_pages}")

##
class Magazine(Publication):
  def __init__(self,title,author,issue_number):
    super().__init__(title,author)
    self.__issue_number = issue_number

  @property
  def get_issue_number(self):
    return f"{self.__issue_number}"
    
  @get_issue_number.setter
  def set_issue_number(self, new_issue_number):
    self.__issue_number = new_issue_number
  
  def display_info(self):
    print(f"Author: {self.get_author} | Title: {self.get_title} | Issue Number: {self.__issue_number}")

pub1 = Publication("Wanderer's Journal","Ellina the Chronicller")
book1 = Book("Book 1", "Bill Cipher", 320)
mag1 = Magazine("Vogue", "Lauren Lopez", 202)

print("Publication Information: ")
pub1.display_info()

print("\nBook Information:")
book1.set_number_of_pages(-310) 
book1.display_info() 
book1.get_number_of_pages()

print("\nMagazine Information:")
mag1.display_info() 
mag1.get_number_of_pages()
