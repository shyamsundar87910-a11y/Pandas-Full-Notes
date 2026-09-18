```python
# ===================== 12_PANDAS_FILTERING.py =====================


import pandas as pd


# .........................Create DataFrame.........................#

data = {
    "Name": ["Aman", "Rahul", "Rohit", "Vikas", "Ankit", "Priya"],
    "Age": [20, 21, 19, 22, 20, 21],
    "Marks": [75, 82, 91, 68, 88, 35],
    "City": [
        "Jamshedpur",
        "Ranchi",
        "Dhanbad",
        "Bokaro",
        "Ranchi",
        "Jamshedpur"
    ]
}

df = pd.DataFrame(data)

print("Original DataFrame:")

print(df)


# .........................Marks Greater Than 80.........................#

result = df[df["Marks"] > 80]

print("\nMarks Greater Than 80:")

print(result)


# .........................Marks Greater Than or Equal to 80.........................#

result = df[df["Marks"] >= 80]

print("\nMarks Greater Than or Equal to 80:")

print(result)


# .........................Marks Less Than 50.........................#

result = df[df["Marks"] < 50]

print("\nMarks Less Than 50:")

print(result)


# .........................Marks Less Than or Equal to 70.........................#

result = df[df["Marks"] <= 70]

print("\nMarks Less Than or Equal to 70:")

print(result)


# .........................Marks Equal to 91.........................#

result = df[df["Marks"] == 91]

print("\nMarks Equal to 91:")

print(result)


# .........................Marks Not Equal to 91.........................#

result = df[df["Marks"] != 91]

print("\nMarks Not Equal to 91:")

print(result)


# .........................Age Equal to 20.........................#

result = df[df["Age"] == 20]

print("\nAge Equal to 20:")

print(result)


# .........................City Equal to Ranchi.........................#

result = df[df["City"] == "Ranchi"]

print("\nStudents from Ranchi:")

print(result)


# .........................AND Condition.........................#

result = df[
    (df["Marks"] > 70) &
    (df["Age"] < 22)
]

print("\nMarks Greater Than 70 AND Age Less Than 22:")

print(result)


# .........................OR Condition.........................#

result = df[
    (df["Marks"] > 90) |
    (df["Marks"] < 50)
]

print("\nMarks Greater Than 90 OR Less Than 50:")

print(result)


# .........................Multiple Conditions.........................#

result = df[
    (df["Marks"] >= 70) &
    (df["City"] == "Ranchi")
]

print("\nMarks >= 70 AND City is Ranchi:")

print(result)


# .........................Between Values.........................#

result = df[
    df["Marks"].between(70, 90)
]

print("\nMarks Between 70 and 90:")

print(result)


# .........................Using isin().........................#

result = df[
    df["City"].isin(["Ranchi", "Jamshedpur"])
]

print("\nStudents from Ranchi or Jamshedpur:")

print(result)


# .........................Using not isin().........................#

result = df[
    ~df["City"].isin(["Ranchi", "Jamshedpur"])
]

print("\nStudents Not from Ranchi or Jamshedpur:")

print(result)


# .........................Filter Specific Columns.........................#

result = df.loc[
    df["Marks"] > 80,
    ["Name", "Marks"]
]

print("\nName and Marks Greater Than 80:")

print(result)


# .........................Filter Passed Students.........................#

passed_students = df[
    df["Marks"] >= 40
]

print("\nPassed Students:")

print(passed_students)


# .........................Filter Failed Students.........................#

failed_students = df[
    df["Marks"] < 40
]

print("\nFailed Students:")

print(failed_students)


# .........................Filter Top Students.........................#

top_students = df[
    df["Marks"] >= 85
]

print("\nTop Students:")

print(top_students)


# .........................Filter by Name.........................#

result = df[
    df["Name"] == "Aman"
]

print("\nAman Data:")

print(result)
```
