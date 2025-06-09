class Book:
    def __init__(self,title:str,author:str,isbn:str):
        self._title=title
        self._author=author
        self._isbn=isbn
        self.is_borrowed=False

    def __str__(self)->str:
        return f"Titolo: {self._title}; Autore: {self._author}; isbn: {self._isbn.upper()}"
    
    @classmethod
    def from_string(cls,str_repr:str):
        words:list[str]= str_repr.split(",")
        if len(words) != 3:
            raise ValueError("La stringa deve essere nel formato 'Titolo,autore,isbn'")
        new_list:list[str]=list()
        for word in words:
            new_list.append(word.strip())
        title = new_list[0]
        author = new_list[1]
        isbn = new_list[2]
        return cls(title,author,isbn)

class Member:
    def __init__(self,name:str,member_id:str,borrowed_books:list)->None:
        self.name=name
        self.member_id=member_id
        self.borrowed_books=borrowed_books

    def borrow_book(self,book:Book)->None:
        if not book.is_borrowed:
            book.is_borrowed=True
            self.borrowed_books.append(book)
        raise ValueError(">Libro già in prestito")
    
    def return_book(self,book:Book)->None:
        if book in self.borrowed_books:
            book.is_borrowed=False
            self.borrowed_books.remove(book)
        raise ValueError("Il libro non può essere rimosso")
    
    def __str__(self)->str:
        return f"{self.name} membro, ID: {self.member_id}. Borrowed books {self.borrowed_books.split(",")}"

    @classmethod
    def from_string(cls,str_member:str):
        words:list[str]=str_member.split(",")
        if len(words) != 2:
            raise ValueError("Non ci possono essere campi vuoti")
        
        new_list:list[str]=list()
        for word in words:
            new_list.append(word)

        name=new_list[0]
        member_id=new_list[1]
        return cls(name,member_id)


class Library:
    total_books:int=0
    def __init__(self)->None:
        self.books:list[str]=list()
        self.members:list[str]=list()
        

    def add_book(self,book:Book):
        if book not in self.books:
            self.books.append(book)
            Library.total_books+=1
        raise ValueError("Libro già nella libreria")
    
    def remove_book(self,book:Book):
        if book in self.books:
            if not book.is_borrowed:
                self.books.remove(book)
                self.total_books-=1
            raise ValueError("Libro in prestito")
        raise ValueError("Libro non nella libreria")

    def register_member(self,member:Member):
        if member not in self.members:
            self.members.append(member)
        raise ValueError("Membro già inserito")
    
    def library_statistics(self)->int:
        return Library.total_books
    
    def __str__(self)->str:
        return f"{self.books} e {self.members}"
    
    def lend_book(self,book:Book,member:Member)->None:
        if book in self.books and member in self.members and book.is_borrowed == False:
            member.borrow_book(book)
            print("Libro prestato al membro")
        raise ValueError("Errore")
    


if __name__ == '__main__':
    book_str:str = "La Divina Commedia,D.Alighieri,999000666"
    b:Book= Book.from_string(book_str)
    print(b)


