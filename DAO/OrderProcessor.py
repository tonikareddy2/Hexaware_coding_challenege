from DAO.IOrderManagementRepository import IOrderManagementRepository
from Entity import Users, Product
from Util.DBconn import DBconnection
from MyExceptions.ManagementException import UserNotFound, OrderNotFound


class OrderProcessor(IOrderManagementRepository, DBconnection):
    def createOrder(self, user, products):
        try:
            self.cursor.execute("SELECT * FROM Users WHERE userId=?", (user.userId,))
            user_exists = self.cursor.fetchone()
            if not user_exists:
                self.cursor.execute(
                    "INSERT INTO Users (userId, username, password, role) VALUES (?, ?, ?, ?)",
                    (user.userId, user.username, user.password, user.role),
                )
                self.conn.commit()
                print("User created successfully.")
        except Exception as e:
            print("Error creating order:", e)

    def cancelOrder(self, userId, orderId):
        try:
            self.cursor.execute(
                "SELECT * FROM Orders WHERE userId=? AND orderId=?", (userId, orderId)
            )
            order_exists = self.cursor.fetchone()
            print("Order Canceled Successfully")
            if not order_exists:
                raise OrderNotFound(orderId)
        except Exception as e:
            print("Error canceling order:", e)

    def getAllProducts(self):
        try:
            self.cursor.execute("SELECT * FROM Product")
            products = self.cursor.fetchall()
            for product in products:
                print(product)
        except Exception as e:
            print("Error getting all products:", e)

    def getOrderByUser(self, user):
        try:
            self.cursor.execute("SELECT * FROM Orders WHERE userId=?", (user.userId,))
            orders = self.cursor.fetchall()
            for order in orders:
                print(order)

        except Exception as e:
            print("Error getting orders by user:", e)

    def createProduct(self, product):
        try:
            self.cursor.execute(
                "INSERT INTO Product (productId, productName, description, price, quantityInStock, type) VALUES (?, ?, ?, ?, ?, ?)",
                (
                    product.productId,
                    product.productName,
                    product.description,
                    product.price,
                    product.quantityInStock,
                    product.type,
                ),
            )
            self.conn.commit()
            print("Product created successfully.")

        except Exception as e:
            print("Error creating product:", e)

    def createUser(self, user):
        try:
            self.cursor.execute("SELECT * FROM Users WHERE userId=?", (user.userId,))
            user_exists = self.cursor.fetchone()
            if user_exists:
                print("User already exists.")
                return
            self.cursor.execute(
                "INSERT INTO Users (userId, username, password, role) VALUES (?, ?, ?, ?)",
                (user.userId, user.username, user.password, user.role),
            )
            self.conn.commit()
            print("User created successfully.")

        except Exception as e:
            print("Error creating user:", e)
