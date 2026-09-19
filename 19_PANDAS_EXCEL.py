```python
# ===================== 19_PANDAS_EXCEL.py =====================


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


# .........................Save DataFrame to Excel.........................#

df.to_excel(
    "students.xlsx",
    index=False
)

print("\nExcel file created successfully.")


# .........................Read Excel File.........................#

data = pd.read_excel("students.xlsx")

print("\nData from Excel:")

print(data)


# .........................First Rows.........................#

print("\nFirst 3 Rows:")

print(data.head(3))


# .........................Last Rows.........................#

print("\nLast 3 Rows:")

print(data.tail(3))


# .........................Shape.........................#

print("\nShape:")

print(data.shape)


# .........................Columns.........................#

print("\nColumns:")

print(data.columns)


# .........................Select One Column.........................#

print("\nNames:")

print(data["Name"])


# .........................Select Multiple Columns.........................#

print("\nName and Marks:")

print(data[["Name", "Marks"]])


# .........................Filter Data.........................#

print("\nStudents with Marks Greater Than 80:")

print(
    data[data["Marks"] > 80]
)


# .........................Filter by City.........................#

print("\nStudents from Ranchi:")

print(
    data[data["City"] == "Ranchi"]
)


# .........................Read Specific Columns.........................#

selected_data = pd.read_excel(
    "students.xlsx",
    usecols=["Name", "Marks"]
)

print("\nSelected Columns:")

print(selected_data)


# .........................Read Limited Rows.........................#

limited_data = pd.read_excel(
    "students.xlsx",
    nrows=3
)

print("\nFirst 3 Rows:")

print(limited_data)


# .........................Set Column as Index.........................#

index_data = pd.read_excel(
    "students.xlsx",
    index_col="Name"
)

print("\nName as Index:")

print(index_data)


# .........................Check Data Types.........................#

print("\nData Types:")

print(data.dtypes)


# .........................Create Multiple Sheets.........................#

students = pd.DataFrame({
    "Name": ["Aman", "Rahul", "Priya"],
    "Marks": [75, 82, 88]
})

sales = pd.DataFrame({
    "Product": ["Laptop", "Mobile", "Tablet"],
    "Sales": [50000, 30000, 20000]
})


with pd.ExcelWriter("college_data.xlsx") as writer:

    students.to_excel(
        writer,
        sheet_name="Students",
        index=False
    )

    sales.to_excel(
        writer,
        sheet_name="Sales",
        index=False
    )

print("\nMultiple Excel Sheets Created.")


# .........................Read Specific Sheet.........................#

student_data = pd.read_excel(
    "college_data.xlsx",
    sheet_name="Students"
)

print("\nStudents Sheet:")

print(student_data)


# .........................Read Sales Sheet.........................#

sales_data = pd.read_excel(
    "college_data.xlsx",
    sheet_name="Sales"
)

print("\nSales Sheet:")

print(sales_data)


# .........................Calculate Excel Data.........................#

total_sales = sales_data["Sales"].sum()

print("\nTotal Sales:")

print(total_sales)


# .........................Average Marks.........................#

average_marks = student_data["Marks"].mean()

print("\nAverage Marks:")

print(average_marks)


# .........................Add New Column.........................#

student_data["Result"] = student_data["Marks"].apply(
    lambda x: "Pass" if x >= 40 else "Fail"
)

print("\nAfter Adding Result Column:")

print(student_data)


# .........................Save Updated Excel File.........................#

student_data.to_excel(
    "updated_students.xlsx",
    index=False
)

print("\nUpdated Excel File Saved.")


# .........................Sales Analysis Example.........................#

sales_data["Category"] = ["Electronics", "Electronics", "Electronics"]

print("\nSales Analysis:")

print(sales_data)


# .........................Filter High Sales.........................#

high_sales = sales_data[
    sales_data["Sales"] > 25000
]

print("\nSales Greater Than 25000:")

print(high_sales)


# .........................Final Data.........................#

print("\nFinal Student Data:")

print(student_data)

print("\nFinal Sales Data:")

print(sales_data)
```
