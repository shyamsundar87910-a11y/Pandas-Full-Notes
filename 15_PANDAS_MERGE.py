```python
# ===================== 15_PANDAS_MERGE.py =====================


import pandas as pd


# .........................First DataFrame.........................#

students = {
    "Student_ID": [101, 102, 103, 104],
    "Name": ["Aman", "Rahul", "Rohit", "Vikas"],
    "Age": [20, 21, 19, 22]
}

students_df = pd.DataFrame(students)

print("Students Data:")

print(students_df)


# .........................Second DataFrame.........................#

marks = {
    "Student_ID": [101, 102, 103, 105],
    "Marks": [75, 82, 91, 88]
}

marks_df = pd.DataFrame(marks)

print("\nMarks Data:")

print(marks_df)


# .........................Inner Merge.........................#

inner_merge = pd.merge(
    students_df,
    marks_df,
    on="Student_ID",
    how="inner"
)

print("\nInner Merge:")

print(inner_merge)


# .........................Left Merge.........................#

left_merge = pd.merge(
    students_df,
    marks_df,
    on="Student_ID",
    how="left"
)

print("\nLeft Merge:")

print(left_merge)


# .........................Right Merge.........................#

right_merge = pd.merge(
    students_df,
    marks_df,
    on="Student_ID",
    how="right"
)

print("\nRight Merge:")

print(right_merge)


# .........................Outer Merge.........................#

outer_merge = pd.merge(
    students_df,
    marks_df,
    on="Student_ID",
    how="outer"
)

print("\nOuter Merge:")

print(outer_merge)


# .........................Merge Using Different Column Names.........................#

student_data = {
    "ID": [101, 102, 103],
    "Name": ["Aman", "Rahul", "Rohit"]
}

marks_data = {
    "Student_ID": [101, 102, 103],
    "Marks": [75, 82, 91]
}

student_df = pd.DataFrame(student_data)

marks_df = pd.DataFrame(marks_data)

result = pd.merge(
    student_df,
    marks_df,
    left_on="ID",
    right_on="Student_ID"
)

print("\nMerge Using Different Column Names:")

print(result)


# .........................Remove Extra Column.........................#

result = result.drop(
    "Student_ID",
    axis=1
)

print("\nAfter Removing Extra Column:")

print(result)


# .........................Merge Multiple Columns.........................#

student_data = {
    "Name": ["Aman", "Rahul", "Rohit"],
    "City": ["Jamshedpur", "Ranchi", "Bokaro"],
    "Marks": [75, 82, 91]
}

attendance_data = {
    "Name": ["Aman", "Rahul", "Rohit"],
    "City": ["Jamshedpur", "Ranchi", "Bokaro"],
    "Attendance": [90, 85, 95]
}

student_df = pd.DataFrame(student_data)

attendance_df = pd.DataFrame(attendance_data)

result = pd.merge(
    student_df,
    attendance_df,
    on=["Name", "City"]
)

print("\nMerge Using Multiple Columns:")

print(result)


# .........................Merge with Suffixes.........................#

first_data = {
    "Student_ID": [101, 102, 103],
    "Name": ["Aman", "Rahul", "Rohit"],
    "Marks": [75, 82, 91]
}

second_data = {
    "Student_ID": [101, 102, 103],
    "Name": ["Aman Kumar", "Rahul Kumar", "Rohit Kumar"],
    "Marks": [80, 85, 95]
}

first_df = pd.DataFrame(first_data)

second_df = pd.DataFrame(second_data)

result = pd.merge(
    first_df,
    second_df,
    on="Student_ID",
    suffixes=("_old", "_new")
)

print("\nMerge with Suffixes:")

print(result)


# .........................Sales Data Example.........................#

products = {
    "Product_ID": [1, 2, 3, 4],
    "Product": ["Laptop", "Mobile", "Tablet", "Monitor"]
}

sales = {
    "Product_ID": [1, 2, 3, 5],
    "Sales": [50000, 30000, 20000, 15000]
}

products_df = pd.DataFrame(products)

sales_df = pd.DataFrame(sales)

sales_result = pd.merge(
    products_df,
    sales_df,
    on="Product_ID",
    how="inner"
)

print("\nProduct Sales Data:")

print(sales_result)
```
