# ===================== 02_PANDAS_SERIES.py =====================


import pandas as pd


# .........................Create Series.........................#

marks = pd.Series([65, 78, 92, 45, 88])

print(marks)


# .........................Series with Index.........................#

marks = pd.Series(
    [65, 78, 92, 45, 88],
    index=["Aman", "Rahul", "Rohit", "Vikas", "Ankit"]
)

print(marks)


# .........................Access Series Values.........................#

print("Aman Marks:", marks["Aman"])

print("Rohit Marks:", marks["Rohit"])


# .........................Access Using Position.........................#

print("First Value:", marks.iloc[0])

print("Second Value:", marks.iloc[1])


# .........................Last Value.........................#

print("Last Value:", marks.iloc[-1])


# .........................Series Slicing.........................#

print("First Three Values:")

print(marks.iloc[:3])


# .........................Series from Dictionary.........................#

student_marks = {
    "Aman": 75,
    "Rahul": 82,
    "Rohit": 91,
    "Vikas": 68
}

marks = pd.Series(student_marks)

print(marks)


# .........................Series Data Type.........................#

print("Data Type:", marks.dtype)


# .........................Series Size.........................#

print("Size:", marks.size)


# .........................Series Values.........................#

print("Values:", marks.values)


# .........................Series Index.........................#

print("Index:", marks.index)


# .........................Basic Calculations.........................#

print("Total Marks:", marks.sum())

print("Average Marks:", marks.mean())

print("Highest Marks:", marks.max())

print("Lowest Marks:", marks.min())


# .........................Filtering Series.........................#

passed = marks[marks >= 40]

print("Passed Students:")

print(passed)


# .........................Marks Greater Than 80.........................#

high_marks = marks[marks > 80]

print("Marks Greater Than 80:")

print(high_marks)


# .........................Sort Series.........................#

print("Sorted Marks:")

print(marks.sort_values())


# .........................Sort in Descending Order.........................#

print("Descending Marks:")

print(marks.sort_values(ascending=False))
