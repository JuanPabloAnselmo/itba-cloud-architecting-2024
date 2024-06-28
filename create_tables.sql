CREATE TABLE selling_items (
    InvoiceNo VARCHAR(50) PRIMARY KEY,
    StockCode VARCHAR(50) NOT NULL,
    Description VARCHAR(100),
    Quantity INT,
    InvoiceDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UnitPrice DECIMAL(10, 2),
    CustomerID VARCHAR(50),
    Country VARCHAR(200)
);


