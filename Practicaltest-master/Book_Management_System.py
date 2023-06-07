import sys

from Book import *

def Bubblesort(records):
            length = len(records)
            for i in range(length - 1,0,-1):
                for j in range(i):
                    if records[j]['Category'] > records[j+1]['Category']:
                        tmp = records[j]
                        records[j] = records[j + 1]
                        records[j + 1] = tmp

def selectionsort(records):
    n = len(records)
    for i in range(n-1):
        max_index = i
        for j in range(i+1, n):
            if records[j]['Publisher'] > records[max_index]['Publisher']:
                max_index = j
        if max_index != i:
            tmp = records[i]
            records[i] = records[max_index]
            records[max_index] = tmp

def duplication_check(records,ISBN):
    new_books = ISBN
    for dict_item in records:
        if dict_item['ISBN'] == new_books:
            return True
    return False



books = Book('ISBN', 'Title', 'Category', 'Publisher', 'Year_published')
count=1
x=1
y=1
records = books.records
bubble_records = books.records
select_records = books.records
while True:
    menu = '''
    This is Books! books records:
    1. Display all of the books in the record
    2. Add a new book to the record
    3. Sort the books by their Category in ascending order
    4. Sort the books by their Publisher in descending order
    5. Exit the program
    6. Search a book
    '''
    print(menu)

    option_input = input("What are do want to do? (Please select the number only): ")

    if option_input == '1':
        for i in records:
            print(count,':',i)
            count+=1
        count=1


    elif option_input == '2':
        try:
            ISBN = input("What is the new book's ISBN?: ")
            while True:
                if not ISBN.isdigit():
                    print("It must be in digits")
                elif len(ISBN) < 13:
                    print("ISBN needs to be at least 13 digits")
                elif duplication_check(records, ISBN):
                    print("Duplicate found")
                else:
                    break
                ISBN = input("What is the new book's ISBN?: ")
            ISBN = int(ISBN)

            title = input("What is the new book's title?: ")
            while True:
                if not title.isalpha():
                    print("It must not be empty")
                else:
                    break
                title = input("What is the new book's title?: ")
            Title=title.title()
            category = input("What is the new book's Category?: ")
            while True:
                if not category.isalpha():
                    print("It must not be empty")
                else:
                    break
                category = input("What is the new book's Category?: ")
            Category=category.title()
            publisher = input("Who is the publisher?: ")
            while True:
                if not publisher.isalpha():
                    print("It must not be empty")
                else:
                    break
                publisher = input("Who is the publisher?: ")
            Publisher = publisher.title()
            Year_Published = input("When was it published?: ")
            while True:
                if not Year_Published.isdigit():
                    print("It must be in digits")
                elif int(Year_Published) in range(1899, 2024):
                    break
                else:
                    print("Please enter a valid year (1900 - current)")
                Year_Published = input("When was it published?: ")
            Year_Published = int(Year_Published)

            new_book = {'ISBN': ISBN,'Title':Title,'Category':Category,'Publisher':Publisher,'Year_Published':Year_Published}

            books.add_record(new_book)
            print("Book titled",Title,"has been added")

        except EnvironmentError:
            print("You have entered a wrong key")
            print(menu)
            option_input = input("What are do want to do? (Please select the number only): ")

    elif option_input == '3':
        Bubblesort(bubble_records)
        for i in records:
            print(x,':',i)
            x+=1
        print("The books has been sorted by Categories")
        x=1

    elif option_input == '4':
        selectionsort(select_records)
        for x in records:
            print(y,':',x)
            y+=1
        print("The books has been sorted by Publisher")
        y=1

    elif option_input == '5':
        print("Goodbye")
        sys.exit()

    elif option_input == '6':
        ISBN_search = input("Enter the ISBN you want to search: ")
        ISBN_search = int(ISBN_search)
        for item in records:
            if item['ISBN'] == ISBN_search:
                print(item)
                break
        else:
            print("The book you are searching for is not found")
            pass
    else:
        print("Please enter a valid number")

