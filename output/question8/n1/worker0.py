```python
import heapq

def find_shortest_route(map, start, end):
    # Create a dictionary to store the shortest distance from the start city to each city
    distances = {city: float('inf') for city in map.cities}
    distances[start] = 0

    # Create a dictionary to store the previous city in the shortest route from the start city to each city
    previous_cities = {city: None for city in map.cities}

    # Create a priority queue to store the cities to be visited
    # The priority is based on the shortest distance from the start city
    queue = [(0, start)]

    while queue:
        # Pop the city with the shortest distance from the queue
        current_distance, current_city = heapq.heappop(queue)

        # If we reach the end city, construct and return the shortest route
        if current_city == end:
            route = []
            while current_city:
                route.append(current_city)
                current_city = previous_cities[current_city]
            route.reverse()
            return route

        # Explore all the roads from the current city
        for road in map.get_roads_from_city(current_city):
            # Calculate the new distance from the start city to the neighboring city
            new_distance = distances[current_city] + road.length

            # If the new distance is shorter than the current distance to the neighboring city,
            # update the distance and previous city
            if new_distance < distances[road.to_city]:
                distances[road.to_city] = new_distance
                previous_cities[road.to_city] = current_city

                # Add the neighboring city to the queue with the updated distance
                heapq.heappush(queue, (new_distance, road.to_city))

    # If there is no route from the start city to the end city, return an empty route
    return []
```