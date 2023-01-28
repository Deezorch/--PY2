class Book:
    """ Базовый класс книги. """

    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"

    @property
    def name(self) -> str:
        return self._name

    @property
    def author(self) -> str:
        return self._author


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self._pages = pages

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, pages={self.pages})"

    @property
    def pages(self) -> int:
        """Возвращает колличество страниц"""
        return self._pages

    @pages.setter
    def pages(self, val):
        if not isinstance(val, int):
            raise TypeError("Колличество страниц должно быть типа int")
        if val <= 0:
            raise ValueError("Колличество страниц не может быть отрицательным или нулевым")
        self._pages = val


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self._duration = duration

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, duration={self.duration})"

    @property
    def duration(self) -> float:
        """Возвращает продолжительность аудиокниги"""
        return self._duration

    @duration.setter
    def duration(self, val):
        if not isinstance(val, float):
            raise TypeError("продолжительность книги должна быть типа float")
        if val <= 0:
            raise ValueError("Продолжительность аудиокниги не может быть отрицательной или нулевой")
        self._duration = val
