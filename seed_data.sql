-- Insert into Product table
INSERT INTO Product (productId, productName, description, price, quantityInStock, type)
VALUES 
(1, 'Laptop', 'High-performance laptop with SSD', 999.99, 10, 'Electronics'),
(2, 'T-shirt', 'Cotton t-shirt for daily wear', 19.99, 50, 'Clothing'),
(3, 'Smartphone', 'Latest smartphone with AI camera', 699.99, 20, 'Electronics'),
(4, 'Jeans', 'Blue denim jeans for men', 49.99, 30, 'Clothing'),
(5, 'Headphones', 'Wireless headphones with noise cancellation', 149.99, 15, 'Electronics');

-- Insert into Electronics table
INSERT INTO Electronics (productId, brand, warrantyPeriod)
VALUES
(1, 'Dell', 2),
(3, 'Apple', 1),
(5, 'Sony', 3);

-- Insert into Clothing table
INSERT INTO Clothing (productId, size, color)
VALUES
(2, 'M', 'Black'),
(4, 'L', 'Blue');

-- Insert into Users table
INSERT INTO Users (userId, username, password, role)
VALUES
(1, 'admin_user', 'admin123', 'Admin'),
(2, 'john_doe', 'password123', 'User'),
(3, 'jane_smith', 'securepass', 'User'),
(4, 'test_user', 'testpass', 'User'),
(5, 'super_admin', 'superadmin', 'Admin');

SELECT * FROM Product;
SELECT * FROM Users;
SELECT * FROM Electronics;
SELECT * FROM Clothing;