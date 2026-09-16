```python
# ===================== 06_PANDAS_ADD_REMOVE_COLUMNS.py =====================


import pandas as pd


# .........................Create DataFrame.........................#

data = {
    "Name": ["Aman", "Rahul", "Rohit", "Vikas"],
    "Age": [20, 21, 19, 22],
    "Marks": [75, 82, 91, 68]
}

df = pd.DataFrame(data)

print("Original DataFrame:")

print(df)


# .........................Add One Column.........................#

df["City"] = ["Jamshedpur", "Ranchi", "Dhanbad", "Bokaro"]

print("\nAfter Adding City:")

print(df)


# .........................Add Column with Same Value.........................#

df["Course"] = "BCA"

print("\nAfter Adding Course:")

print(df)


# .........................Add Column Using Calculation.........................#

df["Marks_10"] = df["Marks"] / 10

print("\nAfter Adding Marks_10:")

print(df)


# .........................Add Column Using Condition.........................#

df["Result"] = df["Marks"] >= 40

print("\nAfter Adding Result:")

print(df)


# .........................Insert Column.........................#

df.insert(1, "Roll_No", [101, 102, 103, 104])

print("\nAfter Inserting Roll_No:")

print(df)


# .........................Remove One Column.........................#

df = df.drop("Course", axis=1)

print("\nAfter Removing Course:")

print(df)


# .........................Remove Multiple Columns.........................#

df = df.drop(["Marks_10", "Result"], axis=1)

print("\nAfter Removing Multiple Columns:")

print(df)


# .........................Remove Column Using del.........................#

del df["City"]

print("\nAfter Removing City:")

print(df)


# .........................Remove Column Using pop.........................#

removed_column = df.pop("Age")

print("\nRemoved Age Column:")

print(removed_column)

print("\nDataFrame After pop:")

print(df)


# .........................Rename Column.........................#

df = df.rename(columns={"Name": "Student_Name"})

print("\nAfter Renaming Column:")

print(df)


# .........................Final DataFrame.........................#

print("\nFinal DataFrame:")

print(df)
```
