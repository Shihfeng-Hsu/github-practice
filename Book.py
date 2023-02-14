class Book:
    def __init__(self,author,title):
        self.author = author
        self.title = title
    
    def rent(self):
        print(f"Rentting Book : {self.title} by {self.author}")

bible = Book("God","Bible")
bible.rent()