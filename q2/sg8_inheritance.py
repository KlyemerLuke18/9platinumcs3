#creating of publication class
class Publication:
    def __init__(self, title: str, author: str):
        self._title = title
        self._author = author
    def get_title(self) -> str:
        return self._title
    def set_title(self, title: str):
        self._title = title
    def get_author(self) -> str:
        return self._author
    def set_author(self, author: str):
        self._author = author
    def display_info(self):
        print(f"Title: {self._title}")
        print(f"Author: {self._author}")
#creation of book class that is inherited from publication class
class Book(Publication):
    def __init__(self, title: str, author: str, number_of_pages: int):
        super().__init__(title, author)
        self.set_number_of_pages(number_of_pages)
    def get_number_of_pages(self) -> int:
        return self._number_of_pages
    def set_number_of_pages(self, number_of_pages: int):
        if number_of_pages <= 0:
            print("Number of pages must be positive.")
            self._number_of_pages = 0
        else:
            self._number_of_pages = number_of_pages
    def display_info(self):
        super().display_info()
        print(f"Number of pages: {self._number_of_pages}")

#creation of magazine class that is also inherited from publication class
class Magazine(Publication):
    def __init__(self, title: str, author: str, issue_number: int):
        super().__init__(title, author)
        self.set_issue_number(issue_number)
    def get_issue_number(self) -> int:
        return self._issue_number
    def set_issue_number(self, issue_number: int):
        if issue_number <= 0:
            print("Issue number must be positive.")
            self._issue_number = 0
        else:
            self._issue_number = issue_number
    def display_info(self):
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
