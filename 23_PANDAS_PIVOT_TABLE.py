```python
# ===================== 23_PANDAS_PIVOT_TABLE.py =====================


import pandas as pd


# .........................Create DataFrame.........................#

data = {
    "Name": [
        "Aman", "Rahul", "Rohit",
        "Priya", "Neha", "Vikas"
    ],
    "Department": [
        "IT", "HR", "IT",
        "Sales", "HR", "Sales"
    ],
    "City": [
        "Jamshedpur", "Ranchi", "Ranchi",
        "Dhanbad", "Jamshedpur", "Ranchi"
    ],
    "Sales": [
        50000, 30000, 45000,
        25000, 35000, 40000
    ],
    "Quantity": [
        5, 3, 4,
        2, 3, 4
    ]
}

df = pd.DataFrame(data)

print("Original Data:")

print(df)


# .........................Basic Pivot Table.........................#

pivot = pd.pivot_table(
    df,
    values="Sales",
    index="Department"
)

print("\nSales by Department:")

print(pivot)


# .........................Pivot Table with Sum.........................#

pivot = pd.pivot_table(
    df,
    values="Sales",
    index="Department",
    aggfunc="sum"
)

print("\nTotal Sales by Department:")

print(pivot)


# .........................Pivot Table with Mean.........................#

pivot = pd.pivot_table(
    df,
    values="Sales",
    index="Department",
    aggfunc="mean"
)

print("\nAverage Sales by Department:")

print(pivot)


# .........................Pivot Table with Multiple Functions.........................#

pivot = pd.pivot_table(
    df,
    values="Sales",
    index="Department",
    aggfunc=["sum", "mean", "max", "min"]
)

print("\nMultiple Aggregations:")

print(pivot)


# .........................Pivot Table with Multiple Values.........................#

pivot = pd.pivot_table(
    df,
    values=["Sales", "Quantity"],
    index="Department",
    aggfunc="sum"
)

print("\nSales and Quantity by Department:")

print(pivot)


# .........................Pivot Table with Two Indexes.........................#

pivot = pd.pivot_table(
    df,
    values="Sales",
    index=["Department", "City"],
    aggfunc="sum"
)

print("\nSales by Department and City:")

print(pivot)


# .........................Columns in Pivot Table.........................#

pivot = pd.pivot_table(
    df,
    values="Sales",
    index="Department",
    columns="City",
    aggfunc="sum"
)

print("\nSales by Department and City:
```
