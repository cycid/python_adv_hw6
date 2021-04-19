"""
task:
Библиотека

Создать три класса:
1. Класс библиотека
Поля:
- список книг (list Books)
- список читателей (list Readers)

Методы:
- Добавить книгу
- Удалить книгу
- Отдать книгу читателю
- Принять книгу от читателя

- Вывести список всех книг
- Вывести список книг в библиотеке (в наличии)
- Вывести списк книг, которые не в наличии

- Отсортировать список книг по названию, автору, году издания (lambda будет плюсом)

2. Класс книга
Поля:
- ID
- Название
- Автор
- Год издания
- ??? (этот параметр нужен!!!)

3. Класс читателя
- ???

Методы:
???
"""


from . import Library, reader, book
user1=reader.Reader("Petro")
book1=book.Book(1,"Hobbit","Tolkien", 1976,user1)
library1=Library.Library("city_lib")
    
book3=book.Book(3,"12 Rules of Life","Jordan Peterson",2018,"lib")
book2=book.Book(2,"Lord of the Rings", "Tolkien", 1960)
library1.add_book(book1)
library1.add_book(book3)
library1.add_book(book2)



if __name__ == '__main__':

    #adding data to programm
    
    library1.add_book(book1)

    #add book function(takes book obj as argument)
    library1.add_book(book3)
    library1.add_book(book2)

    #print books library have(takes param "all", "in" or any another to show all books, in library or user have it
    library1.print_books("in")
    print('\n')
    library1.print_books('any')
    print('\n')
    library1.print_books("all")
    print("\n")

    #print books user have
    library1.show_user_book(user1)

    #give book to user takes 2 arguments: book and reader
    libraryibrary1.give_book_to_reader(book3, user1)
    library1.show_user_book(user1)
    print("")





