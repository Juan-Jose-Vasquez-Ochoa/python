books = {}

id = 1

def add_book(books):

    cont = True
    global id
    
    
    title = input("Title of the book: ")
    author = input("Author of the book: ")
    
    while cont:

        try:

            year = int(input("Year of publication: "))
            if 1500 > year > 2025:
                print(" Error: The year of publication must be between 1500 and 2025")
                continue
            cont = False
        
        except ValueError:
            print(" Error: Ingresa valores numéricos válidos." )
        year = str(year)

    category = input("What is the book's category?: ")
    state = input("What is the book's state? (avaliable/borrowed): ")
    books[id] = {"title": title, "author": author, "year": year, "category": category,"state": state}
    print(" Libro añadido correctamente.")
    id += 1

add_book(books)

print(books)