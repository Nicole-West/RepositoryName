class Car:
    """Базовый класс автомобилей."""
    def __init__(self, brand: str, model: str, year: int):
        """Автомобиль с маркой, моделью и годом выпуска."""
        self.brand = brand
        self.model = model
        self.year = year

    def __str__(self) -> str:
        """Возвращает строковое представление автомобиля."""
        return f"Автомобиль {self.brand} {self.model}"

    def __repr__(self) -> str:
        """Возвращает строковое представление автомобиля."""
        return f"{self.__class__.__name__}(brand={self.brand!r}, model={self.model!r},year={self.year})"

    def drivingStart(self):
        """Возвращает сигнал начала движения"""
        return "Start to move"

    def iscangostright(self) -> bool:
        """Возвращает True, если объект может двигаться прямо"""
        return True

class PassengerCar(Car):
    """Дочерний класс - Легковой автомобиль"""
    def __init__(self, brand: str, model: str, year: int, num_passengers: int):
        """Легковой автомобиль с маркой, моделью, годом выпуска и количеством пассажиров."""
        super().__init__(brand, model, year)
        self.num_passengers = num_passengers

    def __str__(self) -> str:
        """Возвращает строковое представление легкового автомобиля."""
        return f"Легковой автомобиль {self.brand} {self.model} c колличеством пассажиров: {self.num_passengers}"

    def __repr__(self) -> str:
        """Возвращает строковое представление легкового автомобиля."""
        return f"{self.__class__.__name__}(brand={self.brand!r}, model={self.model!r}, year={self.year}, num_passengers={self.num_passengers})"

    def drivingStart(self):
        """Возвращает сигнал начала движения"""
        return "R-r-r"

if __name__ == "__main__":
    pig = PassengerCar(brand='Chevrolet', model='Camaro', year=1969, num_passengers=3)
    print(pig)
    print(repr(pig))
    print(pig.drivingStart())
    print(pig.iscangostright())
