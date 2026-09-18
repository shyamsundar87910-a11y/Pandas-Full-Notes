```python
# ===================== 13_PANDAS_GROUPBY.py =====================


import pandas as pd


# .........................Create DataFrame.........................#

data = {
    "Name": [
        "Aman",
        "Rahul",
        "Rohit",
        "Vikas",
        "Ankit",
        "Priya"
    ],
    "City": [
        "Jamshedpur",
        "Ranchi",
        "Jamshedpur",
        "Ranchi",
        "Bokaro",
        "Bokaro"
    ],
    "Marks": [75, 82, 91, 68, 88, 95],
    "Age": [20, 21, 19, 22, 20, 21]
}

df = pd.DataFrame(data)

print("Original DataFrame:")

print(df)


# .........................Group by City.........................#

grouped_city = df.groupby("City")

print("\nGrouped by City:")

print(grouped_city)


# .........................Mean Marks by City.........................#

mean_marks = df.groupby("City")["Marks"].mean()

print("\nAverage Marks by City:")

print(mean_marks)


# .........................Maximum Marks by City.........................#

max_marks = df.groupby("City")["Marks"].max()

print("\nMaximum Marks by City:")

print(max_marks)


# .........................Minimum Marks by City.........................#

min_marks = df.groupby("City")["Marks"].min()

print("\nMinimum Marks by City:")

print(min_marks)


# .........................Total Marks by City.........................#

total_marks = df.groupby("City")["Marks"].sum()

print("\nTotal Marks by City:")

print(total_marks)


# .........................Count Students by City.........................#

student_count = df.groupby("City")["Name"].count()

print("\nStudent Count by City:")

print(student_count)


# .........................Group by City and Age.........................#

grouped_data = df.groupby(
    ["City", "Age"]
)["Marks"].mean()

print("\nAverage Marks by City and Age:")

print(grouped_data)


# .........................Multiple Calculations.........................#

result = df.groupby("City")["Marks"].agg(
    ["mean", "max", "min", "sum", "count"]
)

print("\nMultiple Calculations:")

print(result)


# .........................Group by City with Multiple Columns.........................#

result = df.groupby("City").agg(
    {
        "Marks": "mean",
        "Age": "mean"
    }
)

print("\nAverage Marks and Age by City:")

print(result)


# .........................Group by City and Sort.........................#

result = df.groupby("City")["Marks"].mean()

result = result.sort_values(
    ascending=False
)

print("\nCities Sorted by Average Marks:")

print(result)


# .........................Group by with Size.........................#

result = df.groupby("City").size()

print("\nNumber of Students in Each City:")

print(result)


# .........................Group by with Sum.........................#

data = {
    "Product": [
        "Laptop",
        "Mobile",
        "Laptop",
        "Tablet",
        "Mobile",
        "Tablet"
    ],
    "Sales": [50000, 20000, 45000, 15000, 25000, 18000]
}

sales_df = pd.DataFrame(data)

print("\nSales Data:")

print(sales_df)


# .........................Product Wise Sales.........................#

product_sales = sales_df.groupby(
    "Product"
)["Sales"].sum()

print("\nProduct Wise Total Sales:")

print(product_sales)


# .........................Product Wise Average Sales.........................#

product_average = sales_df.groupby(
    "Product"
)["Sales"].mean()

print("\nProduct Wise Average Sales:")

print(product_average)


# .........................Highest Selling Product.........................#

highest_product = sales_df.groupby(
    "Product"
)["Sales"].sum().sort_values(
    ascending=False
)

print("\nProducts by Total Sales:")

print(highest_product)
```
