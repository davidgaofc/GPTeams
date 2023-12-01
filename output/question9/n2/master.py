def optimize_vehicle_loading(warehouse, vehicle):
    # Get a list of all products in the warehouse
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