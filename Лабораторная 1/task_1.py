import doctest

class Table:
    def __init__(self, legs_value: int, height_value: float):
        """
            Создание и подготовка к работе объекта "Стол"

            :param legs_value: Количество ножек
            :param height_value: Значение высоты

            Примеры:
            >>> table = Table(1, 80)  # инициализация экземпляра класса
        """
        if not isinstance(legs_value, int):
             raise TypeError("Количество ножек стола должно быть типа int")
        if legs_value <= 0:
             raise ValueError("Количество ножек стола должно быть положительным числом")
        self.legs_value = legs_value

        if not isinstance(height_value, (int, float)):
             raise TypeError("Значение высоты стола должно быть типа int или float")
        if height_value <= 0:
             raise ValueError("Значение высоты стола должно быть положительным числом")
        self.height_value = height_value

    def is_baby_table(self) -> bool:
        """
            Функция которая проверяет является ли стол детским

            :return: Является ли стол детским

            Примеры:
            >>> table = Table(1, 80)
            >>> table.is_baby_table()
        """
        ...
    def add_height_to_table(self, height: float) -> None:
        """
            Добавление столу высоты.
            :param height: Добавляемая высота

            :raise ValueError: Если добавляемая высота отрицательна, то вызываем ошибку

            Примеры:
            >>> table = Table(1, 52)
            >>> table.add_height_to_table(10)
        """
        if not isinstance(height, (int, float)):
            raise TypeError("Добавляемая высота должна быть типа int или float")
        if height < 0:
            raise ValueError("Добавляемая высота должна положительным числом")
        ...

class Tree:
    def __init__(self, trunk_value: int, leaf_value: int):
        """
            Создание и подготовка к работе объекта "Дерево"

            :param trunk_value: Количество стволов дерева
            :param leaf_value: Количество листочков дерева

            Примеры:
            >>> tree = Tree(1, 2000)  # инициализация экземпляра класса
        """
        if not isinstance(trunk_value, int):
            raise TypeError("Количество стволов дерева должно быть типа int")
        if trunk_value <= 0:
            raise ValueError("Количество стволов дерева должно быть положительным числом")
        self.trunk_value = trunk_value

        if not isinstance(leaf_value, int):
            raise TypeError("Количество листочков дерева должно быть типа int")
        if leaf_value < 0:
            raise ValueError("Значение высоты стола должно не должно быть отрицательно")
        self.leaf_value = leaf_value

    def is_leaves_fallen(self) -> bool:
        """
            Функция которая проверяет опали ли листья дерева

            :return: Опали ли листья дерева

            Примеры:
            >>> tree = Tree(1, 2000)
            >>> tree.is_leaves_fallen()
        """
        ...

    def pluck_leaves(self, leaves: int) -> None:
        """
            Срываем листики с дерева.
            :param leaves: Количество срываемых листиков

            :raise ValueError: Если количество срываемых листиков отрицательно, то вызываем ошибку

            Примеры:
            >>> tree = Tree(1, 2000)
            >>> tree.pluck_leaves(10)
        """
        if not isinstance(leaves, int):
            raise TypeError("Количество срываемых листиков должно быть типа int")
        if leaves <= 0:
            raise ValueError("Количество срываемых листиков должно быть положительным числом")
        ...

class Chocolate:
    def __init__(self, slice_value: int, layer_value: int):
        """
            Создание и подготовка к работе объекта "Шоколад"

            :param capacity_volume: Количество долек шоколада
            :param occupied_volume: Количество слоев шоколада

            Примеры:
            >>> сhocolate = Chocolate(15, 3)  # инициализация экземпляра класса
        """
        if not isinstance(slice_value, int):
            raise TypeError("Количество долек шоколада должено быть типа int")
        if slice_value <= 0:
            raise ValueError("Количество долек шоколада должено быть положительным числом")
        self.slice_value = slice_value

        if not isinstance(layer_value, int):
            raise TypeError("Количество слоев шоколада должно быть int")
        if layer_value <= 0:
            raise ValueError("Количество слоев шоколада должено быть положительным числом")
        self.layer_value = layer_value

    def is_empty_chocolate(self) -> bool:
        """
            Функция которая проверяет является ли шоколадка пустой

            :return: Является ли шоколадка пустой

            Примеры:
            >>> сhocolate = Chocolate(15, 3)
            >>> сhocolate.is_empty_chocolate()
        """
        ...

    def eat_chocolate_slices(self, slices: int) -> None:
        """
            Съесть дольки шоколада

            :param slices: Количество съедаемых долек
            :raise ValueError: Если количество съедаемых долек отрицательно,
            то возвращается ошибка.

            :return: Количество съеденых долек

            Примеры:
            >>> сhocolate = Chocolate(15, 3)
            >>> сhocolate.eat_chocolate_slices(5)
        """

if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации