class FlightData:

    def __init__(self, price, origin_airport, destination_airport, out_date, return_date):
        """
        Constructor for initializing a new flight data instance with specific travel details.
        Parameters:
        - price: The cost of the flight.
        - origin_airport: The IATA code for the flight's origin airport.
        - destination_airport: The IATA code for the flight's destination airport.
        - out_date: The departure date for the flight.
        - return_date: The return date for the flight.
        """
        self.price = price
        self.origin_airport = origin_airport
        self.destination_airport = destination_airport
        self.out_date = out_date
        self.return_date = return_date

def find_cheapest_flight(flights):
    """
    Finds the cheapest flight from a list of flight offers.
    Parameters:
        flights (list): A list of flight offers returned by the Amadeus API.
    Returns:
        dict: The flight offer with the lowest price, or None if no flights are available.
    """
    if not flights:
        print("No flight data available.")
        return None

    # Find the flight with the lowest price
    cheapest_flight = min(flights, key=lambda flight: float(flight['price']['grandTotal']))
    return cheapest_flight