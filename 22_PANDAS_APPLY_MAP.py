```python
# ===================== 22_PANDAS_APPLY_MAP.py =====================


import pandas as pd


# .........................Create DataFrame.........................#

data = {
    "Name": ["Aman", "Rahul", "Rohit", "Priya", "Neha"],
    "Marks": [75, 82, 91, 68, 88],
    "Age": [20, 21, 19, 22, 20]
}

df = pd.DataFrame(data)

print("Original Data:")

print(df)


# .........................Apply on Column.........................#

df["Marks_Double"] = df["Marks"].apply(
    lambda x: x * 2
)

print("\nDouble Marks:")

print(df)


# .........................Apply with Lambda.........................#

df["Bonus_Marks"] = df["Marks"].apply(
    lambda x: x + 5
)

print("\nBonus Marks:")

print(df)


# .........................Apply Condition.........................#

df["Result"] = df["Marks"].apply(
    lambda x: "Pass" if x >= 40 else "Fail"
)

print("\nResult:")

print(df)


# .........................Apply Grade.........................#

df["Grade"] = df["Marks"].apply(
    lambda x:
        "A" if x >= 80
        else "B" if x >= 60
        else "C"
)

print("\nGrade:")

print(df)


# .........................Custom Function.........................#

def check_marks(marks):

    if marks >= 80:
        return "Excellent"

    elif marks >= 60:
        return "Good"

    else:
        return "Needs Improvement"


df["Performance"] = df["Marks"].apply(
    check_marks
)

print("\nPerformance:")

print(df)


# .........................Apply on Multiple Columns.........................#

df["Total"] = df.apply(
    lambda row: row["Marks"] + row["Bonus_Marks"],
    axis=1
)

print("\nTotal Marks:")

print(df)


# .........................Apply on Rows.........................#

df["Student_Info"] = df.apply(
    lambda row: row["Name"] + " - " + str(row["Marks"]),
    axis=1
)

print("\nStudent Information:")

print(df)


# .........................Apply Function to Entire DataFrame.........................#

numbers = pd.DataFrame({
    "A": [10, 20, 30],
    "B": [40, 50, 60]
})

result = numbers.apply(
    lambda x: x + 5
)

print("\nAdd 5 to All Values:")

print(result)


# .........................Apply Sum by Column.........................#

column_sum = numbers.apply(
    sum
)

print("\nColumn Sum:")

print(column_sum)


# .........................Apply Sum by Row.........................#

row_sum = numbers.apply(
    sum,
    axis=1
)

prin
```
