import pytest

from trip_calculator import (
    TripCostCalculator,
    AllConsecutiveDaysSelectionStrategy,
    InvalidInputError,
    tripCost
)

def test_basic_trip_cost():
    # ARRANGE
    input_data = {
        "numberofDaysPerCity": 2,
        "guestBudget": 309,
        "hotels": {
            "Paris": [10, 40, 5, 80, 10, 50],
            "London": [60, 30, 30, 70, 50, 70],
            "Berlin": [20, 80, 20, 50, 80, 100],
        }
    }

    # ACT
    results = tripCost(input_data)

    # ASSERT
    # According to the example, the output is [220,240,250,305]
    assert results == [220, 240, 250, 305]


def test_zero_days_raises_error():
    calculator = TripCostCalculator()
    with pytest.raises(InvalidInputError):
        calculator.calculate_trip_costs(0, 200, {"City": [10, 20]})


def test_negative_budget_raises_error():
    calculator = TripCostCalculator()
    with pytest.raises(InvalidInputError):
        calculator.calculate_trip_costs(2, -100, {"City": [10, 20]})


def test_no_hotels_returns_empty():
    calculator = TripCostCalculator()
    # If no hotels, there's no trip
    result = calculator.calculate_trip_costs(2, 100, {})
    assert result == []


def test_bdd_scenario():
    """
    Scenario: A guest wants to find all possible trip costs within their budget
      Given the guest wants 2 consecutive days in each city
      And the guest's budget is 309
      And the hotels are {Paris, London, Berlin} with daily prices
      When the guest invokes tripCost
      Then the result must be [220, 240, 250, 305]
    """
    input_data = {
        "numberofDaysPerCity": 2,
        "guestBudget": 309,
        "hotels": {
            "Paris": [10, 40, 5, 80, 10, 50],
            "London": [60, 30, 30, 70, 50, 70],
            "Berlin": [20, 80, 20, 50, 80, 100],
        }
    }
    results = tripCost(input_data)
    assert results == [220, 240, 250, 305]
