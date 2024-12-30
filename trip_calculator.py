from typing import Dict, List
import itertools

'''

++Booking.com Interview Question asked for Senior SRE Role++

Guests may want to visit multiple cities during one trip. Hotels in these cities offer various prices
for the different days within the guest's trip.

Your goal: Find the cost of the trips that match the guest's budget.

Input:
1. The number of days the guestwould like to stay at in each city.
2. A budget(in EUR) the guest wants to spend at most for the entire trip.
3. A map containing the daily prices(in EUR) of the hotels in the cities the guest would like to visit during the trip.

For the sake of simplicity you can assume there is only one hotel per city in the input list, meaning all
hotels in the list must be visited by the guest.

output:
Sorted list(asc) of prices for the trips matching the guest's budget

Example input:

{
    "numberofDaysPerCity":2,
    "guestBudget":309,
    "hotels":{
    "Paris": [10,40,5,80,10,50],
    "London": [60,30,30,70,50,70],
    "Berlin": [20,80,20,50,80,100],
    }
}

Example output:
[220,240,250,305]


Author: Arun Singh, arunsingh.in@gmail.com
'''

class InvalidInputError(Exception):
    """Custom exception for invalid inputs."""
    pass

# --- Strategy Pattern: Define how we select consecutive days from a city. ---

class BaseDaySelectionStrategy:
    """
    Base class (interface) for day-selection strategies.
    We might want different strategies (e.g., best price, worst price, etc.).
    Here we keep it simple: pick any consecutive chunk of days.
    """
    def get_city_day_sums(self, daily_prices: List[int], days_to_stay: int) -> List[int]:
        """
        Should return a list of possible partial sums for the city, each sum
        representing picking consecutive 'days_to_stay' days from daily_prices.
        """
        raise NotImplementedError("Subclasses must implement get_city_day_sums.")


class AllConsecutiveDaysSelectionStrategy(BaseDaySelectionStrategy):
    """
    This strategy returns sums of ALL possible consecutive day segments
    of length `days_to_stay`.
    """
    def get_city_day_sums(self, daily_prices: List[int], days_to_stay: int) -> List[int]:
        if days_to_stay < 1 or days_to_stay > len(daily_prices):
            return []  # no valid selection
        sums = []
        # Precompute partial sums for performance
        # Example: prefix_sum[i] = sum of daily_prices[:i], prefix_sum[0] = 0
        prefix_sum = [0]
        for p in daily_prices:
            prefix_sum.append(prefix_sum[-1] + p)

        # Now compute sum of any consecutive days_to_stay
        for start in range(0, len(daily_prices) - days_to_stay + 1):
            end = start + days_to_stay
            city_sum = prefix_sum[end] - prefix_sum[start]
            sums.append(city_sum)
        return sums


# --- Main Calculator Class ---

class TripCostCalculator:
    """
    The main class responsible for calculating all possible trip costs
    given the user’s input.
    """
    def __init__(self, strategy: BaseDaySelectionStrategy = None):
        self.strategy = strategy or AllConsecutiveDaysSelectionStrategy()
    
    def calculate_trip_costs(
        self, 
        number_of_days_per_city: int, 
        guest_budget: int, 
        hotels: Dict[str, List[int]]
    ) -> List[int]:
        """
        Returns a sorted list of all possible trip costs <= guest_budget.
        Each city must be visited exactly once, picking 'number_of_days_per_city' 
        consecutive days from its daily prices.
        """

        # Basic input validation
        if number_of_days_per_city <= 0:
            raise InvalidInputError("number_of_days_per_city must be > 0.")
        if guest_budget < 0:
            raise InvalidInputError("guest_budget cannot be negative.")
        if not hotels:
            return []

        # 1) For each city, compute all possible sums of consecutive days
        city_partial_sums = []
        for city, prices in hotels.items():
            possible_sums = self.strategy.get_city_day_sums(prices, number_of_days_per_city)
            if not possible_sums:
                # If no possible consecutive chunk is found for any city, 
                # no valid trip can be made
                return []
            city_partial_sums.append(possible_sums)

        # 2) Build Cartesian product of all possible city sums
        #    Example: if city A has [sum1, sum2], city B has [sum3, sum4],
        #             possible total trips = sum1+sum3, sum1+sum4, sum2+sum3, sum2+sum4
        all_combinations = itertools.product(*city_partial_sums)

        # 3) Filter costs by budget
        valid_costs = []
        for combo in all_combinations:
            total_cost = sum(combo)
            if total_cost <= guest_budget:
                valid_costs.append(total_cost)

        # 4) Return sorted list of valid costs
        valid_costs.sort()
        return valid_costs


# --- The function as requested (entry point) ---

def tripCost(input_data: Dict) -> List[int]:
    """
    Conforms to the example input structure:

    input_data = {
      "numberofDaysPerCity": int,
      "guestBudget": int,
      "hotels": {
        "Paris": [10,40,5,80,10,50],
        "London": [60,30,30,70,50,70],
        "Berlin": [20,80,20,50,80,100],
      }
    }

    Output: sorted list of costs
    """
    number_of_days = input_data.get("numberofDaysPerCity", 0)
    budget = input_data.get("guestBudget", 0)
    hotels = input_data.get("hotels", {})

    calculator = TripCostCalculator()
    return calculator.calculate_trip_costs(
        number_of_days_per_city=number_of_days,
        guest_budget=budget,
        hotels=hotels
    )
