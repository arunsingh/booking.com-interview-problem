# main.py

# Import or paste the 'tripCost' function from your first version here.
# For example, if your code is in trip_calculator.py, you'd do:
# from trip_calculator import tripCost

def tripCost(input_data):
    """
    This is a placeholder for your 'tripCost' function 
    from the first version of the code, where no 
    helper function existed. Replace this body with the
    actual implementation.
    """
    # Example placeholder logic:
    number_of_days = input_data.get("numberofDaysPerCity", 0)
    budget = input_data.get("guestBudget", 0)
    hotels = input_data.get("hotels", {})

    # Just return a dummy list or implement your actual logic here
    return [220, 240, 250, 305]  # Placeholder

def main():
    # Sample input data (as in your example)
    input_data = {
        "numberofDaysPerCity": 2,
        "guestBudget": 309,
        "hotels": {
            "Paris": [10, 40, 5, 80, 10, 50],
            "London": [60, 30, 30, 70, 50, 70],
            "Berlin": [20, 80, 20, 50, 80, 100]
        }
    }

    # Call your tripCost function with the sample input
    results = tripCost(input_data)

    # Print the results
    print("Possible trip costs:", results)

if __name__ == "__main__":
    main()
