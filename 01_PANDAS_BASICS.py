# ===================== 01_PANDAS_BASICS.py =====================


import pandas as pd


# .........................Check Pandas Version.........................#

print("Pandas Version:", pd.__version__)


# .........................Create Series.........................#

marks = pd.Series([65, 78, 92, 45, 88])

print(marks)


# .........................Create Series with Index.........................#

marks = pd.Series(
    [65, 78, 92, 45, 88],
    index=["Aman", "Rahul", "Rohit", "Vikas", "Ankit"]
)

print(marks)


# .........................Access Series Data.........................#

print("Aman Marks:", marks["Aman"])

print("Rohit Marks:", marks["Rohit"])


# .........................Create DataFrame.........................#

data = {
    "Name": ["Aman", "Rahul", "Rohit", "Vikas"],
    "Age": [20, 21, 19, 22],
    "Marks": [75, 82, 91, 68]
}

df = pd.DataFrame(data)

print(df)


# .........................Display Columns.........................#

print("Names:")

print(df["Name"])


print("Marks:")

print(df["Marks"])


# .........................Display First Rows.........................#

print("First Rows:")

print(df.head())


# .........................Display Last Rows.........................#

print("Last Rows:")

print(df.tail())


# .........................Basic Information.........................#

print("DataFrame Information:")

print(df.info())


# .........................DataFrame Shape.........................#

print("Shape:", df.shape)


# .........................DataFrame Columns.........................#

print("Columns:", df.columns)


# .........................DataFrame Index.........................#

print("Index:", df.index)


# .........................Basic Statistics.........................#

print("Statistics:")

print(df.describe())


# .........................Marks Analysis.........................#

print("Average Marks:", df["Marks"].mean())

print("Highest Marks:", df["Marks"].max())

print("Lowest Marks:", df["Marks"].min())


# .........................Filtering Data.........................#

passed_students = df[df["Marks"] >= 40]

print("Passed Students:")

print(passed_students)
