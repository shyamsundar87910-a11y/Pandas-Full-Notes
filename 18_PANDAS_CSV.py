```python
# ===================== 18_PANDAS_CSV.py =====================


import pandas as pd


# .........................Create DataFrame.........................#

data = {
    "Name": ["Aman", "Rahul", "Rohit", "Priya", "Neha"],
    "Age": [20, 21, 19, 22, 20],
    "Marks": [75, 82, 91, 68, 88],
    "City": ["Jamshedpur", "Ranchi", "Jamshedpur", "Dhanbad", "Ranchi"]
}

df = pd.DataFrame(data)

print("Original DataFrame:")

print(df)


# .........................Save DataFrame to CSV.........................#

df.to_csv(
    "students.csv",
    index=False
)

print("\nCSV file created successfully.")


# .........................Read CSV File.........................#

data = pd.read_csv("students.csv")

print("\nData from CSV:")

print(data)


# .........................First Rows.........................#

print("\nFirst 3 Rows:")

print(data.head(3))


# .........................Last Rows.........................#

print("\nLast 3 Rows:")

print(data.tail(3))


# .........................Shape of CSV Data.........................#

print("\nShape:")

print(data.shape)


# .........................Column Names.........................#

print("\nColumns:")

print(data.columns)


# .........................Select One Column.........................#

print("\nNames:")

print(data["Name"])


# .........................Select Multiple Columns.........................#

print("\nName and Marks:")

print(data[["Name", "Marks"]])


# .........................Filter CSV Data.........................#

print("\nStudents with Marks greater than 80:")

print(
    data[data["Marks"] > 80]
)


# .........................Filter by City.........................#

print("\nStudents from Ranchi:")

print(
    data[data["City"] == "Ranchi"]
)


# .........................Usecols.........................#

selected_data = pd.read_csv(
    "students.csv",
    usecols=["Name", "Marks"]
)

print("\nSelected Columns Using usecols:")

print(selected_data)


# .........................Read Limited Rows.........................#

limited_data = pd.read_csv(
    "students.csv",
    nrows=3
)

print("\nFirst 3 Rows Using nrows:")

print(limited_data)


# .........................Skip Rows.........................#

skip_data = pd.read_csv(
    "students.csv",
    skiprows=[1]
)

print("\nData After Skipping Row:")

print(skip_data)


# .........................Set Column as Index.........................#

index_data = pd.read_csv(
    "students.csv",
    index_col="Name"
)

print("\nName as Index:")

print(index_data)


# .........................Change Data Type.........................#

type_data = pd.read_csv(
    "students.csv",
    dtype={"Age": "int64", "Marks": "int64"}
)

print("\nData Types:")

print(type_data.dtypes)


# .........................Missing Values in CSV.........................#

missing_data = pd.DataFrame({
    "Name": ["Aman", "Rahul", "Rohit", "Priya"],
    "Marks": [75, None, 91, None]
})

missing_data.to_csv(
    "students_missing.csv",
    index=False
)

new_data = pd.read_csv("students_missing.csv")

print("\nCSV with Missing Values:")

print(new_data)


# .........................Check Missing Values.........................#

print("\nMissing Values:")

print(new_data.isnull())


print("\nMissing Value Count:")

print(new_data.isnull().sum())


# .........................Fill Missing Values.........................#

new_data["Marks"] = new_data["Marks"].fillna(0)

print("\nAfter Filling Missing Marks:")

print(new_data)


# .........................na_values.........................#

new_data = pd.DataFrame({
    "Name": ["Aman", "Rahul", "Rohit"],
    "Marks": [75, "NA", 91]
})

new_data.to_csv(
    "marks.csv",
    index=False
)

marks_data = pd.read_csv(
    "marks.csv",
    na_values=["NA"]
)

print("\nNA Converted to Missing Value:")

print(marks_data)


# .........................Save Cleaned Data.........................#

marks_data["Marks"] = marks_data["Marks"].fillna(
    marks_data["Marks"].mean()
)

marks_data.to_csv(
    "cleaned_marks.csv",
    index=False
)

print("\nCleaned Data:")

print(marks_data)


# .........................Sales CSV Example.........................#

sales = {
    "Product": ["Laptop", "Mobile", "Tablet", "Monitor", "Keyboard"],
    "Sales": [50000, 30000, 20000, 15000, 5000],
    "Quantity": [5, 10, 8, 6, 15]
}

sales_df = pd.DataFrame(sales)

sales_df.to_csv(
    "sales.csv",
    index=False
)

print("\nSales CSV Created:")

print(sales_df)


# .........................Read Sales CSV.........................#

sales_data = pd.read_csv("sales.csv")

print("\nSales Data:")

print(sales_data)


# .........................Sales Filtering.........................#

print("\nProducts with Sales Greater Than 20000:")

print(
    sales_data[sales_data["Sales"] > 20000]
)


# .........................Total Sales.........................#

total_sales = sales_data["Sales"].sum()

print("\nTotal Sales:")

print(total_sales)


# .........................Average Sales.........................#

average_sales = sales_data["Sales"].mean()

print("\nAverage Sales:")

print(average_sales)


# .........................Final CSV Data.........................#

print("\nFinal Sales Data:")

print(sales_data)
```
