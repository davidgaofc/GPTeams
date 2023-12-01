def optimize_vehicle_loading(warehouse, vehicle):
    # Sort products in the warehouse by decreasing value-to-weight ratio
    products = sorted(warehouse.inventory.values(), key=lambda x: x['product'].value / x['product'].weight, reverse=True)
    
    loaded_products = []
    remaining_capacity = vehicle.capacity
    
    # Iterate over the sorted products and add them to the vehicle if there is enough capacity
    for product in products:
        if product['quantity'] > 0 and product['product'].weight <= remaining_capacity:
            quantity_loaded = min(product['quantity'], remaining_capacity // product['product'].weight)
            loaded_products.append((product['product'], quantity_loaded))
            remaining_capacity -= quantity_loaded * product['product'].weight
            product['quantity'] -= quantity_loaded
    
    return loaded_products