"""
Set 5 (Vehicle Rental System)
A rental service rents different vehicles.
Scenario:
Base class Vehicle with method calculate_rent()

Subclasses: Car, Bike

Requirements:
Car rent = base + per-day + insurance

Bike rent = base + per-day

Calculate total rent for mixed vehicle bookings using polymorphism
"""
from abc import ABC, abstractmethod
class Vehicle(ABC):
    
    def __init__(self,vehicle_id, model):
        self.vehicle_id = vehicle_id
        self.model = model

    @abstractmethod
    def calculate_rent(self,base, per_day_rent):
        pass

class Car(Vehicle):
    def __init__(self, vehicle_id, model, insurance):
        super().__init__(vehicle_id, model)
        self.insurance = insurance
    
    def calculate_rent(self, base, per_day_rent):
        return (base + per_day_rent + self.insurance)
        
class Bike(Vehicle):
    def __init__(self, vehicle_id, model):
        super().__init__(vehicle_id, model)
    
    def calculate_rent(self, base, per_day_rent):
        return (base + per_day_rent)
