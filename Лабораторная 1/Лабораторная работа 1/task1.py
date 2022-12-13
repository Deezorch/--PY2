class WashingMachine:

    def __init__(self, capacity_volume: (float, int), occupied_volume=0, washing_powder=0):
        """
        Создание и подготовка к работе объекта "Стиральная машина".

        :param capacity_volume: объем стиральной машины.
        :param occupied_volume: объем вещей в стиральной машине (вещи добавляются после создания объекта).
        :param washing_powder: колличество порошка в стиральной машинке в граммах (порошок добавляется после создания
        объекта).

        :raise TypeError: если значение объема не действительное/целочисленное, то вызываем ошибку
               ValueError: Если объем стиральной машинки отрицательный, то вызываем ошибку

        Примеры:
        >>> washing_machine = WashingMachine(200) #инициализация экземпляра класса
        """
        if not isinstance(capacity_volume, (int, float)):
            raise TypeError("объем стиральной машины долен быть целочисленным/действительным")
        if capacity_volume < 0:
            raise ValueError("Объем стиральной машины должен быть неотрицательным")
        self.capacity_vilume = capacity_volume
        self.occupied_volume = occupied_volume
        self.washing_powder = washing_powder

    def loading(self, new_things) -> None:
        """
        Функция добавляющая вещи в стиральную машинку.

        :param new_things: новые вещи

        :raise TypeError: если значение объема не действительное/целочисленное, то вызываем ошибку
               ValueError: если объем вещей в стиральной машинке больше ее собсвтенного объема, то вызываем ошибку

        Примеры:
        >>> washing_machine = WashingMachine(200)
        >>> washing_machine.loading(50)
        """
        if not isinstance(new_things, (int, float)):
            raise TypeError("Объем новых вещей должен быть целочисленным/действительным")
        if self.occupied_volume + new_things > self.capacity_vilume:
            raise ValueError("Суммарный объем вещей в машинке не должен превышать ее собственный")
        self.occupied_volume += new_things

    def add_washing_powder(self, washing_powder) -> None:
        """
        Функция, добавляющая порошок в стиральную машинку

        :param washing_powder: колличество стирального порошка

        :raise TypeError: если колличество порошка не действительное/целочисленное, то вызываем ошибку
               ValueError: если колличество порошка больше 100, то вызываем ошибку

        Примеры:
        >>> washing_machine = WashingMachine(200)
        >>> washing_machine.add_washing_powder(50)
        """
        if not isinstance(washing_powder, (int, float)):
            raise TypeError("Колличество порошка должно быть целочисленным/действительным")
        if self.washing_powder + washing_powder > 100:
            raise ValueError("Колличество порошка превышает допустимое")
        self.washing_powder += washing_powder


class DynamicBed:

    def __init__(self, height=0.1, width=0.1, length=0.1):
        """
        Создание и подготовка к работе объекта "Динамическая Кровать"

        :param height: высота кровати (по-умолчанию 0.1 метр)
        :param width: ширна кровати (по-умолчанию 0.1 метр)
        :param length: длина кровати (по-умолчанию 0.1 метр)

        Примеры:
        >>> dynamic_bed = DynamicBed()  #инициализация экземпляра класса
        """
        if not isinstance(height, (int, float)):
            raise TypeError("Высота может принимать только целые/действительные значения")
        if height < 0.1:
            raise TypeError("Минимальная высота - 0.1 метр")
        self.height = height

        if not isinstance(width, (int, float)):
            raise TypeError("Ширина может принимать только целые/действительные значения")
        if width < 0.1:
            raise TypeError("Минимальная ширина - 0.1 метр")
        self.width = width

        if not isinstance(length, (int, float)):
            raise TypeError("Длина может принимать только целые/действительные значения")
        if length < 0.1:
            raise TypeError("Минимальная Длина - 0.1 метр")
        self.length = length

    def chenge_options(self, added_height: (int, float), added_width: (int, float), added_length: (int, float)) -> None:
        """
        Функция изменяет параметры динамической кровати

        :param added_height: приращение высоты
        :param added_width: приращение ширины
        :param added_length: приращение длины

        :raise TypeError: если приращение высоты/ширины/длины не целочисленное/действительное, то вызываем ошибку
               ValueError: если высота/ширина/длина кровати после приращения превышает 1.5 метра, то вызываем ошибку

        Пример:
        >>> bed = DynamicBed()
        >>> bed.chenge_options(0.3, 0.1, 0.6)
        """
        if not isinstance(added_height, (int, float)) or not isinstance(added_width, (int, float)) or not isinstance(
                added_length, (int, float)):
            raise TypeError("Значения приращений должны быть целочисленными/действительными")
        if self.height + added_height > 1.5 or self.width + added_width > 1.5 or self.length + added_length > 1.5:
            raise ValueError("Параметры кровати не могут превышать 1.5 метра")
        self.height += added_height
        self.width += added_width
        self.length += added_length

    def fold(self) -> None:
        """
        Функция складывает кровать в кубик 0.1/0.1/0.1

        Пример:
        >>> bed = DynamicBed(0.3, 0.6, 0.3)
        >>> bed.fold()
        """
        self.height, self.width, self.length = 0.1, 0.1, 0.1


class PillPackaging:

    def __init__(self, pills: (int, float), capacity: (int, float)):
        """
        Создание и подготовка к работе объекта "Упаковка таблеток"

        :param pills: колличество таблеток
        :param capacity: колличество таблеток которые могут поместиться в упаковке

        Примеры:
        >>> pill_packaging = PillPackaging(10, 100)
        """
        if not isinstance(pills, int) or not isinstance(capacity, int):
            raise TypeError("Колличество таблеток должно быть целочисленным")
        if pills < 0 or capacity < 0:
            raise ValueError("Колличество таблеток не может быть отрицательным")
        if capacity < pills:
            raise ValueError("Колличество таблеток не должно превышать вместимость")

        self.pills = pills
        self.capacity = capacity

    def add_pills(self, amount: int) -> None:
        """
        Функци добавляет или вынимает таблетки из упаковки

        :param amount: колличество добавленных таблеток

        :raise TypeError: если колличество добавленных таблеток не целочесленное, то выводим ошибку
               ValueError: если таблеток в пачке окажется больше чем это возможно, то выводим ошибку

        Примеры:
        >>> pills = PillPackaging(10, 20)
        >>> pills.add_pills(2)
        """
        if not isinstance(amount, int):
            raise TypeError("Колличество добавленных таблеток должно быть целочисленным")
        if self.capacity < self.pills + amount:
            raise ValueError("Колличество таблеток не должно превышать вместимость")
        self.pills += amount

    def pour_out(self) -> None:
        """
        Функция, очищающая упаковку от таблеток

        Пример:
        >>> pills = PillPackaging(10, 20)
        >>> pills.pour_out()
        """
        self.pills = 0

help(PillPackaging)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    pass
