# booking.com-interview-problem


++Booking.com Interview Question asked for Senior SRE Role++

## Guests may want to visit multiple cities during one trip. Hotels in these cities offer various prices for the different days within the guest's trip.

## Your goal: Find the cost of the trips that match the guest's budget.

## Input:
1. The number of days the guestwould like to stay at in each city.
2. A budget(in EUR) the guest wants to spend at most for the entire trip.
3. A map containing the daily prices(in EUR) of the hotels in the cities the guest would like to visit during the trip.

## For the sake of simplicity you can assume there is only one hotel per city in the input list, meaning all hotels in the list must be visited by the guest.

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
