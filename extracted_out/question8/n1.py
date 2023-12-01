from collections import defaultdict, deque
import math

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
        self.roads[road.from_city].append(road)
        self.roads[road.to_city].append(road)  # Assuming roads are bidirectional

    def get_roads_from_city(self, city):
        return self.roads[city]

def create_city(name):
    return City(name)

def create_road(from_city, to_city, length):
    return Road(from_city, to_city, length)

def add_city_to_map(transport_map, city):
    transport_map.add_city(city)

def add_road_to_map(transport_map, road):
    transport_map.add_road(road)

import heapq
# TODO: Implement 'find_shortest_route'
def find_shortest_route(map, start, end):
    # This function should take a TransportationMap object, start city, and end city, and find the shortest route by road length.
    # Implement a pathfinding algorithm like Dijkstra's algorithm or A* to find the shortest path.
    # Expected Input: map (TransportationMap object), start (City object), end (City object)
    # Expected Output: route (list of City objects, representing the shortest route from start to end)
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