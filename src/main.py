from vehicle import Vehicle, Car, Bike
class Main:
    @staticmethod
    def main():

         # Create Car and Bike objects
        car1 = Car(101, "Tesla", 5000)
        bike1 = Bike(102, "GT650")
        car2 = Car(103, "BMW", 7000)
        car3 = Car(105, "Xcross", 6000)
        bike2 = Bike(104, "Apache")

         # Store all vehicle objects in a single list
        vehicle = [car1, bike1, car2, car3, bike2]

        # Iterate through each vehicle
        for v in vehicle:

            # Check if the current vehicle is a Car
            if v.__class__.__name__ == "Car":
                per_day_rent = int(input("Enter per day rent for Car : "))
                rent = v.calculate_rent(1000, per_day_rent)
                print(f"{v.model} total rent {rent}")

            else:
                per_day_rent = int(input("Enter per day rent for Bike : "))
                rent = v.calculate_rent(500, per_day_rent)
                print(f"{v.model} total rent {rent}")

if __name__ == "__main__":
    Main.main()