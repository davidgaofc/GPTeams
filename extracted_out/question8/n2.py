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
from queue import PriorityQueue
# TODO: Implement 'find_shortest_route'
def find_shortest_route(map, start, end):
    # This function should take a TransportationMap object, start city, and end city, and find the shortest route by road length.
    # Implement a pathfinding algorithm like Dijkstra's algorithm or A* to find the shortest path.
    # Expected Input: map (TransportationMap object), start (City object), end (City object)
    # Expected Output: route (list of City objects, representing the shortest route from start to end)
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