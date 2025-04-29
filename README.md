
# Dynamic Carbon Footprint Tracker 

## Description
The Dynamic Carbon Footprint Tracker is a Python program that calculates carbon emissions and savings for a vehicle trip based on various
factors such as distance, number of riders, fuel type, traffic conditions, idle time, and trip timing. The program also tracks
cumulative emissions and savings across multiple trips.
## Documentation

FEATURES
- Carbon Emissions Calculation: Computes the total emissions for a trip using base emission rates and adjustments.
- Emissions Savings: Calculates emissions saved due to carpooling.
- Cumulative Tracking: Keeps a record of total emissions and savings for all trips entered.
- Traffic and Nighttime Adjustments: Adjusts emissions based on traffic conditions and trip timing.

HOW IT WORKS?

Logic
1. Base Emissions:
- Every vehicle emits a base amount of CO2 per kilometer, determined by the fuel type.
- Example: Petrol emits 251 grams/km, diesel emits 15% more, and EVs have zero emissions.

2. Adjustments:
- Traffic Conditions: Moderate traffic increases emissions by 10%, while heavy traffic increases them by 20%.
- Idle Time: Vehicles emit additional CO2 while idling, calculated at 10 grams per minute.
- Nighttime Efficiency**: Trips between 8 PM and 6 AM are slightly more efficient, reducing emissions by 5%.

3. Carpooling Savings:
- Emissions are shared among riders, reducing per-person emissions and contributing to savings.

4. Cumulative Data:
- Tracks the total emissions and savings for all trips entered during the program run.



RUN THE PROGRAM

After running the program, the console at the bottom of PyCharm will prompt you to enter data for:
- Distance traveled (in kilometers).

- Number of riders (as an integer).

- Fuel type (choose from petrol, diesel, or ev).

- Traffic condition (choose from light, moderate, or heavy).

- Idle time (in minutes as an integer).

- Trip time (in HH:MM format, e.g., 23:15 for 11:15 PM).


After providing the inputs, the program will display:

- Total Emissions: The carbon emissions for the trip in grams.

- Emissions Saved: The emissions saved by having multiple riders in the vehicle.

- Cumulative Emissions Saved: The total emissions saved across all trips
   
Repeat for Multiple Trips (Optional)

You can rerun the program to input details for another trip.
The cumulative emissions data will continue to grow, tracking all trips calculated during the program’s session.


---------------------------------------------------------------------------------------------------------------------------------

## Example Input and Output
Welcome to the Dynamic Carbon Footprint Tracker!

Enter distance traveled (in km): 20

Enter number of riders: 2

Enter fuel type (petrol/diesel/ev): petrol

Enter traffic condition (light/moderate/heavy): moderate

Enter idle time (in minutes): 22

Enter trip time (HH:MM, 24-hour format): 18:20

Fuel Adjustment: 1.0, Traffic Adjustment: 1.1, Nighttime Adjustment: 1.0

Base Emissions: 5522.0

Shared Emissions: 2761.0

Idle Emissions: 220

Total Emissions: 2981.0

Emissions Saved: 2541.0

Trip Results:

Total Emissions: 2981.0 grams

Emissions Saved: 2541.0 grams

Cumulative Emissions Saved: 2541.0 grams




