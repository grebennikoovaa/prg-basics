class Phone():
    def __init__(self, brand, battery_percentage):
        self.brand = brand
        self.battery_percentage = battery_percentage
        self.it_on = False

    def power_on(self):
        if not self.is_on:
            self.is_on = True
            print(f"{self.brand} phone is now ON.")
        else:
            print(f"{self.brand} phone is already ON.")
    
    def power_off(self):
        if self.is_on:
            self.is_on = False
            print(f"{self.brand} phone is now OFF.")
        else:
            print(f"{self.brand} phone is already OFF.")

    def charge_battery(self, charge_amount):
        if self.battery_percentage < 100:
            self.battery_percentage += charge_amount
            if self.battery_percentage > 100:
                self.battery_percentage = 100
            print(f"{self.brand} phone charged to {self.battery_percentage}%.")
        else:
            print(f"{self.brand} phone is already fully charged.")
    
    def main():
        my_phone = Phone(brand="Apple", battery_percentage=20)

        print(f"Brand: {my_phone.brand}")
        print(f"Battery Percentage: {my_phone.battery_percentage}%")
        print(f"Is On: {my_phone.is_on}")

        my_phone.power_on()
        my_phone.charge_battery(50)
        my_phone.power_off()

    if __name__ == "__main__":
        main()    