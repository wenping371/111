# filter_rules.py

# Filter logic for equipment categories and concrete materials

def filter_equipment_and_materials(items):
    exclusion_criteria = [
        "labor subcontracting",
        "ecological restoration",
        "sluice gates",
        "reservoirs",
        "highways",
        "asphalt"
    ]

    filtered_items = []
    for item in items:
        if not any(exclusion in item.lower() for exclusion in exclusion_criteria):
            filtered_items.append(item)

    return filtered_items

# Example usage
if __name__ == '__main__':
    items = ["Concrete Mix", "Labor Subcontracting Task", "Highways Construction", "Excavator", "Asphalt Paving", "Reservoir Pump"]
    print(filter_equipment_and_materials(items))