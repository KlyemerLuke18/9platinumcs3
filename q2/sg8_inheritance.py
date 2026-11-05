## Klyemer Luke S. Colico
## 9-Platinum

#creating of publication class
class Publication:
    def __init__(self, title: str, author: str):                          #defining the title and the author of the publicator and turning both into string
        self._title = title                                               
        self._author = author
    def get_title(self) -> str:                                           #defining the get_title and turning into string
        return self._title
    def set_title(self, title: str):                                      #defining the set_title and turning into string
        self._title = title
    def get_author(self) -> str:                                          #defining the get_author and turning into string
        return self._author
    def set_author(self, author: str):                                    #defining the set_author and turning into string
        self._author = author
    def display_info(self):                                               #giving the display_info, printing out the information
        print(f"Title: {self._title}")
        print(f"Author: {self._author}")
#creation of book class that is inherited from publication class
class Book(Publication):
    def __init__(self, title: str, author: str, number_of_pages: int):    #defining the title, author, and number_of_pages in a book
        super().__init__(title, author)
        self.set_number_of_pages(number_of_pages)
    def get_number_of_pages(self) -> int:                                 #defining the get_number_of_pages and turning it into integer
        return self._number_of_pages
    def set_number_of_pages(self, number_of_pages: int):                  #defining the set_number_of_pages and turning it into integer
        if number_of_pages <= 0:                                          #if function when numer_of_pages is less than or equal to 0
            print("Number of pages must be positive.")                    #doesn't count it
            self._number_of_pages = 0
        else:                                                             #else function when numer_of_pages is greater than 0
            self._number_of_pages = number_of_pages                       #counts it
    def display_info(self):                                               #displaying the info of the book
        super().display_info()                                            
        print(f"Number of pages: {self._number_of_pages}")
#creation of magazine class that is also inherited from publication class
class Magazine(Publication):
    def __init__(self, title: str, author: str, issue_number: int):       #defining the title, author, and issue_number in a magazine
        super().__init__(title, author)
        self.set_issue_number(issue_number)
    def get_issue_number(self) -> int:                                    #defining the get_issue_number and turning it into integer
        return self._issue_number
    def set_issue_number(self, issue_number: int):                        #defining the set_issue_number and turning it into integer
        if issue_number <= 0:                                             #if function when issue_number is less than or equal to 0                   
            print("Issue number must be positive.")                       #doesn't count it
            self._issue_number = 0
        else:                                                             #else function when issue_number is greater than 0 
            self._issue_number = issue_number                             #counts it
    def display_info(self):                                               #displaying the info of the book
        super().display_info()                                            
        print(f"Issue number: {self._issue_number}")
#printing of publication, book, and magazine information
print("Publication Information:")
public1 = Publication("Journal of Experimental Psychology", "Ratchiff, R. & Van Dongen, H.")
public1.display_info()
print("\nBook Information:")
book_invalid = Book("Faulty Book", "Unknown", -5) 
book1 = Book("The Hobbit", "J.R.R. Tolkien", 310)
book1.display_info()
print("\nMagazine Information:")
magasin1 = Magazine("National Geographic", "Various Authors", 202)
magasin1.display_info()
