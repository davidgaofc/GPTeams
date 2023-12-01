```python
def optimize_vehicle_loading(warehouse, vehicle):
    # Get a list of all products in the warehouse
    products = list(warehouse.inventory.values())

    # Sort the products in descending order of their value-to-weight ratio
    products.sort(key=lambda x: x['product'].value / x['product'].weight, reverse=True)

    # Initialize variables
    loaded_products = []
    remaining_capacity = vehicle.max_capacity

    # Iterate through the sorted products
    for product in products:
        # Check if the product can be added to the vehicle's load
        if vehicle.total_weight + product['product'].weight * product['quantity'] <= vehicle.max_capacity:
            # Add the product to the vehicle's load
            loaded_products.append((product['product'], product['quantity']))
            vehicle.current_load.append((product['product'], product['quantity']))
            vehicle.total_weight += product['product'].weight * product['quantity']
            remaining_capacity -= product['product'].weight * product['quantity']

            # Check if the vehicle is fully loaded
            if remaining_capacity == 0:
                break

    return loaded_products
```

This implementation of `optimize_vehicle_loading` uses a greedy approach to maximize the total value of the loaded products without exceeding the vehicle's weight capacity. It sorts the products in descending order of their value-to-weight ratio and iterates through them, adding each product to the vehicle's load if it can be accommodated within the remaining capacity. The function returns a list of tuples, where each tuple contains a `Product` object and the quantity loaded on the vehicle.