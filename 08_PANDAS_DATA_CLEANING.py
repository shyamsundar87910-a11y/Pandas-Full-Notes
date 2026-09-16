```python
# ===================== 08_PANDAS_DATA_CLEANING.py =====================


import pandas as pd


# .........................Create DataFrame.........................#

data = {
    "Name": ["Aman", "Rahul", "Rohit", "Vikas", "Ankit"],
    "Age": [20, 21, None, 22, 20],
    "City": ["Jamshedpur", "Ranchi", "Jamshedpur", None, "Ranchi"],
    "Marks": [75, 82, 91, None, 88]
}

df = pd.DataFrame(data)

print("Original DataFrame:")

print(df)


# .........................Check Missing Values.........................#

print("\nMissing Values:")

print(df.isnull())


# .........................Count Missing Values.........................#

print("\nMissing Value Count:")

print(df.isnull().sum())


# .........................Remove Missing Rows.........................#

clean_df = df.dropna()

print("\nAfter Removing Missing Rows:")

print(clean_df)


# .........................Fill Missing Values.........................#

df["Age"] = df["Age"].fillna(20)

df["Marks"] = df["Marks"].fillna(0)

df["City"] = df["City"].fillna("Unknown")

print("\nAfter Filling Missing Values:")

print(df)


# .........................Remove Duplicate Rows.........................#

data = {
    "Name": ["Aman", "Rahul", "Aman", "Rohit"],
    "Age": [20, 21, 20, 19],
    "Marks": [75, 82, 75, 91]
}

df = pd.DataFrame(data)

print("\nData with Duplicate Rows:")

print(df)


df = df.drop_duplicates()

print("\nAfter Removing Duplicate Rows:")

print(df)


# .........................Rename Columns.........................#

df = df.rename(
    columns={
        "Name": "Student_Name",
        "Marks": "Student_Marks"
    }
)

print("\nAfter Renaming Columns:")

print(df)


# .........................Change Data Type.........................#

df["Age"] = df["Age"].astype(int)

print("\nAge Data Type:")

print(df["Age"].dtype)


# .........................Clean Text Data.........................#

data = {
    "Name": [" Aman ", " Rahul ", " Rohit "],
    "City": ["Jamshedpur", " RANCHI ", "Dhanbad"]
}

df = pd.DataFrame(data)

print("\nBefore Cleaning Text:")

print(df)


df["Name"] = df["Name"].str.strip()

df["City"] = df["City"].str.strip()

print("\nAfter Removing Extra Spaces:")

print(df)


# .........................Convert Text to Lowercase.........................#

df["City"] = df["City"].str.lower()

print("\nCity in Lowercase:")

print(df)


# .........................Convert Text to Uppercase.........................#

df["Name"] = df["Name"].str.upper()

print("\nName in Uppercase:")

print(df)


# .........................Replace Values.........................#

df["City"] = df["City"].replace("ranchi", "ranchi city")

print("\nAfter Replacing Value:")

print(df)


# .........................Final DataFrame.........................#

print("\nFinal Clean Data:")

print(df)
```
