
# Создайте класс и поля соответствующему вашему варианту (поля статические и динамические).
# Создайте три метода (класса, объекта и статический). Выберете поле или метод для реализации инкапсуляции.
# Пропишите запись и считывание (get, set) инкапсулированных полей

# Вариант №1 - Book

class Book:
    __id = 0  #указываем статичное поле с начальным значением в 0
    #прописываем инициализатор с полями класса - в данном случае мы указываем методы экземпляра класса
    def __init__(self, name, author, publisher, year, num_pages, price, binding):
        self.__id = Book.__id
        Book.__id += 1  #используем для увеличение счетчика при добавлении следующей книги
        self.name = name
        self.author = author
        self.publisher = publisher
        self.year = year
        self.num_pages = num_pages
        self.price = price
        self.binding = binding

    # прописываем метод самого класса
    @classmethod
    def get_count_id(cls):
        return cls.__id

    #прописываем статический метод
    @staticmethod
    def num_page_book(num_pages):
        if num_pages < 0:
            return "Ошибка внесенных данных"
        elif num_pages < 100:
            return "книга маленького объема"
        elif num_pages < 250:
            return "книга среднего объема"
        else:
            return "книга большого объема"

    def set_num_pages(self, num_pages):
        if num_pages < 0:
            print("Вы ввели неправильные данные")
        else:
            self.num_pages = num_pages

    #прописываем геттеры и сеттеры
    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_author(self):
        return self.author

    def set_author(self, author):
        self.author = author

    def get_publisher(self):
        return self.publisher

    def set_publisher(self, publisher):
        self.publisher = publisher

    def get_year(self):
        return self.year

    def set_year(self, year):
        if year < 0:
            print("Вы ввели неправильные данные")
        else:
            self.year = year

    def get_num_pages(self):
        return self.num_pages

    def set_num_pages(self, num_pages):
        if num_pages < 0:
            print("Вы ввели неправильные данные")
        else:
            self.num_pages = num_pages

    def get_price(self):
        return self.price

    def set_price(self, price):
        if price < 0:
            print("Вы ввели неправильные данные")
        else:
            self.price = price

    def get_binding(self):
        return self.binding

    def set_binding(self, binding):
        self.binding = binding

#указываем список книг
books = [
    Book("Запретная дверь", "Олег Синицын", "Аскона", 2013, 150, 32.15, "Плотный переплет"),
    Book("Нижний уровень", "Андрей Круз", "Питер", 2013, 212, 45.85, "Плотный переплет"),
    Book("Попытка возврата", "Владислав Конюшевский", "Эксмо", 2009, 130, 30.44, "Мягкий переплет"),
    Book("Метро 2033", "Дмитрий Глуховский", "АСТ", 2021, 384, 75.52, "Плотный переплет"),
    Book("Закон Черного сталкера", "Дмитрий Силлов", "АСТ", 2023, 288, 31.45, "Плотный переплет"),
    Book("Старатель", "Ерофей Трофимов", "Аскона", 2020, 254, 32.78, "Плотный переплет"),
    Book("Десантник на престоле", "Михаил Ланцов", "Питер", 2019, 290, 34.63, "Плотный переплет"),
    Book("Девятый", "Артем Каменистый", "Альпина Паблишер", 2014, 190, 25.74, "Мягкий переплет"),
    Book("Товарищ жандарм", "Станислав Сергеев", "АСТ", 2015, 205, 27.42, "Мягкий переплет"),
    Book("Механики", "Александр Март", "Питер", 2019, 245, 30.54, "Плотный переплет"),
    ]

#определяем функцию для вывода данных из списка
def show_catalog_books(books):
    print("Список интересных книг: ")
    for book in books:
        print(f"{book.get_name()}, {book.get_author()}, {book.get_publisher()}, {book.get_year()}, "
        f"{book.get_num_pages()}, {book.get_price()}, {book.get_binding()}")
show_catalog_books(books)

#данный цикл для вывода данных используя статический метод
for book in books:
    print(f"{book.name} - {Book.num_page_book(book.num_pages)}")

#вывод данных по методу класса
print("В нашем списке: ", Book.get_count_id(), " книг")
