from datetime import datetime

# Storing cumulative data for all trips
cumulative_data = {
    "total_emissions": 0,
    "total_savings": 0,
    "trips": []
}

def calculate_carbon_savings(distance, riders, fuel_type, traffic, idle_time, trip_time):
    """
    Calculate carbon emissions and savings for a given trip.

    Args:
        distance (float): Distance traveled in kilometers.
        riders (int): Number of riders in the vehicle.
        fuel_type (str): Type of fuel (e.g., petrol, diesel, ev).
        traffic (str): Traffic condition (e.g., light, moderate, heavy).
        idle_time (int): Idle time in minutes.
        trip_time (str): Trip time in HH:MM 24-hour format.

    Returns:
        dict: Emissions data containing total emissions and savings.
    """
    BASE_EMISSIONS = 251  # grams per km
    IDLE_EMISSIONS_PER_MIN = 10  # grams per minute

    # Traffic and fuel adjustment factors
    traffic_factors = {"light": 1.0, "moderate": 1.1, "heavy": 1.2}
    fuel_factors = {"petrol": 1.0, "diesel": 1.15, "ev": 0.0}

    # Adjusting for nighttime trips
    trip_hour = datetime.strptime(trip_time, "%H:%M").hour
    nighttime_adjustment = 0.95 if 20 <= trip_hour or trip_hour < 6 else 1.0

    # Applying adjustment factors
    fuel_factor = fuel_factors.get(fuel_type.lower(), 1.0)
    traffic_factor = traffic_factors.get(traffic.lower(), 1.0)

    # Debugging: Print factors
    print(f"Fuel Adjustment: {fuel_factor}, Traffic Adjustment: {traffic_factor}, Nighttime Adjustment: {nighttime_adjustment}")

    # Calculating emissions
    idle_emissions = idle_time * IDLE_EMISSIONS_PER_MIN
    base_emissions = distance * BASE_EMISSIONS * fuel_factor * traffic_factor * nighttime_adjustment
    shared_emissions = base_emissions / riders if riders > 1 else base_emissions

    total_emissions = shared_emissions + idle_emissions
    emissions_saved = base_emissions - total_emissions

    # Debugging: Print intermediate results
    print(f"Base Emissions: {base_emissions}")
    print(f"Shared Emissions: {shared_emissions}")
    print(f"Idle Emissions: {idle_emissions}")
    print(f"Total Emissions: {total_emissions}")
    print(f"Emissions Saved: {emissions_saved}")

    return {
        "total_emissions": round(total_emissions, 2),
        "emissions_saved": round(emissions_saved, 2)
    }

def main():
    print("Welcome to the Dynamic Carbon Footprint Tracker!")

    try:
        # Collecting trip details from the user
        distance = float(input("Enter distance traveled (in km): "))
        riders = int(input("Enter number of riders: "))
        fuel_type = input("Enter fuel type (petrol/diesel/ev): ").strip()
        traffic = input("Enter traffic condition (light/moderate/heavy): ").strip()
        idle_time = int(input("Enter idle time (in minutes): "))
        trip_time = input("Enter trip time (HH:MM, 24-hour format): ").strip()

        # Validating trip time format
        datetime.strptime(trip_time, "%H:%M")
    except ValueError:
        print("Invalid input. Please ensure all values are correct.")
        return

    # Calculating emissions and savings
    result = calculate_carbon_savings(distance, riders, fuel_type, traffic, idle_time, trip_time)

    # Updating cumulative data
    cumulative_data["total_emissions"] += result["total_emissions"]
    cumulative_data["total_savings"] += result["emissions_saved"]
    cumulative_data["trips"].append({
        "distance": distance,
        "riders": riders,
        "fuel_type": fuel_type,
        "traffic": traffic,
        "idle_time": idle_time,
        "trip_time": trip_time,
        "total_emissions": result["total_emissions"],
        "emissions_saved": result["emissions_saved"]
    })

    # Displaying results to the user
    print("\nTrip Results:")
    print(f"Total Emissions: {result['total_emissions']} grams")
    print(f"Emissions Saved: {result['emissions_saved']} grams")
    print(f"Cumulative Emissions Saved: {cumulative_data['total_savings']} grams")


if __name__ == "__main__":
    main()
