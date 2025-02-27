class Cart:
    def __init__(self):
        self.cart_items = []
        
    def add_item(self, product, quantity):
        """Adding products to the cart"""
        if product.quantity < quantity:
            return f"{product.name} insufficient in stock, please enter a smaller quantity"
        else:
            self.cart_items.append((product, quantity))
        return f"New product added to the cart: {product.name}"
    
    def total_cart(self):
        """Calculating the total value of the cart items"""
        return sum(item[0].price * item[1] for item in self.cart_items)
    
    def display_cart(self):
        """Displaying the contents of the cart"""
        items_info = ""
        for i, item in enumerate(self.cart_items, start=1):
                items_info += f"{i}. {item[0].name}: {item[0].price} x {item[1]}\n"   
        return f"{items_info}"

                
