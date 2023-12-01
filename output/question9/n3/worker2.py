```python

def optimize_vehicle_loading(warehouse, vehicle):
    # Initialize variables
    loaded_products = []
    remaining_capacity = vehicle.max_capacity

    # Sort products in the warehouse by their value (in descending order)
    products_sorted_by_value = sorted(warehouse.current_load, key=lambda x: x[0].value, reverse=True)

    # Iterate through the sorted products
    for product, quantity in products_sorted_by_value:
        # Check if adding the product to the vehicle exceeds its weight capacity
        if product.weight * quantity <= remaining_capacity:
            # Add the product to the vehicle and update remaining capacity
            load_product_on_vehicle(vehicle, product, quantity)
            remaining_capacity -= product.weight * quantity

            # Add the product to the loaded products list
            loaded_products.append((product, quantity))

    # Return the loaded products
    return loaded_products

```