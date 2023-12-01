```python
def optimize_vehicle_loading(warehouse, vehicle):
    # Get all the products in the warehouse
    products = [(product, quantity) for product, quantity in warehouse.inventory.values()]

    # Sort the products by their value-to-weight ratio in descending order
    products.sort(key=lambda x: x[0].value / x[0].weight, reverse=True)

    loaded_products = []
    for product, quantity in products:
        # Check if adding the product to the vehicle exceeds its weight capacity
        if vehicle.total_weight + product.weight * quantity <= vehicle.max_capacity:
            # Add the product to the vehicle's current load
            vehicle.add_product(product, quantity)
            loaded_products.append((product, quantity))
    
    return loaded_products
```

In this implementation, we first retrieve all the products in the warehouse and store them in a list of tuples `(product, quantity)`. The list is then sorted based on the value-to-weight ratio of each product in descending order.

We iterate through the sorted list and check if adding each product to the vehicle's current load exceeds its weight capacity. If not, we add the product to the vehicle and append it to the `loaded_products` list.

Finally, we return the `loaded_products` list, which contains tuples of the loaded products and their quantities.