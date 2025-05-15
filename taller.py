books = []
category = ""
def add_book(books):
    id = 0
    title = input("Title of the book: ")
    author = input("Author of the book: ")
    while True:
        year = input("Year of publication: ")
        if year.isdigit() and int(year) >= 1500 and int(year) <= 2025:
            while True:
                print("Select the type of book ")
                print("[1] Fiction")
                print("[2] No fiction")
                print("[3] Infantila")
                print("[4] Educative")
                category = input("What is the book's category?: ")
                if category == "1":
                    category = "Fiction"
                    break
                elif category == "2":
                    category = "No fiction"
                    break
                elif category == "3":
                    category = "Infantila"
                    break
                elif category == "4":
                    category = "Educative"
                    break
                else:
                    print("Invalid value")
            while True:
                print("Select the type of book ")
                print("[1] Avaliable")
                print("[2] Borrowed")
                state = input("What is the book's state?: ")
                if state == "1":
                    state = "Avaliable"
                    break
                elif state == "2":
                    state = "Borrowed"
                    break
                else:
                    print("Invalid value")
            id += 1
            book = {"id": id, "title": title, "author": author, "year": year, "category": category,"state": state}
            books.append(book) 
            print(" Libro añadido correctamente.")
            print(books)     
        else:
            print(" Error: The year of publication must be between 1500 and 2025")         
add_book(books)
