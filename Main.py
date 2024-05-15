from DAO import OrderProcessor, IOrderManagementRepository
from Entity import Users, Product


class OrderManagement:
    def main():
        order_processor = OrderProcessor()
        while True:
            print(
                """      
                1. Create User
                2. Create Product
                3. Create Order
                4. Cancel Order
                5. Get All Products
                6. Get Order by User
                7. Exit
                """
            )

            choice = int(input("Please choose from above options: "))

            if choice == 1:
                pass

            elif choice == 2:
                product_id = int(input("Enter product ID: "))
                product_name = input("Enter product name: ")
                description = input("Enter description: ")
                price = float(input("Enter price: "))
                quantity_in_stock = int(input("Enter quantity in stock: "))
                product_type = input("Enter product type (Electronics/Clothing): ")
                product = Product(
                    product_id,
                    product_name,
                    description,
                    price,
                    quantity_in_stock,
                    product_type,
                )
                order_processor.createProduct(product)

            elif choice == 3:
                try:
                    user_id = int(input("Enter user ID: "))
                    num_products = int(
                        input("Enter the number of products in the order: ")
                    )
                    products = []
                    for i in range(num_products):
                        product_id = int(input(f"Enter product ID {i+1}: "))
                        product_name = input(f"Enter product name {i+1}: ")
                        description = input(f"Enter description {i+1}: ")
                        price = float(input(f"Enter price {i+1}: "))
                        quantity_in_stock = int(
                            input(f"Enter quantity in stock {i+1}: ")
                        )
                        product_type = input(
                            f"Enter product type {i+1} (Electronics/Clothing): "
                        ).capitalize()
                        product = Product(
                            product_id,
                            product_name,
                            description,
                            price,
                            quantity_in_stock,
                            product_type,
                        )
                        products.append(product)
                    user = Users(user_id, "", "", "")
                    order_processor.createOrder(user, products)
                    print("Order successfully created")
                except Exception as e:
                    print("Error creating order:", e)

            elif choice == 4:
                user_id = int(input("Enter user ID: "))
                order_id = int(input("Enter order ID: "))
                order_processor.cancelOrder(user_id, order_id)

            elif choice == 5:
                order_processor.getAllProducts()

            elif choice == 6:
                user_id = int(input("Enter user ID: "))
                user = Users(user_id, "", "", "")
                order_processor.getOrderByUser(user)

            elif choice == 7:
                print("Exited. Come Back Soon!👋")
                break


if __name__ == "__main__":
    print("Welcome to the Order Management System😊")
    OrderManagement.main()
