```python
import heapq

def find_shortest_route(map, start, end):
    # Create a dictionary to store the shortest distances from the start city to all other cities
    distances = {city: float('inf') for city in map.cities}
    # Set the distance of the start city to 0
    distances[start] = 0
    
    # Create a priority queue (min heap) to store the cities to be visited, with the start city as the initial node
    queue = [(0, start)]
  
    # Create a dictionary to store the previous city in the shortest route
    previous = {}
  
    while queue:
        # Pop the city with the smallest distance from the priority queue
        current_distance, current_city = heapq.heappop(queue)
        
        # If the current city is the end city, we have found the shortest route, so break out of the loop
        if current_city == end:
            break
        
        # If the current distance is larger than the previously calculated shortest distance for this city, skip it
        if current_distance > distances[current_city]:
            continue
        
        # Iterate through the roads from the current city
        for road in map.get_roads_from_city(current_city):
            # Calculate the distance to the neighboring city
            neighbor_distance = current_distance + road.length
            
            # If the calculated distance is smaller than the previously stored distance for the neighboring city, update it
            if neighbor_distance < distances[road.to_city]:
                distances[road.to_city] = neighbor_distance
                # Update the previous city in the shortest route
                previous[road.to_city] = current_city
                # Push the neighboring city and its distance to the priority queue
                heapq.heappush(queue, (neighbor_distance, road.to_city))
    
    # If no route is found, return an empty list
    if not previous.get(end):
        return []
    
    # Reconstruct the shortest route from the previous dictionary
    route = [end]
    while route[-1] != start:
        route.append(previous[route[-1]])
  
    # Reverse the route to get it in the correct order
    route.reverse()
    return route
```
In this solution, I used Dijkstra's algorithm to find the shortest route between two cities. The algorithm works by iteratively selecting the city with the smallest distance from the start city, then updating the distances to its neighboring cities if a shorter route is found. I used a heap data structure to efficiently select the city with the smallest distance. The algorithm terminates when the end city is reached or if there are no more cities to visit. Finally, I reconstructed the shortest route by backtracking from the end city to the start city using the previous dictionary.