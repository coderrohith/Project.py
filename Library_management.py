books=[]

while True:
    print("\n1.Add Book")
    print("2.View Books")
    print("3.Exit")

    choice=int(input("Enter your choice:"))

    if choice == 1:
        book=input("Enter Book name :")
        books.append(book)

    elif choice == 2:
        print("\ Books in Library:")
        for book in books:
            print(book)

    elif choice == 3:
        break

