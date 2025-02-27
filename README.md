# Online Sales Analysis 

Sales data analysis system in an online store


## Description 

Functional Python project that uses advanced OOP concepts. System that can work with products (adding, displaying, updating and removing); customer cart management (adding products, displaying content and calculating the total value).


## Classes and Functionalities
    * Product:
        - Contains the attributes: name, price and quantity.
        Methods:
        - display_info() - Method for displaying product information.
        - update_quantity() - Method for updating product quantity.
    
    * ProductManager:
        - Contains as an attribute a list of all available products.
        Methods:
        - add_product() - Adding products.
        - display_products() - Displaying all products.
        - calc_inventory_value() - Displaying the total value of all products.
        - remove_product() - Remove products by name.
        - filter_product() - Filter a product by name.
    
     * Cart:
        - Contains the attributes: car_items.
        Methods
        - add_item() - Adding products to the cart.
        - total_cart() - Calculating the total value of the cart items.
        - display_cart() - Displaying the contents of the cart.

