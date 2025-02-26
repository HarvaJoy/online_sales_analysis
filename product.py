
class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        
    def display_info(self):
        """Display the info about the product"""
        return f"Name: {self.name}, Price: {self.price}, Quantity: {self.quantity}"
    
    def update_quantity(self, quantity):
        """Update the quantity of product increasing"""
        if quantity > 0:
            self.quantity += quantity
            return "Updated price."
        else:
            return "Price must be a positive value."

