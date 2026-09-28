```python
# ===================== 28_PANDAS_PRACTICE_QUESTIONS.py =====================


import pandas as pd


# .........................Create Dataset.........................#

data = {
    "Name": [
        "Aman",
        "Rahul",
        "Priya",
        "Sneha",
        "Rohit",
        "Ankit",
        "Neha",
        "Pooja",
        "Vikas",
        "Riya"
    ],
    "Age": [
        20,
        21,
        19,
        22,
        20,
        21,
        19,
        22,
        20,
        21
    ],
    "City": [
        "Jamshedpur",
        "Ranchi",
        "Jamshedpur",
        "Dhanbad",
        "Ranchi",
        "Jamshedpur",
        "Dhanbad",
        "Ranchi",
        "Jamshedpur",
        "Dhanbad"
    ],
    "Marks": [
        78,
        85,
        92,
        67,
        74,
        88,
        95,
        69,
        81,
        73
    ],
    "Attendance": [
        85,
        90,
        95,
        72,
        80,
        88,
        96,
        75,
        84,
        78
    ]
}

df = pd.DataFrame(data)


print("Original Dataset:")

print(df)


# .........................Question 1 - Display First 5 Rows.........................#

print("\nQuestion 1 - First 5 Rows:")

print(df.head())


# .........................Question 2 - Display Last 3 Rows.........................#

print("\nQuestion 2 - Last 3 Rows:")

print(df.tail(3))


# .........................Question 3 - Find Shape.........................#

print("\nQuestion 3 - Shape:")

print(df.shape)


# .........................Question 4 - Select Specific Columns.........................#

print("\nQuestion 4 - Name and Marks:")

print(df[["Name", "Marks"]])


# .........................Question 5 - Filter Students with Marks Greater Than 80.........................#

print("\nQuestion 5 - Marks Greater Than 80:")

high_marks = df[
    df["Marks"] > 80
]

print(high_marks)


# .........................Question 6 - Filter Students from Jamshedpur.........................#

print("\nQuestion 6 - Jamshedpur Students:")

jamshedpur_students = df[
    df["City"] == "Jamshedpur"
]

print(jamshedpur_students)


# .........................Question 7 - Multiple Conditions.........................#

print("\nQuestion 7 - Marks Greater Than 80 and Attendance Greater Than 85:")

good_students = df[
    (df["Marks"] > 80) &
    (df["Attendance"] > 85)
]

print(good_students)


# .........................Question 8 - Sort by Marks.........................#

print("\nQuestion 8 - Students Sorted by Marks:")

sorted_marks = df.sort_values(
    "Marks",
    ascending=False
)

print(sorted_marks)


# .........................Question 9 - Find Highest Marks.........................#

highest_marks = df["Marks"].max()

print("\nQuestion 9 - Highest Marks:")

print(highest_marks)


# .........................Question 10 - Find Lowest Marks.........................#

lowest_marks = df["Marks"].min()

print("\nQuestion 10 - Lowest Marks:")

print(lowest_marks)


# .........................Question 11 - Find Average Marks.........................#

average_marks = df["Marks"].mean()

print("\nQuestion 11 - Average Marks:")

print(round(average_marks, 2))


# .........................Question 12 - Find Top 3 Students.........................#

top_3 = df.nlargest(
    3,
    "Marks"
)

print("\nQuestion 12 - Top 3 Students:")

print(top_3)


# .........................Question 13 - Add Result Column.........................#

df["Result"] = df["Marks"].apply(
    lambda x:
        "Pass" if x >= 40
        else "Fail"
)

print("\nQuestion 13 - Result Column:")

print(df)


# .........................Question 14 - Add Grade Column.........................#

def get_grade(marks):

    if marks >= 90:
        return "A"

    elif marks >= 80:
        return "B"

    elif marks >= 70:
        return "C"

    elif marks >= 60:
        return "D"

    else:
        return "F"


df["Grade"] = df["Marks"].apply(
    get_grade
)

print("\nQuestion 14 - Grade Column:")

print(df)


# .........................Question 15 - Count Students by City.........................#

city_count = df["City"].value_counts()

print("\nQuestion 15 - Students by City:")

print(city_count)


# .........................Question 16 - Average Marks by City.........................#

average_city_marks = df.groupby(
    "City"
)["Marks"].mean()

print("\nQuestion 16 - Average Marks by City:")

print(average_city_marks)


# .........................Question 17 - Highest Marks by City.........................#

highest_city_marks = df.groupby(
    "City"
)["Marks"].max()

print("\nQuestion 17 - Highest Marks by City:")

print(highest_city_marks)


# .........................Question 18 - Average Attendance.........................#

average_attendance = df["Attendance"].mean()

print("\nQuestion 18 - Average Attendance:")

print(round(average_attendance, 2))


# .........................Question 19 - Students with Attendance Below 80.........................#

low_attendance = df[
    df["Attendance"] < 80
]

print("\nQuestion 19 - Attendance Below 80:")

print(low_attendance)


# .........................Question 20 - Create Performance Category.........................#

df["Performance"] = df["Marks"].apply(
    lambda x:
        "Excellen
```
