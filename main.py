from product_manager import ProductManager
from product import Product
from data import products


# Added products in Product manager
product_manager = ProductManager()
for product in products:
    product_manager.add_product(Product(product["name"], product["price"], product["quantity"]))

# Display info about the products
print("All Products:")
print(product_manager.display_products())

# Show the Total inventory value in stock
print('Inventory Valuation: ', product_manager.calc_inventory_value())

# Remove products by name
print(product_manager.remove_product('Monitor'))
print('Upated list of products:')
print(product_manager.display_products())