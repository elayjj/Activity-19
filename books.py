books = [
  {"title" : "The Great Gatsby", "author" : "F. Scott Fitzgerald", "ID" : 1, "genre" : "Fiction", "published year" : 1925, "ISBN" :  "978-0743273565", "stock" : 20, "price" : 15.99},
  {"title" : "To Kill a Mockingbird", "author" : "Harper Lee", "ID" : 2, "genre" : "Fiction", "published year" : 1925, "ISBN" : "978-0743273565", "stock" : 35, "price" : 10.99},
  {"title" : 1984, "author" : "George Orwell", "ID" : 3, "genre" : "Dystopian", "published year" : 1949, "ISBN" : "978-0451524935", "stock" : 40, "price" : 9.99},
  {"title" : "The Catcher in the Rye", "author" : "J.D. Salinger", "ID" : 4, "genre" : "Fiction", "published year" : 1951, "ISBN" : "978-0316769488", "stock" : 25, "price" : 8.99},
  {"title" : "A Brief History of Time", "author" : "Stephen Hawking", "ID" : 5, "genre" : "Non-Fiction", "published year" : 1988, "ISBN" : "978-0553380163", "stock" : 10, "price" : 18.99}
]

for book in books:
  
     print(f"title: {book['title']}, author: {book['author']}, ID: {book['ID']}, genre: {book['genre']}, published year: {book['published year']}, ISBN: {book['ISBN']}, stock: {book['stock']}, price: {book['price']},")