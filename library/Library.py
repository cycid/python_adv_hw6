class Library:


    def __init__(self, name, list_of_books=None, list_of_readers=None):
        self.name=name
        self.list_of_books = []
        self.list_of_readers = []



    def __repr__(self):
        return f'{self.name}'


    def add_book(self, book):
        self.list_of_books.append(book)
        return f'book was added successful'


    def del_book(self, id_book):
        for item in self.list_of_books:
            if item.id==id_book:
                self.list_of_books.remove(item)
        return None



    def give_book_to_reader(self, book_id, reader_id):

        """
        the function change the status lib to status with reader
        status lib means the book is in library
        :param book: book object
        :param reader: reader object
        :return: message with operation
        """
        for book in list_of_books:
            if book.id==book_id:
                for user in self.list_of_readers:
                    if user.id==user_id:
                        book.status=user.id
                        return True      



    def get_book_from_reader(self,book_id):
        """
        the func return book from any reader who had it

        """
        for book in self.list_of_books:
            if book.id==book_id:
                book.status="lib"
                return True

    def print_books(self,param):
        """the function return books in library depends on parameter

        :param param: could be "all", "in" mean in library, and "out" mean out of library
        :return:
        """
        book_list=''
        if param=="all":            
            for item in self.list_of_books:
                book_list+=str(item)+"\n"          
            return book_list
                #iterating all list of books and if book is in library - print it
        elif param=="in":
            for item in self.list_of_books:
                if item.status=="lib":
                    book_list+=str(item)+"\n"
                else:pass
            return book_list
        else:
            for item in self.list_of_books:
                if item.status!="lib":
                    book_list+=str(item)+"\n"                 
                else:pass
            return book_list



    def sort(self,param):
        book_list=''
        if param=="year":
            sorted_list=sorted(self.list_of_books, key=lambda item:item.year)
            for i in sorted_list:
                book_list+=str(i)+"\n"   
            return book_list
        elif param=="name":
            sorted_list = sorted(self.list_of_books, key=lambda item: item.name)
            for i in sorted_list:
                book_list+=str(i)+"\n"   
            return book_list
        elif param=="author":
            for i in sorted_list:
                book_list+=str(i)+"\n"   
            return book_list
        else:
            raise Exception("Sorry, keyword wasnt correct")
        return print("all the books in our library")

    def show_user_book(self,user):
        print(f"{user} have such books:")
        for item in self.list_of_books:
            if item.status==user:
                print(item)
            else:
                pass