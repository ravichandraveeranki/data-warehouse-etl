from scripts.extract import extract
from scripts.transform import transform
from scripts.load import load

customers, products, sales = extract()
sales_data = transform(customers, products, sales)
load(sales_data)

print("ETL pipeline completed successfully.")
print(sales_data.head())