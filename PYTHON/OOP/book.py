class book:
    book_name:str
    author:str
    price:str
    pages:int

    def __init__(self,name,author,price,pages):
        self.book_name=name
        self.author=author
        self.price=price
        self.pages=pages
    
    def get(self):
        print(self.book_name,self.author,self.price,self.pages)
    def __str__(self):
        return (self.author)+str(self.price)  #__str__ meathod must always return string value , this is also overriding

book1=book("AADUJEEVITHAM","Benyamin",990,2000)
print(f"AUTHOR OF {book1.book_name} IS {book1.author}")
book1.get()
print(book1)
