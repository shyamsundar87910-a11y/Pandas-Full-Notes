```python
# ===================== 16_PANDAS_JOIN.py =====================


import pandas as pd


# .........................First DataFrame.........................#

students = {
    "Name": ["Aman", "Rahul", "Rohit", "Vikas"],
    "Marks": [75, 82, 91, 68]
}

students_df = pd.DataFrame(
    students,
    index=[101, 102, 103, 104]
)

print("Students Data:")

print(students_df)


# .........................Second DataFrame.........................#

attendance = {
    "Attendance": [90, 85, 95, 80]
}

attendance_df = pd.DataFrame(
    attendance,
    index=[101, 102, 103, 104]
)

print("\nAttendance Data:")

print(attendance_df)


# .........................Join DataFrames.........................#

result = students_df.join(attendance_df)

print("\nJoined Data:")

print(result)


# .........................Join with Different Index.........................#

marks = {
    "Marks": [75, 82, 91]
}

marks_df = pd.DataFrame(
    marks,
    index=[101, 102, 105]
)

print("\nMarks Data:")

print(marks_df)


# .........................Left Join.........................#

left_join = students_df.join(
    marks_df,
    how="left",
    lsuffix="_student",
    rsuffix="_marks"
)

print("\nLeft Join:")

print(left_join)


# .........................Right Join.........................#

right_join = students_df.join(
    marks_df,
    how="right",
    lsuffix="_student",
    rsuffix="_marks"
)

print("\nRight Join:")

print(right_join)


# .........................Outer Join.........................#

outer_join = students_df.join(
    marks_df,
    how="outer",
    lsuffix="_student",
    rsuffix="_marks"
)

print("\nOuter Join:")

print(outer_join)


# .........................Inner Join.........................#

inner_join = students_df.join(
    marks_df,
    how="inner",
    lsuffix="_student",
    rsuffix="_marks"
)

print("\nInner Join:")

print(inner_join)


# .........................Join Using lsuffix and rsuffix.........................#

first_data = {
    "Name": ["Aman", "Rahul", "Rohit"],
    "Marks": [75, 82, 91]
}

second_data = {
    "Name": ["Aman", "Rahul", "Rohit"],
    "Marks": [80, 85, 95]
}

first_df = pd.DataFrame(
    first_data,
    index=[101, 102, 103]
)

second_df = pd.DataFrame(
    second_data,
    index=[101, 102, 103]
)

result = first_df.join(
    second_df,
    lsuffix="_first",
    rsuffix="_second"
)

print("\nJoin with Same Column Names:")

print(result)


# .........................Join Series.........................#

attendance = pd.Series(
    [90, 85, 95, 80],
    index=[101, 102, 103, 104],
    name="Attendance"
)

result = students_df.join(attendance)

print("\nJoin DataFrame with Series:")

print(result)


# .........................Student Performance Example.........................#

student_data = {
    "Name": ["Aman", "Rahul", "Rohit", "Vikas"],
    "Marks": [75, 82, 91, 68]
}

attendance_data = {
    "Attendance": [90, 85, 95, 80]
}

student_df = pd.DataFrame(
    student_data,
    index=[101, 102, 103, 104]
)

attendance_df = pd.DataFrame(
    attendance_data,
    index=[101, 102, 103, 104]
)

performance = student_df.join(
    attendance_df
)

print("\nStudent Performance:")

print(performance)


# .........................Filter Good Attendance.........................#

good_attendance = performance[
    performance["Attendance"] >= 90
]

print("\nStudents with Good Attendance:")

print(good_attendance)
```
