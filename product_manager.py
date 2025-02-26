class ProductManager:
    def __init__(self):
        self.products = []
        
    def add_product(self, product):
        """Add a product to the list of products"""
        self.products.append(product)
        return "Added product"

    def display_products(self):
        """Display a list of product"""
        if not self.products:
            print("Out of stock")
        else:
            list_product = ""
            for product in self.products: 
                list_product += product.display_info()+"\n"
            return "All Products:" + "\n" + f"{list_product}"
    
    def calc_inventory_value(self):
        """Calculate value of unsold products"""    
        return sum(product.price * product.quantity for product in self.products)
        
