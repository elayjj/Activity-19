products = [
   {"name" : "Laptop", "category" : "Electronics", "ID" : 1, "price" : 750, "stock" : 50, "supplier email" : "supplier1@gmail.com"},
   {"name" : "Desk Chair", "category" : "Furniture", "ID" : 2, "price" : 100, "stock" : 200, "supplier email" : "supplier2@gmail.com"},
   {"name" : "Smartwatch", "category" : "Electronics", "ID" : 3, "price" : 200, "stock" : 150, "supplier email" : "supplier3@gmail.com"},
   {"name" : "Notebook", "category" : "Stationery", "ID" : 4, "price" : 5, "stock" : 500, "supplier email" : "supplier4@gmail.com"},
   {"name" : "Running Shoes", "category" : "Apparel", "ID" : 5, "price" : 80, "stock" : 100, "supplier email" : "supplier5@gmail.com"}
]

for product in products:

   print(f"name: {product['name']}, category: {product['category']}, ID: {product['ID']}, price: {product['price']}, stock: {product['stock']}, supplier email: {product['supplier email']},")