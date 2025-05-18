from car import Car

class Truck(Car):
    def __init__(self, model_name, mileage, manufacturer, max_loadings):
        super().__init__(model_name, mileage, manufacturer)
        self._max_loadings = max_loadings
        self._loadings = 0
    
    def gas(self):
        if self._loadings > self._max_loadings:
            print("No Drive")
            print(f"Please {self._max_loadings - self._loadings} unload")
        else:
            super().gas()
    
    def load(self, weight):
        if weight > 0:
            print(f"We loaded {weight} tons of cargo")
            self._loadings += weight
        else:
            if self._loadings <= -weight:
                print(f"We unloaded all {self._loadings} tons of the cargo")
                self._loadings = 0
            else:
                print(f"We unloaded {weight} tons of the cargo")
                self._loadings += weight
        print(f"{self._loadings} tons now!")

        if self._loadings > self._max_loadings:
            print("Over the loading limit")

if __name__ == "__main__":
    isuzu_truck = Truck("TruckA", 6, "Izusu", 10)
    isuzu_truck.gas()
    isuzu_truck.load(5)
    isuzu_truck.load(-3)
    isuzu_truck.load(-1)
    isuzu_truck.load(13)
    isuzu_truck.gas()
    isuzu_truck.load(-30)