```python
# ===================== 26_PANDAS_WITH_MATPLOTLIB.py =====================


import pandas as pd
import matplotlib.pyplot as plt


# .........................Create DataFrame.........................#

data = {
    "Month": [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June"
    ],
    "Sales": [
        20000,
        25000,
        30000,
        28000,
        35000,
        40000
    ]
}

df = pd.DataFrame(data)

print("Sales Data:")

print(df)


# .........................Line Chart.........................#

plt.figure()

df.plot(
    x="Month",
    y="Sales",
    kind="line"
)

plt.title("Monthly Sales")

plt.xlabel("Month")

plt.ylabel("Sales")

plt.xticks(rotation=45)

plt.tight_layout()

plt.show()


# .........................Bar Chart.........................#

plt.figure()

df.plot(
    x="Month",
    y="Sales",
    kind="bar"
)

plt.title("Monthly Sales")

plt.xlabel("Month")

plt.ylabel("Sales")

plt.tight_layout()

plt.show()


# .........................Horizontal Bar Chart.........................#

plt.figure()

df.plot(
    x="Month",
    y="Sales",
    kind="barh"
)

plt.title("Monthly Sales")

plt.xlabel("Sales")

plt.ylabel("Month")

plt.tight_layout()

plt.show()


# .........................Pie Chart.........................#

plt.figure()

df.set_index("Month")["Sales"].plot(
    kind="pie",
    autopct="%1.1f%%"
)

plt.title("Sales Distribution")

plt.ylabel("")

plt.show()


# .........................Histogram.........................#

marks_data = {
    "Marks": [
        45, 52, 60, 65, 68,
        72, 75, 78, 82, 85,
        88, 91, 95
    ]
}

marks_df = pd.DataFrame(marks_data)

print("\nMarks Data:")

print(marks_df)


plt.figure()

marks_df["Marks"].plot(
    kind="hist",
    bins=5
)

plt.title("Marks Distribution")

plt.xlabel("Marks")

plt.ylabel("Frequency")

plt.show()


# .........................Box Plot.........................#

plt.figure()

marks_df["Marks"].plot(
    kind="box"
)

plt.title("Marks Box Plot")

plt.ylabel("Marks")

plt.show()


# .........................Scatter Plot.........................#

student_data = {
    "Study_Hours": [
        1, 2, 3, 4, 5, 6
    ],
    "Marks": [
        45, 52, 60, 70, 82, 90
    ]
}

students = pd.DataFrame(student_data)

print("\nStudent Data:")

print(students)


plt.figure()

students.plot(
    x="Study_Hours",
    y="Marks",
    kind="scatter"
)

plt.title("Study Hours vs Marks")

plt.xlabel("Study Hours")

plt.ylabel("Marks")

plt.show()


# .........................Multiple Columns Bar Chart.........................#

sales_data = {
    "Product": [
        "Laptop",
        "Mobile",
        "Tablet",
        "Monitor"
    ],
    "Sales": [
        50000,
        30000,
        20000,
        15000
    ],
    "Quantity": [
        5,
        10,
        8,
        6
    ]
}

sales_df = pd.DataFrame(sales_data)

print("\nProduct Sales Data:")

print(sales_df)


sales_df.plot(
    x="Product",
    y=["Sales", "Quantity"],
    kind="bar"
)

plt.title("Product Sales and Quantity")

plt.xlabel("Product")

plt.ylabel("Value")

plt.tight_layout()

plt.show()


# .........................Multiple Lines.........................#

monthly_data = {
    "Month": [
        "January",
        "February",
        "March",
        "April",
        "May"
    ],
    "Sales": [
        20000,
        25000,
        30000,
        28000,
        35000
    ],
    "Expenses": [
        12000,
        14000,
        15000,
        16000,
        18000
    ]
}

monthly_df = pd.DataFrame(monthly_data)

print("\nMonthly Sales and Expenses:")

print(monthly_df)


monthly_df.plot(
    x="Month",
    y=["Sales", "Expenses"],
    kind="line"
)

plt.title("Sales vs Expenses")

plt.xlabel("Month")

plt.ylabel("Amount")

plt.xticks(rotation=45)

plt.tight_layout()

plt.show()


# .........................DataFrame Plot.........................#

monthly_df.plot(
    x="Month",
    kind="bar"
)

plt.title("Monthly Sales and Expenses")

plt.xlabel("Month")

plt.ylabel("Amount")

plt.xticks(rotation=45)

plt.tight_layout()

plt.show()


# .........................Save Chart.........................#

monthly_df.plot(
    x="Month",
    y="Sales",
    kind="line"
)

plt.title("Monthly Sales")

plt.xlabel("Month")

plt.ylabel("Sales")

plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig(
    "monthly_sales.png"
)

plt.show()


# .........................Practical Analysis.........................#

highest_sales = df["Sales"].max()

lowest_sales = df["Sales"].min()

average_sales = df["Sales"].mean()

total_sales = df["Sales"].sum()

print("\nHighest Sales:")

print(highest_sales)


print("\nLowest Sales:")

print(lowest_sales)


print("\nAverage Sales:")

print(average_sales)


print("\nTotal Sales:")

print(total_sales)


# .........................Final Data.........................#

print("\nFinal Sales Data:")

print(df)
```
