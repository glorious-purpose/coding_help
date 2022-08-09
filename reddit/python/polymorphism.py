"""
Provide an example of polymorphism.

Original question:
https://www.reddit.com/r/pythonhelp/comments/vlpasm/how_to_do_this_example_with_polymorphism/
"""

class Vehicle():
    TotalFare = {}

    def fare(self, amt: int) -> int:
        return amt


class Bus(Vehicle):
    def __init__(self):
        if "Bus" not in self.TotalFare:
            self.TotalFare["Bus"] = 0

    def fare(self, amt: int) -> int:
        self.TotalFare["Bus"] += amt
        return amt


class Car(Vehicle):
    def __init__(self):
        if "Car" not in self.TotalFare:
            self.TotalFare["Car"] = 0

    def fare(self, amt: int) -> int:
        self.TotalFare["Car"] += amt
        return amt


class Train(Vehicle):
    def __init__(self):
        if "Train" not in self.TotalFare:
            self.TotalFare["Train"] = 0

    def fare(self, amt: int) -> int:
        self.TotalFare["Train"] += amt
        return amt


class Truck(Vehicle):
    def __init__(self):
        if "Truck" not in self.TotalFare:
            self.TotalFare["Truck"] = 0

    def fare(self, amt: int) -> int:
        self.TotalFare["Truck"] += amt
        return amt


class Ship(Vehicle):
    def __init__(self):
        if "Ship" not in self.TotalFare:
            self.TotalFare["Ship"] = 0

    def fare(self, amt: int) -> int:
        self.TotalFare["Ship"] += amt
        return amt

veh = Vehicle()
bus = Bus()
car = Car()
train = Train()
truck = Truck()
ship = Ship()

print(f"Today, took a Lyft to help a friend move. It cost ${car.fare(40)}, mostly because I had to ride a ferry.")
print(f" That added another ${ship.fare(20)}, but was the quickest route during rush hour.")
print(f"When I arrived, I realized my friend hadn't rented a truck. I took the Lyft to the local rental shop.")
print(f"The truck ran me ${truck.fare(200)} for the day. Paul will pay me back later. After we loaded, we opted to take the toll tunnel, which added another ${truck.fare(5)}.")
print(f"Several tolls later ${truck.fare(20)}, we arrived at the new location and unloaded.")
print(f"We dropped the truck off at the rental location near his new house. Walking out the door, Paul realized he forgot his lucky jacket on the counter of the old place.")
print(f"We hop on the bus (${bus.fare(4)}) and rode to the local train station and caught a ride back to his old neighborhood. ${train.fare(20)} later, and we're calling for another Lyft.")
print(f"I start complaining to Paul about the money and time we're spending for this jacket as I approve another ${car.fare(15)} for the car ride.")
print(f"Paul grabs his jacket and does one last check. The Lyft driver decided to wait for the return trip. Another ${car.fare(15)}, plus an extra ${car.fare(20)} tip for waiting.")
print(f"Another ${train.fare(15)} train ride and a claustrophobic ${bus.fare(4)} bus trip back to his neighborhood.")
print("We have some delivered sushi and declare victory on the day, then I start looking for a ride home.")
print("I briefly consider just buying a car as I wait for my new Lyft driver to arrive.")
print(f"${car.fare(80)} later, and I'm safely in bed.")
print(f"I decide to run through my expenses for the day:")
total = 0
for key, cost in veh.TotalFare.items():
    print(f"{key}: ${cost}")
    total += cost
print(f"\nTotal: ${total}")
