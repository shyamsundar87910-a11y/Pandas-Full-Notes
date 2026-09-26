```python
# ===================== 24_PANDAS_STATISTICAL_ANALYSIS.py =====================


import pandas as pd


# .........................Create DataFrame.........................#

data = {
    "Name": ["Aman", "Rahul", "Rohit", "Priya", "Neha", "Vikas"],
    "Age": [20, 21, 19, 22, 20, 21],
    "Marks": [75, 82, 91, 68, 88, 79],
    "Study_Hours": [3, 4, 5, 2, 5, 4]
}

df = pd.DataFrame(data)

print("Student Data:")

print(df)


# .........................Count.........................#

print("\nCount:")

print(df["Marks"].count())


# .........................Sum.........................#

print("\nTotal Marks:")

print(df["Marks"].sum())


# .........................Mean.........................#

print("\nAverage Marks:")

print(df["Marks"].mean())


# .........................Median.........................#

print("\nMedian Marks:")

print(df["Marks"].median())


# .........................Mode.........................#

print("\nMode of Marks:")

print(df["Marks"].mode())


# .........................Minimum.........................#

print("\nMinimum Marks:")

print(df["Marks"].min())


# .........................Maximum.........................#

print("\nMaximum Marks:")

print(df["Marks"].max())


# .........................Range.........................#

marks_range = (
    df["Marks"].max() -
    df["Marks"].min()
)

print("\nMarks Range:")

print(marks_range)


# .........................Standard Deviation.........................#

print("\nStandard Deviation:")

print(df["Marks"].std())


# .........................Variance.........................#

print("\nVariance:")

print(df["Marks"].var())


# .........................Quantile.........................#

print("\n25% Quantile:")

print(df["Marks"].quantile(0.25))


print("\n50% Quantile:")

print(df["Marks"].quantile(0.50))


print("\n75% Quantile:")

print(df["Marks"].quantile(0.75))


# .........................Describe.........................#

print("\nStatistical Summary:")

print(df.describe())


# .........................Describe Specific Column.........................#

print("\nMarks Statistics:")

print(df["Marks"].describe())


# .........................Correlation.........................#

print("\nCorrelation:")

print(
    df[["Marks", "Study_Hours"]].corr()
)


# .........................Correlation Between Two Columns.........................#

correlation = df["Marks"].corr(
    df["Study_Hours"]
)

print("\nMarks and S
```
