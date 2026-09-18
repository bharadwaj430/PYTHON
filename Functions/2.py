# Smart Parking Lot Tracker 🚗

parking_slots = ["Car", None, "Bike", None, "Car", "Bike", None]

print("Current Parking Status:")
print(parking_slots)

# 1. Access an array element using index
print("\nVehicle at slot 1:", parking_slots[0])

# 2. Find all empty parking slots
empty_slots = []

for i in range(len(parking_slots)):
    if parking_slots[i] is None:
        empty_slots.append(i + 1)

print("Available slots:", empty_slots)

# 3. Park a new vehicle in the first available slot
new_vehicle = "Car"

for i in range(len(parking_slots)):
    if parking_slots[i] is None:
        parking_slots[i] = new_vehicle
        print(f"{new_vehicle} parked at slot {i + 1}")
        break

# 4. Count different vehicles
car_count = parking_slots.count("Car")
bike_count = parking_slots.count("Bike")

print("\nTotal Cars:", car_count)
print("Total Bikes:", bike_count)

# 5. Search for a particular vehicle
vehicle = "Bike"

if vehicle in parking_slots:
    print(f"{vehicle} is present in the parking lot.")
else:
    print(f"{vehicle} is not present.")

# 6. Final parking status
print("\nFinal Parking Status:")
for slot in range(len(parking_slots)):
    print(f"Slot {slot + 1}: {parking_slots[slot]}")