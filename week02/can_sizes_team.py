import math

def main():

    items = [
        {"name": "#1 Picnic", "radius": 6.83, "height": 10.16, "cost_per_can": 0.28},
        {"name": "#1 Tall", "radius": 7.78, "height": 11.91, "cost_per_can": 0.43},
        {"name": "#2", "radius": 8.73, "height": 11.59, "cost_per_can": 0.45},
        {"name": "#2.5", "radius": 10.32, "height": 11.91, "cost_per_can": 0.61},
        {"name": "#3 Cylinder", "radius": 10.79, "height": 17.78, "cost_per_can": 0.86},
        {"name": "#5", "radius": 13.02, "height": 14.29, "cost_per_can": 0.83},
        {"name": "#6Z", "radius": 5.40, "height": 8.89, "cost_per_can": 0.22},
        {"name": "#8Z short", "radius": 6.83, "height": 7.62, "cost_per_can": 0.26},
        {"name": "#10", "radius": 15.72, "height": 17.78, "cost_per_can": 1.53},
        {"name": "#211", "radius": 6.83, "height": 12.38, "cost_per_can": 0.34},
        {"name": "#300", "radius": 7.62, "height": 11.27, "cost_per_can": 0.38},
        {"name": "#303", "radius": 8.10, "height": 11.11, "cost_per_can": 0.42}
    ]

    storage_efficiency_greatest = 0

    for item in items:
        radius = item["radius"]
        height = item["height"]
        cost = item["cost_per_can"]
        name = item["name"]

        volume = compute_volume(radius, height)

        surface_area = compute_surface_area(radius, height)

        storage_efficieny = compute_storage_efficiency(volume, surface_area)

        if storage_efficieny < 100:
            storage_efficiency_greatest = storage_efficieny
            name = item["name"]
        print(f"{name}")
        print(f"{volume}")
        
    print(f"{name} {storage_efficiency_greatest:.2f}")
    
    pass

def compute_volume(radius, height):
   
    volume = math.pi * (radius**2) * height   
   
    return volume

def compute_surface_area(radius, height):

    surface_area = 2 * math.pi * radius * (radius + height)

    return surface_area

def compute_storage_efficiency(volume, surface_area):

    storage_efficiency = volume / surface_area

    return storage_efficiency




