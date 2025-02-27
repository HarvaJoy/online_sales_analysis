from product_manager import ProductManager
from product import Product
from data import products
from cart import Cart

"""Main program"""
def main():
    # Added products in Product manager
    product_manager = ProductManager()
    for product in products:
        product_manager.add_product(Product(
                                    product["name"], 
                                    product["price"], 
                                    product["quantity"]))

    # # Display info about the products
    # print("All Products:")
    # print(product_manager.display_products())

    # Show the Total inventory value in stock
    # print(f'Inventory Valuation: {product_manager.calc_inventory_value()}\n')

    # Remove products by name
    print(product_manager.remove_product('Memory USB'))
    print('Upated list of products:')
    print(product_manager.display_products())

    # init the cart
    cart_items = [
        (product_manager.filter_product('Laptop'), 2),
        (product_manager.filter_product('Monitor'), 4),
        (product_manager.filter_product('Keyboards'), 2)
    ]
    cart = Cart()
    for item in cart_items:
        cart.add_item(item[0], item[1])
        
    # Cart details
    print('Shopping cart status:')
    print(cart.display_cart())
    print(f"Total cart: {cart.total_cart()}\n")
    
    
""" Run the main program"""
if __name__ == '__main__':
    main()  
   
    
    