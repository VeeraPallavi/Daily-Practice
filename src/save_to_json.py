import csv
import json

def save_to_json(csv_file, json_file):
    vehicles = []

    with open(csv_file, mode="r", newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            row["Battery Percentage"] = int(row["Battery Percentage"])
            row["Rental Price"] = int(row["Rental Price"])
            vehicles.append(row)
        
        battery = {}

        for start in range(0, 100, 10):
            end = start + 10
            key = f"{start}-{end}"
            battery[key] = []
        
        for vehicle in vehicles:
            battery_percentage = vehicle["Battery Percentage"]

            for start in range(0, 100, 10):
                end = start + 10

                if start <= battery_percentage < end:
                    battery[f"{start}-{end}"].append(vehicle)

    with open(json_file, "w") as file:
        json.dump(battery, file, indent =4)


save_to_json("data.csv", "data.json")