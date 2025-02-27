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
            return f"{list_product}"
    
    def calc_inventory_value(self):
        """Calculate value of unsold products"""    
        return sum(product.price * product.quantity for product in self.products)
    
    def remove_product(self, product_name):
        """Remove products by name"""
        index_product = [index for index, product in enumerate(self.products) if product.name == product_name]
        if not index_product:
            return f"The product name {product_name} doesn't exist."
        else:
            self.products.pop(index_product[0])
            return f"Removed {product_name}"
    
    def filter_product(self, product_name):
        """Filter a product by name"""
        return list(filter(lambda x: x.name == product_name, self.products))[0]
            
      
            