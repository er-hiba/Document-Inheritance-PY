class Document():
    _counter = 0

    def __init__(self, title="Untitled", date="No date"):
        Document._counter += 1
        self.__code = Document._counter
        self.__title = title
        self.__date = date

    def get_code(self):
        return self.__code

    def get_title(self):
        return self.__title

    def get_date(self):
        return self.__date

    def to_string(self):
        return f"Document code: {self.__code}, Title: '{self.__title}', Date: '{self.__date}'"

    def equals(self, other):
        return self.__code == other.get_code()


class Copy(Document):
    def __init__(self, title="Untitled", date="No date", number=0, purchase_date="Purchase date not specified"):
        super().__init__(title, date)
        self.__number = number
        self.__purchase_date = purchase_date

    def get_number(self):
        return self.__number

    def get_purchase_date(self):
        return self.__purchase_date

    def to_string(self):
        return f"Copy code: {self.get_code()}, Title: '{self.get_title()}', Date: '{self.get_date()}', Number: {self.__number}, Purchase Date: '{self.__purchase_date}'"

    def equals(self, other):
        return self.__number == other.get_number()
