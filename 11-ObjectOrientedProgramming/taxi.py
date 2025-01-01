class TaxiRide:
    def __init__(self, rate_per_km):
        self.rate_per_km = rate_per_km # value in € (e.g. €2)
        self.distance = 0
        self.fare = 0

    def calculate_fare(self, distance):
        self.distance = distance
        self.fare = self.distance * self.rate_per_km

    def print_receipt(self):
        print(f"Distance traveled: {self.distance} km")
        print(f"Rate per km: €{self.rate_per_km}")
        print(f"Total fare: €{self.fare}")

def main():
    driver1 = TaxiRide(rate_per_km=5)
    driver2 = TaxiRide(rate_per_km=8)
    driver1.calculate_fare(distance=50)
    driver2.calculate_fare(distance=80)
    driver1.print_receipt()
    driver2.print_receipt()

if __name__ == "__main__":
    main()
