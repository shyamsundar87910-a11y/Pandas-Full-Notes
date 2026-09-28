```python
# ===================== 29_PANDAS_MINI_PROJECT.py =====================


import pandas as pd


# .........................Project Title.........................#

print("========================================")
print("     E-COMMERCE SALES ANALYSIS")
print("========================================")


# .........................Project Objective.........................#

# Objective:
# Analyze e-commerce sales data using Pandas.
#
# We will find:
# 1. Total Sales
# 2. Total Quantity
# 3. Average Sales
# 4. Product-wise Sales
# 5. Category-wise Sales
# 6. City-wise Sales
# 7. Top Selling Products
# 8. Sales Performance
# 9. Business Insights


# .........................Create Dataset.........................#

data = {
    "Order_ID": [
        101, 102, 103, 104, 105,
        106, 107, 108, 109, 110,
        111, 112, 113, 114, 115
    ],

    "Product": [
        "Laptop",
        "Mobile",
        "Tablet",
        "Laptop",
        "Monitor",
        "Mobile",
        "Keyboard",
        "Laptop",
        "Mouse",
        "Tablet",
        "Mobile",
        "Monitor",
        "Keyboard",
        "Laptop",
        "Mouse"
    ],

    "Category": [
        "Electronics",
        "Electronics",
        "Electronics",
        "Electronics",
        "Electronics",
        "Electronics",
        "Accessories",
        "Electronics",
        "Accessories",
        "Electronics",
        "Electronics",
        "Electronics",
        "Accessories",
        "Electronics",
        "Accessories"
    ],

    "City": [
        "Jamshedpur",
        "Ranchi",
        "Dhanbad",
        "Ranchi",
        "Jamshedpur",
        "Dhanbad",
        "Ranchi",
        "Jamshedpur",
        "Dhanbad",
        "Ranchi",
        "Jamshedpur",
        "Dhanbad",
        "Ranchi",
        "Jamshedpur",
        "Dhanbad"
    ],

    "Sales": [
        55000,
        32000,
        22000,
        60000,
        18000,
        35000,
        5000,
        65000,
        3000,
        25000,
        38000,
        20000,
        6000,
        70000,
        4000
    ],

    "Quantity": [
        5,
        8,
        6,
        6,
        4,
        10,
        5,
        7,
        6,
        7,
        11,
        5,
        6,
        8,
        7
    ],

    "Date": [
        "2026-01-05",
        "2026-01-08",
        "2026-01-12",
        "2026-01-15",
        "2026-01-20",
        "2026-02-03",
        "2026-02-08",
        "2026-02-15",
        "2026-02-20",
        "2026-02-25",
        "2026-03-05",
        "2026-03-10",
        "2026-03-15",
        "2026-03-20",
        "2026-03-25"
    ]
}


df = pd.DataFrame(data)


print("\nOriginal Dataset:")

print(df)


# .........................Understand Dataset.........................#

print("\n========== DATASET INFORMATION ==========")


print("\nFirst 5 Rows:")

print(df.head())


print("\nShape:")

print(df.shape)


print("\nColumns:")

print(df.columns)


print("\nData Types:")

print(df.dtypes)


# .........................Convert Date Column.........................#

df["Date"] = pd.to_datetime(
    df["Date"]
)

print("\nDate Column:")

print(df["Date"])


# .........................Check Missing Values.........................#

print("\nMissing Values:")

print(df.isnull().sum())


# .........................Check Duplicate Rows.........................#

print("\nDuplicate Rows:")

print(df.duplicated().sum())


# .........................Basic Statistics.........................#

print("\nStatistical Summary:")

print(df.describe())


# .........................Total Sales.........................#

total_sales = df["Sales"].sum()

print("\n========== KEY PERFORMANCE INDICATORS ==========")

print("\nTotal Sales:")

print(total_sales)


# .........................Total Quantity.........................#

total_quantity = df["Quantity"].sum()

print("\nTotal Quantity Sold:")

print(total_quantity)


# .........................Average Sales.........................#

average_sales = df["Sales"].mean()

print("\nAverage Order Sales:")

print(round(average_sales, 2))


# .........................Highest Sale.........................#

highest_sale = df["Sales"].max()

print("\nHighest
```
