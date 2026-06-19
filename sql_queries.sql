-- Category Revenue

SELECT Category,
SUM(Sales) AS Revenue
FROM sales
GROUP BY Category;

-- Product Revenue

SELECT Product,
SUM(Sales) AS Revenue
FROM sales
GROUP BY Product
ORDER BY Revenue DESC;

-- Quantity Sold

SELECT Product,
SUM(Quantity) AS Quantity
FROM sales
GROUP BY Product
ORDER BY Quantity DESC;