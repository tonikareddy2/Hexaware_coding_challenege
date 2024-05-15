from DAO.IOrderManagementRepository import IOrderManagementRepository
from Entity import Users, Product
from Util.DBconn import DBconnection
from MyExceptions.ManagementException import UserNotFound, OrderNotFound, AdminRequired


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
