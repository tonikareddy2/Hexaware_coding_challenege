CREATE DATABASE OrdersDB;
Use OrdersDB;

CREATE TABLE Product (
    productId INT PRIMARY KEY,
    productName VARCHAR(255),
    description VARCHAR(255),
    price DECIMAL(18, 2),
    quantityInStock INT,
    type VARCHAR(200)
);

CREATE TABLE Electronics (
    productId INT PRIMARY KEY,
    brand VARCHAR(255),
    warrantyPeriod INT,
    FOREIGN KEY (productId) REFERENCES Product(productId)
);

CREATE TABLE Clothing (
    productId INT PRIMARY KEY,
    size VARCHAR(20),
    color VARCHAR(20),
    FOREIGN KEY (productId) REFERENCES Product(productId)
);

CREATE TABLE Users (
    userId INT PRIMARY KEY,
    username VARCHAR(255),
    password VARCHAR(255),
    role VARCHAR(20)
);