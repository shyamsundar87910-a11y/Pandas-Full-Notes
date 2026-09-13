```python
# ===================== 05_PANDAS_INDEXING.py =====================


import pandas as pd


# .........................Create DataFrame.........................#

data = {
    "Name": ["Aman", "Rahul", "Rohit", "Vikas", "Ankit"],
    "Age": [20, 21, 19, 22, 20],
    "Marks": [75, 82, 91, 68, 88]
}

df = pd.DataFrame(data)

print(df)


# .........................Select One Column.........................#

print("Name Column:")

print(df["Name"])


# .........................Select Multiple Columns.........................#

print("Name and Marks:")

print(df[["Name", "Marks"]])


# .........................Select First Row Using iloc.........................#

print("First Row:")

print(df.iloc[0])


# .........................Select Second Row.........................#

print("Second Row:")

print(df.iloc[1])


# .........................Select Last Row.........................#

print("Last Row:")

print(df.iloc[-1])


# .........................Select Multiple Rows.........................#

print("First Three Rows:")

print(df.iloc[:3])


# .........................Select Specific Rows.........................#

print("First and Third Row:")

print(df.iloc[[0, 2]])


# .........................Select Row and Column.........................#

print("First Row Marks:")

print(df.iloc[0, 2])


# .........................Select Specific Rows and Columns.........................#

print("First Two Students Name and Marks:")

print(df.iloc[:2, [0, 2]])


# .........................Using loc.........................#

print("First Row Using loc:")

print(df.loc[0])


# .........................Using loc for Columns.........................#

print("Names and Marks Using loc:")

print(df.loc[:, ["Name", "Marks"]])


# .........................Using loc for Specific Rows.........................#

print("First Three Rows Using loc:")

print(df.loc[0:2])


# .........................Conditional Indexing.........................#

print("Students with Marks Greater Than 80:")

print(df[df["Marks"] > 80])


# .........................Multiple Conditions.........................#

print("Students with Marks Greater Than 70 and Age Less Than 22:")

print(df[(df["Marks"] > 70) & (df["Age"] < 22)])


# .........................OR Condition.........................#

print("Students with Marks Less Than 70 or Age Greater Than 21:")

print(df[(df["Marks"] < 70) | (df["Age"] > 21)])


# .........................Index Based Selection.........................#

print("Third Student Name:")

print(df.iloc[2]["Name"])


# .........................Specific Cell Using loc.........................#

print("Rahul Marks:")

print(df.loc[1, "Marks"])
```
