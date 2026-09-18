```python
# ===================== 11_PANDAS_SORTING.py =====================


import pandas as pd


# .........................Create DataFrame.........................#

data = {
    "Name": ["Aman", "Rahul", "Rohit", "Vikas", "Ankit"],
    "Age": [20, 21, 19, 22, 20],
    "Marks": [75, 82, 91, 68, 88],
    "City": ["Jamshedpur", "Ranchi", "Dhanbad", "Bokaro", "Ranchi"]
}

df = pd.DataFrame(data)

print("Original DataFrame:")

print(df)


# .........................Sort by One Column.........................#

sorted_marks = df.sort_values("Marks")

print("\nSorted by Marks:")

print(sorted_marks)


# .........................Sort in Descending Order.........................#

sorted_marks = df.sort_values(
    "Marks",
    ascending=False
)

print("\nMarks in Descending Order:")

print(sorted_marks)


# .........................Sort by Age.........................#

sorted_age = df.sort_values("Age")

print("\nSorted by Age:")

print(sorted_age)


# .........................Sort by Name.........................#

sorted_name = df.sort_values("Name")

print("\nSorted by Name:")

print(sorted_name)


# .........................Sort Name in Descending Order.........................#

sorted_name = df.sort_values(
    "Name",
    ascending=False
)

print("\nName in Descending Order:")

print(sorted_name)


# .........................Sort by Multiple Columns.........................#

sorted_data = df.sort_values(
    ["Age", "Marks"]
)

print("\nSorted by Age and Marks:")

print(sorted_data)


# .........................Multiple Columns with Different Order.........................#

sorted_data = df.sort_values(
    ["Age", "Marks"],
    ascending=[True, False]
)

print("\nAge Ascending and Marks Descending:")

print(sorted_data)


# .........................Sort Index.........................#

sorted_index = df.sort_index()

print("\nSorted by Index:")

print(sorted_index)


# .........................Sort Index in Descending Order.........................#

sorted_index = df.sort_index(
    ascending=False
)

print("\nIndex in Descending Order:")

print(sorted_index)


# .........................Reset Index After Sorting.........................#

sorted_data = df.sort_values(
    "Marks",
    ascending=False
)

sorted_data = sorted_data.reset_index(
    drop=True
)

print("\nAfter Sorting and Resetting Index:")

print(sorted_data)


# .........................Highest Marks Student.........................#

top_student = df.sort_values(
    "Marks",
    ascending=False
).iloc[0]

print("\nTop Student:")

print(top_student)


# .........................Top Three Students.........................#

top_three = df.sort_values(
    "Marks",
    ascending=False
).head(3)

print("\nTop Three Students:")

print(top_three)


# .........................Lowest Three Students.........................#

lowest_three = df.sort_values(
    "Marks"
).head(3)

print("\nLowest Three Students:")

print(lowest_three)


# .........................Sort and Select Column.........................#

sorted_names = df.sort_values(
    "Marks",
    ascending=False
)["Name"]

print("\nStudents by Marks:")

print(sorted_names)
```
