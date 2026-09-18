```python
# ===================== 14_PANDAS_AGGREGATION.py =====================


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
    "Department": [
        "IT",
        "HR",
        "IT",
        "Sales",
        "Sales",
        "HR"
    ],
    "Salary": [
        30000,
        28000,
        35000,
        25000,
        32000,
        30000
    ],
    "Age": [20, 22, 21, 24, 23, 22]
}

df = pd.DataFrame(data)

print("Original DataFrame:")

print(df)


# .........................Sum.........................#

total_salary = df["Salary"].sum()

print("\nTotal Salary:")

print(total_salary)


# .........................Mean.........................#

average_salary = df["Salary"].mean()

print("\nAverage Salary:")

print(average_salary)


# .........................Maximum.........................#

highest_salary = df["Salary"].max()

print("\nHighest Salary:")

print(highest_salary)


# .........................Minimum.........................#

lowest_salary = df["Salary"].min()

print("\nLowest Salary:")

print(lowest_salary)


# .........................Count.........................#

total_employees = df["Name"].count()

print("\nTotal Employees:")

print(total_employees)


# .........................Median.........................#

median_salary = df["Salary"].median()

print("\nMedian Salary:")

print(median_salary)


# .........................Standard Deviation.........................#

salary_std = df["Salary"].std()

print("\nSalary Standard Deviation:")

print(salary_std)


# .........................Multiple Aggregations.........................#

result = df["Salary"].agg(
    ["sum", "mean", "max", "min", "median", "std"]
)

print("\nMultiple Salary Calculations:")

print(result)


# .........................Aggregation by Department.........................#

result = df.groupby("Department")["Salary"].agg(
    ["sum", "mean", "max", "min", "count"]
)

print("\nDepartment Wise Salary Analysis:")

print(result)


# .........................Multiple Columns Aggregation.........................#

result = df.groupby("Department").agg(
    {
        "Salary": ["sum", "mean", "max", "min"],
        "Age": ["mean", "min", "max"]
    }
)

print("\nDepartment Wise Salary and Age Analysis:")

print(result)


# .........................Named Aggregation.........................#

result = df.groupby("Department").agg(
    Average_Salary=("Salary", "mean"),
    Highest_Salary=("Salary", "max"),
    Total_Salary=("Salary", "sum"),
    Employee_Count=("Name", "count")
)

print("\nDepartment Summary:")

print(result)


# .........................Aggregation with Multiple Functions.........................#

result = df.agg(
    {
        "Salary": ["sum", "mean", "max", "min"],
        "Age": ["mean", "max", "min"]
    }
)

print("\nOverall Data Analysis:")

print(result)


# .........................Product Sales Example.........................#

sales_data = {
    "Product": [
        "Laptop",
        "Mobile",
        "Laptop",
        "Tablet",
        "Mobile",
        "Tablet"
    ],
    "Sales": [
        50000,
        20000,
        45000,
        15000,
        25000,
        18000
    ]
}

sales_df = pd.DataFrame(sales_data)

print("\nSales Data:")

print(sales_df)


# .........................Product Wise Aggregation.........................#

product_analysis = sales_df.groupby("Product")["Sales"].agg(
    ["sum", "mean", "max", "min", "count"]
)

print("\nProduct Wise Sales Analysis:")

print(product_analysis)


# .........................Final Analysis.........................#

print("\nFinal Analysis:")

print("Total Salary:", total_salary)

print("Average Salary:", average_salary)

print("Highest Salary:", highest_salary)

print("Lowest Salary:", lowest_salary)

print("Total Employees:", total_employees)
```
