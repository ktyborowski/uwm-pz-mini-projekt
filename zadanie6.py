from datetime import datetime


class Car:
    AGE_DEPRECIATION_FACTOR = 0.15  # Per year value depreciation
    MILEAGE_DEPRECIATION_FACTOR = 0.00001  # Per 1km depreciation value

    def __init__(self, make, model, year, mileage, price) -> None:
        self.make = make
        self.model = model
        self.year = year
        self.mileage = mileage
        self.price = price

    def set_mileage(self, mileage):
        if mileage < 0.0:
            raise ValueError("Mileage can't be lower than 0.")

        if mileage < self.mileage:
            raise ValueError("New value can't be lower than the current mileage.")

        self.mileage = mileage

    def get_mileage(self):
        return self.mileage

    def set_price(self, price):
        if price < 0.0:
            raise ValueError("Price can't be lower than 0.")

        self.price = price

    def get_price(self):
        return self.price

    def drive(self, distance):
        if distance < 0.0:
            raise ValueError("Distance can't be lower than 0.")

        self.mileage += distance

    def calculate_depreciation(self):
        """Returns the total depreciation rate over age and mileage. To calculate current car value multiply result by purchase price."""
        today = datetime.now()

        age = today.year - self.year

        age_depreciation = (1 - self.AGE_DEPRECIATION_FACTOR) ** age
        mileage_depreciation = (1 - self.MILEAGE_DEPRECIATION_FACTOR) ** self.mileage

        return abs(age_depreciation - mileage_depreciation)

    def __str__(self) -> str:
        return f"{self.year} {self.make} {self.model} - {self.mileage} km - {self.price} USD"

    def __repr__(self):
        class_name = type(self).__name__
        return f"{class_name}(self.make={self.make!r}, model={self.model!r}, year={self.year!r}, mileage={self.mileage!r}, price={self.price!r})"


if __name__ == "__main__":
    car = Car(make="Ford", model="T", year=2010, mileage=200000.0, price=2500.0)

    print(str(car))
    print(car.__repr__())

    print(car.calculate_depreciation())
