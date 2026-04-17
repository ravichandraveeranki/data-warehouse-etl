import pandas as pd

def extract():
    customers = pd.read_csv("data/customers.csv")
    products = pd.read_csv("data/products.csv")
    sales = pd.read_csv("data/sales.csv")

    return customers, products, sales