# This is an exercise project that I wrote during my internship in IELTSways Academy These codes are for implementing a shopping cart as well as products.


## If you want to use this project, you can install and use the project packages with the following command:
```bash pip install requierments.txt
```


## The APIs I wrote for this project are as follows:
  - An API for user login
  - An API for products
  - An API for the shopping cart
## Each of which has different parts.

-----------------------------------------------------------------------

### Ednpoint for user login 
- The login API is available at this address  `login/`
- The register API is available at this address  `register/`
- The profile detail API is available at this address  `profile/<int:pk>/`
- The token refresh API is available at this address  `token/refresh/`
-----------------------------------------------------------------------
### Ednpoint for product
- The API of the products is available at this address  `products/` this API for list of products
- The API details of the products are available at this address `products/<int:pk>/`
- The API for creating products is available at this address  `products/create/`
-----------------------------------------------------------------------
### Ednpoint for Shopping cart
- The API is available to display all orders at this address  `orders/`
- The API is available to display order details at this address `orders-detail/<int:pk>/`
- The API is available to create order at this address  `orders-create/`
- The Add to cart API is available at this address  `add-to-cart/`
- The API for displaying the shopping cart is available at this address  `view-cart/`
- The api to remove the product from the shopping cart is available at this address  `remove-from-cart/<int:pk>/`
- The Payment api is available at this address  `payment/`
-----------------------------------------------------------------------
- ### The payment gateway is also implemented in this project using Zarinpal


