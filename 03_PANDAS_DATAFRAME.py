# ===================== 03_PANDAS_DATAFRAME.py =====================


import pandas as pd


# .........................Create DataFrame from Dictionary.........................#

data = {
    "Name": ["Aman", "Rahul", "Rohit", "Vikas"],
    "Age": [20, 21, 19, 22],
    "Marks": [75, 82, 91, 68]
}

df = pd.DataFrame(data)

print(df)


# .........................Create DataFrame from List.........................#

data = [
    ["Aman", 20, 75],
    ["Rahul", 21, 82],
    ["Rohit", 19, 91],
    ["Vikas", 22, 68]
]

df = pd.DataFrame(
    data,
    columns=["Name", "Age", "Marks"]
)

print(df)


# .........................Create Empty DataFrame.........................#

empty_df = pd.DataFrame()

print(empty_df)


# .........................Display DataFrame.........................#

print("Student Data:")

print(df)


# .........................Display First Rows.........................#

print("First 2 Rows:")

print(df.head(2))


# .........................Display Last Rows.........................#

print("Last 2 Rows:")

print(df.tail(2))


# .........................Select One Column.........................#

print("Names:")

print(df["Name"])


# .........................Select Multiple Columns.........................#

print("Name and Marks:")

print(df[["Name", "Marks"]])


# .........................Select First Row.........................#

print("First Row:")

print(df.iloc[0])


# .........................Select Specific Row.........................#

print("Second Row:")

print(df.iloc[1])


# .........................Select Rows and Columns.........................#

print("First Two Students:")

print(df.iloc[:2, :2])


# .........................Add New Column.........................#

df["City"] = ["Jamshedpur", "Ranchi", "Dhanbad", "Bokaro"]

print("DataFrame after adding City:")

print(df)


# .........................Calculate Average Marks.........................#

average_marks = df["Marks"].mean()

print("Average Marks:", average_marks)


# .........................Highest Marks.........................#

highest_marks = df["Marks"].max()

print("Highest Marks:", highest_marks)


# .........................Lowest Marks.........................#

lowest_marks = df["Marks"].min()

print("Lowest Marks:", lowest_marks)


# .........................Filter Students.........................#

passed_students = df[df["Marks"] >= 40]

print("Passed Students:")

print(passed_students)


# .........................Filter High Marks.........................#

high_marks = df[df["Marks"] > 80]

print("Students with Marks Greater Than 80:")

print(high_marks)
```
