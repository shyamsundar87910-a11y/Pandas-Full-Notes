```python
# ===================== 17_PANDAS_CONCATENATE.py =====================


import pandas as pd


# .........................First DataFrame.........................#

data1 = {
    "Name": ["Aman", "Rahul", "Rohit"],
    "Marks": [75, 82, 91]
}

df1 = pd.DataFrame(data1)

print("First DataFrame:")

print(df1)


# .........................Second DataFrame.........................#

data2 = {
    "Name": ["Vikas", "Ankit", "Priya"],
    "Marks": [68, 88, 95]
}

df2 = pd.DataFrame(data2)

print("\nSecond DataFrame:")

print(df2)


# .........................Concatenate Rows.........................#

result = pd.concat(
    [df1, df2]
)

print("\nAfter Concatenating Rows:")

print(result)


# .........................Reset Index.........................#

result = pd.concat(
    [df1, df2],
    ignore_index=True
)

print("\nAfter Resetting Index:")

print(result)


# .........................Concatenate Columns.........................#

age_data = {
    "Age": [20, 21, 19]
}

age_df = pd.DataFrame(age_data)

result = pd.concat(
    [df1, age_df],
    axis=1
)

print("\nAfter Concatenating Columns:")

print(result)


# .........................Three DataFrames.........................#

data3 = {
    "Name": ["Neha", "Pooja"],
    "Marks": [78, 86]
}

df3 = pd.DataFrame(data3)

result = pd.concat(
    [df1, df2, df3],
    ignore_index=True
)

print("\nThree DataFrames:")

print(result)


# .........................Concatenate with Different Columns.........................#

first_data = {
    "Name": ["Aman", "Rahul"],
    "Marks": [75, 82]
}

second_data = {
    "Name": ["Rohit", "Vikas"],
    "Age": [19, 22]
}

first_df = pd.DataFrame(first_data)

second_df = pd.DataFrame(second_data)

result = pd.concat(
    [first_df, second_df],
    ignore_index=True
)

print("\nDifferent Columns:")

print(result)


# .........................Join Types in Concatenate.........................#

result = pd.concat(
    [first_df, second_df],
    join="inner",
    ignore_index=True
)

print("\nInner Join Concatenate:")

print(result)


# .........................Concatenate with Keys.........................#

result = pd.concat(
    [df1, df2],
    keys=["Group_1", "Group_2"]
)

print("\nConcatenate with Keys:")

print(result)


# .........................Select Data Using Keys.........................#

print("\nGroup 1 Data:")

print(result.loc["Group_1"])


# .........................Sales Data Example.........................#

sales1 = {
    "Product": ["Laptop", "Mobile"],
    "Sales": [50000, 30000]
}

sales2 = {
    "Product": ["Tablet", "Monitor"],
    "Sales": [20000, 15000]
}

sales_df1 = pd.DataFrame(sales1)

sales_df2 = pd.DataFrame(sales2)

sales_result = pd.concat(
    [sales_df1, sales_df2],
    ignore_index=True
)

print("\nSales Data:")

print(sales_result)


# .........................Monthly Sales Example.........................#

january = pd.DataFrame({
    "Product": ["Laptop", "Mobile"],
    "Sales": [50000, 30000]
})

february = pd.DataFrame({
    "Product": ["Laptop", "Mobile"],
    "Sales": [55000, 35000]
})

monthly_sales = pd.concat(
    [january, february],
    keys=["January", "February"]
)

print("\nMonthly Sales:")

print(monthly_sales)
```
