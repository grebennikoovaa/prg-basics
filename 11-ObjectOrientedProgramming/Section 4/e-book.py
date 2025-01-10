class eBook:
    def __init__(self, title, author, number_of_pages, is_open=False):
        self.title = title
        self.author = author
        self.number_of_pages = number_of_pages
        self.current_page = 1
        self.is_open = is_open
    
    def open_book(self):
        if not self.is_open:
            self.is_open = True
            print("open")
        else:
            print("already open")

    def display_status(self):
        status = "open" if self.is_open else "closed"
        print(self.title)
        print(self.author)
        print(self.current_page)
        print(self.number_of_pages)
        print(status)

    