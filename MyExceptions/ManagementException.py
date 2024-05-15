class UserNotFound(Exception):
    def __init__(self, user_id):
        super().__init__(f"User with ID {user_id} not found in the database.")


class OrderNotFound(Exception):
    def __init__(self, order_id):
        super().__init__(f"Order with ID {order_id} not found in the database.")


class AdminRequired(Exception):
    def __init__(self):
        super().__init__("Only admin users are allowed to perform this operation.")
