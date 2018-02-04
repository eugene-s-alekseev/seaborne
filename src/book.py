import bisect
from collections import deque


class Book():
    def __init__(self, book=deque()):
        self.book = book


    @classmethod
    def get_book(book_type):
        if book_type == "sell":
            return SellBook()
        elif book_type == "buy":
            return BuyBook()


    def take_order(self, order):
        bisect.insort(self.book, order)


    def get_top_order(self):
        pass


    def get_current_price(self):
        return self.current_price


    def __str__(self):
        return "\n".join([str(item) for item in self.book])


    def __repr__(self):
        return "\n".join([str(item) for item in self.book])


class SellBook(Book):
    def __init__(self, book=deque()):
        super().__init__(book)
        if len(book) != 0:
            self.current_price = book[0].price
        else:
            self.current_price = 0


    def get_top_order(self):
        order = self.book.popleft()
        self.current_price = order.price
        return order


class BuyBook(Book):
    def __init__(self, book=deque()):
        super().__init__(book)
        if len(book) != 0:
            self.current_price = book[-1].price
        else:
            self.current_price = 0


    def get_top_order(self):
        order =  self.book.pop()
        self.current_price = order.price
        return order
