import pandas as pd

# Extract
customers = pd.read_csv("data/customers.csv")
products = pd.read_csv("data/products.csv")
sales = pd.read_csv("data/sales.csv")

# Transform
sales_data = sales.merge(customers, on="customer_id", how="left")
sales_data = sales_data.merge(products, on="product_id", how="left")
sales_data["revenue"] = sales_data["quantity"] * sales_data["price"]

# Load
sales_data.to_csv("data/final_sales_data.csv", index=False)

print("ETL pipeline completed successfully.")
print(sales_data)