```python
import heapq

def find_shortest_route(map, start, end):
    # Initialize a dictionary to store the distances from the start city to each city
    distances = {city: float('inf') for city in map.cities}
    # Set the distance from the start city to the start city as 0
    distances[start] = 0
    
    # Initialize a dictionary to store the previous city in the shortest route
    previous_cities = {}
    
    # Create a priority queue to store cities to be visited
    # Each item in the priority queue is a tuple of the form (distance, city)
    # We use the distance as the priority to prioritize the cities with the smallest distance
    queue = [(0, start)]
    
    while queue:
        current_distance, current_city = heapq.heappop(queue)
        
        # If the current city is the end city, we have found the shortest route
        if current_city == end:
            # Backtrack from the end city to the start city to construct the shortest route
            route = []
            while current_city is not None:
                route.append(current_city)
                current_city = previous_cities.get(current_city)
            route.reverse()
            return route
        
        # If we have already processed the current city, skip it
        if current_distance > distances[current_city]:
            continue
        
        # Iterate through the roads from the current city
        for road in map.get_roads_from_city(current_city):
            next_city = road.to_city
            distance = current_distance + road.length
            
            # If the new distance is smaller than the current distance to the next city,
            # update the distance and previous city
            if distance < distances[next_city]:
                distances[next_city] = distance
                previous_cities[next_city] = current_city
                heapq.heappush(queue, (distance, next_city))
    
    # If there is no route from the start city to the end city, return an empty list
    return []
```
This implementation uses Dijkstra's algorithm to find the shortest route by road length from a start city to an end city in a transportation map object.