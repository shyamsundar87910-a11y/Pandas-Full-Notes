```python
# ===================== 25_PANDAS_WITH_NUMPY.py =====================


import pandas as pd
import numpy as np


# .........................Create NumPy Array.........................#

marks = np.array([
    75,
    82,
    91,
    68,
    88
])

print("NumPy Array:")

print(marks)


# .........................Create DataFrame from NumPy Array.........................#

df = pd.DataFrame({
    "Marks": marks
})

print("\nDataFrame:")

print(df)


# .........................NumPy Mean.........................#

average = np.mean(
    df["Marks"]
)

print("\nAverage Marks:")

print(average)


# .........................NumPy Maximum.........................#

highest = np.max(
    df["Marks"]
)

print("\nHighest Marks:")

print(highest)


# .........................NumPy Minimum.........................#

lowest = np.min(
    df["Marks"]
)

print("\nLowest Marks:")

print(lowest)


# .........................NumPy Sum.........................#

total = np.sum(
    df["Marks"]
)

print("\nTotal Marks:")

print(total)


# .........................NumPy Standard Deviation.........................#

standard_deviation = np.std(
    df["Marks"]
)

print("\nStandard Deviation:")

print(standard_deviation)


# .........................NumPy Square Root.........................#

df["Square_Root"] = np.sqrt(
    df["Marks"]
)

print("\nSquare Root:")

print(df)


# .........................NumPy Power.........................#

df["Marks_Squared"] = np.power(
    df["Marks"],
    2
)

print("\nMarks Squared:")

print(df)


# .........................NumPy Round.........................#

df["Rounded"] = np.round(
    df["Square_Root"],
    2
)

print("\nRounded Values:")

print(df)


# .........................NumPy Absolute Value.........................#

numbers = pd.Series([
    -10,
    -5,
    0,
    5,
    10
])

absolute_values = np.abs(
    numbers
)

print("\nAbsolute Values:")

print(absolute_values)


# .........................NumPy Conditions.........................#

df["Result"] = np.where(
    df["Marks"] >= 40,
    "Pass",
    "Fail"
)

print("\nResult:")

print(df)


# .........................NumPy Multiple Conditions.........................#

df["Grade"] = np.select(
    [
        df["Marks"] >= 80,
        df["Marks"] >= 60,
        df["Marks"] >= 40
    ],
    [
        "A",
        "B",
        "C"
    ],
    default="Fail"
)

print("\nGrade:")

print(df)


# .........................Create DataFrame with Random Values.........................#

random_numbers = np.random.randint(
    1,
    101,
    size=5
)

random_df = pd.DataFrame({
    "Random_Number": random_numbers
})

print("\nRandom Data:")

print(random_df)


# .........................Random Student Data.........................#

student_data = pd.DataFrame({
    "Name": [
        "Aman",
        "Rahul",
        "Rohit",
        "Priya",
        "Neha"
    ],
    "Marks": np.random.randint(
        40,
        101,
        size=5
    )
})

print("\nRandom Student Marks:")

print(student_data)


# .........................NumPy Median.........................#

median_marks = np.median(
    student_data["Marks"]
)

print("\nMedian Marks:")

print(median_marks)


# .........................NumPy Percentile.........................#

percentile_75 = np.percentile(
    student_data["Marks"],
    75
)

print("\n75th Percentile:")

print(percentile_75)


# .........................NumPy Sorting.........................#

sorted_marks = np.sort(
    student_data["Marks"]
)

print("\nSorted Marks:")

print(sorted_marks)


# .........................NumPy Unique Values.........................#

values = np.array([
    10,
    20,
    10,
    30,
    20,
    40
])

unique_values = np.unique(
    values
)

print("\nUnique Values:")

print(unique_values)


# .........................NumPy Random Sales Data.........................#

sales = pd.DataFrame({
    "Product": [
        "Laptop",
        "Mobile",
        "Tablet",
        "Monitor",
        "Keyboard"
    ],
    "Sales": np.random.randint(
        5000,
        60000,
        size=5
    )
})

print("\nSales Data:")

print(sales)


# .........................Sales Category.........................#

sales["Category"] = np.where(
    sales["Sales"] >= 30000,
    "High",
    "Low"
)

print("\nSales Category:")

print(sales)


# .........................Sales Tax.........................#

sales["Tax"] = np.round(
    sales["Sales"] * 0.18,
    2
)

print("\nSales Tax:")

print(sales)


# .........................Final Sales Amount.........................#

sales["Final_Amount"] = (
    sales["Sales"] + sales["Tax"]
)

print("\nFinal Sales Amount:")

print(sales)


# .........................Pandas and NumPy Statistics.........................#

print("\nSales Average:")

print(
    np.mean(sales["Sales"])
)


print("\nHighest Sales:")

print(
    np.max(sales["Sales"])
)


print("\nLowest Sales:")

print(
    np.min(sales["Sales"])
)


print("\nTotal Sales:")

print(
    np.sum(sales["Sales"])
)


# .........................Final Data.........................#

print("\nFinal Student Data:")

print(student_data)


print("\nFinal Sales Data:")

print(sales)
```
