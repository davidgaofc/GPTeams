```python
def find_shortest_route(map, start, end):
    # Initialize the distances to all cities as infinite except for the starting city, which is set to 0
    distances = {city: float('inf') for city in map.cities}
    distances[start] = 0

    # Initialize the previous cities for each city as None
    previous = {city: None for city in map.cities}

    # Create a set to keep track of visited cities
    visited = set()

    # Create a priority queue to store cities and their distances
    pq = PriorityQueue()
    pq.put((0, start))

    while not pq.empty():
        # Get the city with the minimum distance from the priority queue
        current_distance, current_city = pq.get()

        # If the current city has been visited before, skip it
        if current_city in visited:
            continue

        # Mark the current city as visited
        visited.add(current_city)

        # For each road from the current city
        for road in map.get_roads_from_city(current_city):
            # Calculate the new distance to the neighboring city
            neighbor_city = road.from_city if road.to_city == current_city else road.to_city
            distance_to_neighbor = current_distance + road.length

            # If the new distance is shorter than the current distance to the neighboring city, update the distances and previous cities
            if distance_to_neighbor < distances[neighbor_city]:
                distances[neighbor_city] = distance_to_neighbor
                previous[neighbor_city] = current_city

                # Put the neighbor city and its distance into the priority queue
                pq.put((distance_to_neighbor, neighbor_city))

    # Reconstruct the shortest route from start to end using the previous cities
    route = []
    current_city = end

    while current_city is not None:
        route.append(current_city)
        current_city = previous[current_city]

    # Reverse the route to get it from start to end
    route.reverse()

    return route
```
