```python
# ===================== 27_PANDAS_DATA_ANALYSIS.py =====================


import pandas as pd


# .........................Create Dataset.........................#

data = {
    "Product": [
        "Laptop",
        "Mobile",
        "Tablet",
        "Laptop",
        "Mobile",
        "Monitor",
        "Tablet",
        "Laptop",
        "Mobile",
        "Monitor"
    ],
    "Category": [
        "Electronics",
        "Electronics",
        "Electronics",
        "Electronics",
        "Electronics",
        "Electronics",
        "Electronics",
        "Electronics",
        "Electronics",
        "Electronics"
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
        "Ranchi",
        "Jamshedpur"
    ],
    "Sales": [
        50000,
        30000,
        20000,
        55000,
        35000,
        15000,
        25000,
        60000,
        40000,
        18000
    ],
    "Quantity": [
        5,
        10,
        8,
        6,
        12,
        6,
        10,
        7,
        15,
        5
    ]
}

df = pd.DataFrame(data)

print("Original Dataset:")

print(df)


# .........................Understand Dataset.........................#

print("\nFirst 5 Rows:")

print(df.head())


print("\nLast 5 Rows:")

print(df.tail())


print("\nShape:")

print(df.shape)


print("\nColumns:")

print(df.columns)


print("\nData Types:")

print(df.dtypes)


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

print("\nTotal Sales:")

print(total_sales)


# .........................Total Quantity.........................#

total_quantity = df["Quantity"].sum()

print("\nTotal Quantity Sold:")

print(total_quantity)


# .........................Average Sales.........................#

average_sales = df["Sales"].mean()

print("\nAverage Sales:")

print(average_sales)


# .........................Highest Sale.........................#

highest_sale = df["Sales"].max()

print("\nHighest Sale:")

print(highest_sale)


# .........................Lowest Sale.........................#

lowest_sale = df["Sales"].min()

print("\nLowest Sale:")

print(lowest_sale)


# .........................Highest Sale Product.........................#

highest_product = df[
    df["Sales"] == df["Sales"].max()
]

print("\nProduct with Highest Sale:")

print(highest_product)


# .........................Lowest Sale Product.........................#

lowest_product = df[
    df["Sales"] == df["Sales"].min()
]

print("\nProduct with Lowest Sale:")

print(lowest_product)


# .........................Sales by Product.........................#

product_sales = df.groupby(
    "Product"
)["Sales"].sum()

print("\nTotal Sales by Product:")

print(product_sales)


# .........................Quantity by Product.........................#

product_quantity = df.groupby(
    "Product"
)["Quantity"].sum()

print("\nTotal Quantity by Product:")

print(product_quantity)


# .........................Sales by City.........................#

city_sales = df.groupby(
    "City"
)["Sales"].sum()

print("\nTotal Sales by City:")

print(city_sales)


# .........................Quantity by City.........................#

city_quantity = df.groupby(
    "City"
)["Quantity"].sum()

print("\nTotal Quantity by City:")

print(city_quantity)


# .........................Average Sales by Product.........................#

average_product_sales = df.groupby(
    "Product"
)["Sales"].mean()

print("\nAverage Sales by Product:")

print(average_product_sales)


# .........................Sort Products by Sales.........................#

sorted_sales = df.sort_values(
    "Sales",
    ascending=False
)

print("\nSales from Highest to Lowest:")

print(sorted_sales)


# .........................Top 5 Sales.........................#

top_5 = df.nlargest(
    5,
    "Sales"
)

print("\nTop 5 Sales:")

print(top_5)


# .........................Filter High Sales.........................#

high_sales = df[
    df["Sales"] > 40000
]

print("\nSales Greater Than 40000:")

print(high_sales)


# .........................Filter Specific City.........................#

ranchi_data = df[
    df["City"] == "Ranchi"
]

print("\nRanchi Sales:")

print(ranchi_data)


# .........................Multiple Conditions.........................#

high_ranchi_sales = df[
    (df["City"] == "Ranchi") &
    (df["Sales"] > 30000)
]

print("\nRanchi Sales Greater Than 30000:")

print(high_ranchi_sales)


# .........................Calculate Average Selling Price.........................#

df["Average_Price"] = (
    df["Sales"] / df["Quantity"]
)

print("\nAverage Selling Price:")

print(df)


# .........................Round Average Price.........................#

df["Average_Price"] = df[
    "Average_Price"
].round(2)

print("\nRounded Average Price:")

print(df)


# .........................Sales Category.........................#

df["Sales_Category"] = df["Sales"].apply(
    lambda x:
        "High" if x >= 40000
        else "Medium" if x >= 20000
        else "Low"
)

print("\nSales Category:")

print(df)


# .........................Category Count.........................#

category_count = df[
    "Sales_Category"
].value_counts()

print("\nSales Category Count:")

print(category_count)


# .........................Product Summary.........................#

product_summary = df.groupby(
    "Product"
).agg(
    Total_Sales=("Sales", "sum"),
    Total_Quantity=("Quantity", "sum"),
    Average_Sales=("Sales", "mean")
)

print("\nProduct Summary:")

print(product_summary)


# .........................City Summary.........................#

city_summary = df.groupby(
    "City"
).agg(
    Total_Sales=("Sales", "sum"),
    Total_Quantity=("Quantity", "sum"),
    Average_Sales=("Sales", "mean")
)

print("\nCity Summary:")

print(city_summary)


# .........................Find Best Product.........................#

best_product = product_summary[
    "Total_Sales"
].idxmax()

print("\nProduct with Highest Total Sales:")

print(best_product)


# .........................Find Best City.........................#

best_city = city_summary[
    "Total_Sales"
].idxmax()

print("\nCity with Highest Total Sales:")

print(best_city)


# .........................Sales Percentage.........................#

df["Sales_Percentage"] = (
    df["Sales"] / total_sales
) * 100

df["Sales_Percentage"] = df[
    "Sales_Percentage"
].round(2)

print("\nSales Percentage:")

print(df)


# .........................Final Analysis.........................#

print("\n========== FINAL ANALYSIS ==========")


print("\nTotal Sales:")

print(total_sales)


print("\nTotal Quantity:")

print(total_quantity)


print("\nAverage Sale:")

print(round(average_sales, 2))


print("\nHighest Sale:")

print(highest_sale)


print("\nLowest Sale:")

print(lowest_sale)


print("\nBest Product:")

print(best_product)


print("\nBest City:")

print(best_city)


# .........................Final Dataset.........................#

print("\nFinal Dataset:")

print(df)
```
