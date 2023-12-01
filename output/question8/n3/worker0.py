```python
import heapq
from collections import defaultdict

class City:
    def __init__(self, name):
        self.name = name

class Road:
    def __init__(self, from_city, to_city, length):
        self.from_city = from_city
        self.to_city = to_city
        self.length = length

class TransportationMap:
    def __init__(self):
        self.cities = set()
        self.roads = defaultdict(list)

    def add_city(self, city):
        self.cities.add(city)

    def add_road(self, road):
        self.roads[road.from_city].append((road.to_city, road.length))
        self.roads[road.to_city].append((road.from_city, road.length))

# Implement 'find_shortest_route'
def find_shortest_route(map, start, end):
    # This function should take a TransportationMap object, start city, and end city, and find the shortest route by road length.
    # Implement a pathfinding algorithm like Dijkstra's algorithm or A* to find the shortest path.
    # Expected Input: map (TransportationMap object), start (City object), end (City object)
    # Expected Output: route (list of City objects, representing the shortest route from start to end)
    distances = {city: float('inf') for city in map.cities}
    distances[start] = 0
    previous = {city: None for city in map.cities}
    queue = [(0, start)]

    while queue:
        current_distance, current_city = heapq.heappop(queue)

        if current_city == end:
            route = []
            while current_city:
                route.append(current_city)
                current_city = previous[current_city]
            return route[::-1]

        if current_distance > distances[current_city]:
            continue

        for neighbor, road_length in map.roads[current_city]:
            distance = current_distance + road_length
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous[neighbor] = current_city
                heapq.heappush(queue, (distance, neighbor))

    return None
```