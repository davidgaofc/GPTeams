```python
import heapq

def find_shortest_route(map, start, end):
    # Create a dictionary to store the shortest distance from the start to each city
    distances = {city: float('inf') for city in map.cities}
    # Set the distance from the start city to itself as 0
    distances[start] = 0
    
    # Create a priority queue to store the cities and their distances
    pq = [(0, start)]
    
    # Create a dictionary to store the previous city in the shortest path
    previous = {}
    
    while pq:
        # Get the city with the smallest distance from the priority queue
        current_distance, current_city = heapq.heappop(pq)
        
        if current_distance > distances[current_city]:
            continue
        
        # Check if the current city is the destination city
        if current_city == end:
            # Reconstruct the shortest path
            path = []
            while current_city in previous:
                path.append(current_city)
                current_city = previous[current_city]
            path.append(start)
            # Reverse the path to get the correct order
            route = list(reversed(path))
            return route
        
        # Visit each neighboring city
        for road in map.get_roads_from_city(current_city):
            neighbor = road.to_city if road.from_city == current_city else road.from_city
            distance = distances[current_city] + road.length
            # Update if the new distance is smaller than the current distance
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous[neighbor] = current_city
                # Add the neighbor and its distance to the priority queue
                heapq.heappush(pq, (distance, neighbor))
    
    # If the destination city cannot be reached from the start city
    return None
```

This solution uses Dijkstra's algorithm to find the shortest route from the start city to the end city in the TransportationMap. It uses a priority queue to determine the next city to visit based on the smallest distance. The algorithm continues until either the end city is reached or all cities have been visited. If the end city is reached, the function reconstructs the shortest path by backtracking through the previous dictionary. The path is then reversed to get the correct order of cities from start to end. If the end city cannot be reached from the start city, the function returns None.