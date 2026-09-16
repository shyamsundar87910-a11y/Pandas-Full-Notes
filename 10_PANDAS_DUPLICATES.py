```python
# ===================== 10_PANDAS_DUPLICATES.py =====================


import pandas as pd


# .........................Create DataFrame.........................#

data = {
    "Name": [
        "Aman",
        "Rahul",
        "Rohit",
        "Aman",
        "Vikas",
        "Rahul"
    ],
    "Age": [20, 21, 19, 20, 22, 21],
    "Marks": [75, 82, 91, 75, 68, 82]
}

df = pd.DataFrame(data)

print("Original DataFrame:")

print(df)


# .........................Check Duplicate Rows.........................#

print("\nDuplicate Rows:")

print(df.duplicated())


# .........................Count Duplicate Rows.........................#

print("\nNumber of Duplicate Rows:")

print(df.duplicated().sum())


# .........................Display Duplicate Rows.........................#

duplicates = df[df.duplicated()]

print("\nDuplicate Rows:")

print(duplicates)


# .........................Keep First Duplicate.........................#

print("\nKeep First Duplicate:")

print(df.duplicated(keep="first"))


# .........................Keep Last Duplicate.........................#

print("\nKeep Last Duplicate:")

print(df.duplicated(keep="last"))


# .........................Mark All Duplicates.........................#

print("\nMark All Duplicates:")

print(df.duplicated(keep=False))


# .........................Remove Duplicate Rows.........................#

clean_df = df.drop_duplicates()

print("\nAfter Removing Duplicates:")

print(clean_df)


# .........................Remove Duplicates from Specific Column.........................#

data = {
    "Name": ["Aman", "Rahul", "Aman", "Rohit", "Rahul"],
    "Age": [20, 21, 22, 19, 23],
    "Marks": [75, 82, 90, 91, 88]
}

df = pd.DataFrame(data)

print("\nNew DataFrame:")

print(df)


# .........................Check Duplicate Names.........................#

print("\nDuplicate Names:")

print(df.duplicated(subset=["Name"]))


# .........................Display Duplicate Names.........................#

duplicate_names = df[df.duplicated(subset=["Name"], keep=False)]

print("\nStudents with Duplicate Names:")

print(duplicate_names)


# .........................Remove Duplicate Names.........................#

unique_names = df.drop_duplicates(
    subset=["Name"]
)

print("\nAfter Removing Duplicate Names:")

print(unique_names)


# .........................Keep Last Duplicate Name.........................#

last_names = df.drop_duplicates(
    subset=["Name"],
    keep="last"
)

print("\nKeep Last Duplicate Name:")

print(last_names)


# .........................Remove All Duplicate Names.........................#

unique_only = df[
    ~df.duplicated(
        subset=["Name"],
        keep=False
    )
]

print("\nOnly Unique Names:")

print(unique_only)


# .........................Reset Index.........................#

unique_names = unique_names.reset_index(drop=True)

print("\nAfter Resetting Index:")

print(unique_names)


# .........................Final DataFrame.........................#

print("\nFinal DataFrame:")

print(unique_names)
```
