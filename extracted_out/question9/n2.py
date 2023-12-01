import random
from heapq import heappush, heappop

class Product:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

class Warehouse:
    def __init__(self):
        self.inventory = {}

    def add_product(self, product, quantity):
        if product.name in self.inventory:
            self.inventory[product.name]['quantity'] += quantity
        else:
            self.inventory[product.name] = {'product': product, 'quantity': quantity}

    def get_product_quantity(self, product_name):
        return self.inventory.get(product_name, {'quantity': 0})['quantity']

class DeliveryVehicle:
    def __init__(self, max_capacity):
        self.max_capacity = max_capacity
        self.current_load = []
        self.total_weight = 0

    def add_product(self, product, quantity):
        if self.total_weight + product.weight * quantity <= self.max_capacity:
            self.current_load.append((product, quantity))
            self.total_weight += product.weight * quantity
            return True
        return False

def create_product(name, weight):
    return Product(name, weight)

def add_product_to_warehouse(warehouse, product, quantity):
    warehouse.add_product(product, quantity)

def create_delivery_vehicle(max_capacity):
    return DeliveryVehicle(max_capacity)

def load_product_on_vehicle(vehicle, product, quantity):
    return vehicle.add_product(product, quantity)

# TODO: Implement 'optimize_vehicle_loading'
def optimize_vehicle_loading(warehouse, vehicle):
    # This function should take a Warehouse object and a DeliveryVehicle object and load the vehicle with products from the warehouse.
    # The goal is to maximize the total value of the loaded products without exceeding the vehicle's weight capacity.
    # This is a variant of the knapsack problem, and can be solved using dynamic programming or a greedy approach.
    # Expected Input: warehouse (Warehouse object), vehicle (DeliveryVehicle object)
    # Expected Output: loaded_products (list of tuples, each tuple contains a Product object and quantity loaded on the vehicle)
    products = warehouse.inventory.keys()

    # Sort the products by their value-to-weight ratio in descending order
    sorted_products = sorted(products, key=lambda p: p.value / p.weight, reverse=True)

    loaded_products = []

    # Iterate through the sorted products and try to add them to the vehicle
    for product in sorted_products:
        quantity = warehouse.get_product_quantity(product)

        # Check if adding the product to the vehicle exceeds its weight capacity
        if vehicle.total_weight + product.weight * quantity <= vehicle.max_capacity:
            # Add the product to the vehicle's current load
            vehicle.add_product(product, quantity)
            loaded_products.append((product, quantity))

    return loaded_products