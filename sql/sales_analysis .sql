-- View all records
SELECT * FROM final_sales_data;

-- Total revenue by city
SELECT city, SUM(revenue) AS total_revenue
FROM final_sales_data
GROUP BY city
ORDER BY total_revenue DESC;

-- Top selling products
SELECT product_name, SUM(quantity) AS total_quantity
FROM final_sales_data
GROUP BY product_name
ORDER BY total_quantity DESC;