```python
# ===================== 21_PANDAS_STRING_FUNCTIONS.py =====================


import pandas as pd


# .........................Create DataFrame.........................#

data = {
    "Name": [" Aman ", "RAHUL", "rohit", " Priya ", "NEHA"],
    "City": ["Jamshedpur", "Ranchi", "Jamshedpur", "Dhanbad", "Ranchi"],
    "Email": [
        "aman@gmail.com",
        "rahul@gmail.com",
        "rohit@gmail.com",
        "priya@gmail.com",
        "neha@gmail.com"
    ]
}

df = pd.DataFrame(data)

print("Original Data:")

print(df)


# .........................Lowercase.........................#

df["Name_Lower"] = df["Name"].str.lower()

print("\nLowercase Names:")

print(df)


# .........................Uppercase.........................#

df["Name_Upper"] = df["Name"].str.upper()

print("\nUppercase Names:")

print(df)


# .........................Title Case.........................#

df["Name_Title"] = df["Name"].str.title()

print("\nTitle Case Names:")

print(df)


# .........................Remove Extra Spaces.........................#

df["Clean_Name"] = df["Name"].str.strip()

print("\nAfter Removing Extra Spaces:")

print(df)


# .........................Left Strip.........................#

left_data = pd.Series([
    "   Aman",
    "   Rahul",
    "   Rohit"
])

print("\nLeft Strip:")

print(left_data.str.lstrip())


# .........................Right Strip.........................#

right_data = pd.Series([
    "Aman   ",
    "Rahul   ",
    "Rohit   "
])

print("\nRight Strip:")

print(right_data.str.rstrip())


# .........................String Length.........................#

df["Name_Length"] = df["Name"].str.len()

print("\nName Length:")

print(df)


# .........................Contains.........................#

print("\nNames Containing 'a':")

print(
    df[df["Name"].str.lower().str.contains("a")]
)


# .........................Starts With.........................#

print("\nNames Starting With 'A':")

print(
    df[df["Name"].str.lower().str.startswith("a")]
)


# .........................Ends With.........................#

print("\nNames Ending With 'a':")

print(
    df[df["Name"].str.lower().str.endswith("a")]
)


# .........................Replace Text.........................#

df["City_Changed"] = df["City"].str.replace(
    "Jamshedpur",
    "JAMSHEDPUR"
)

print("\nAfter Replacing City:")

print(df)


# .........................Find Text.........................#

print("\nPosition of 'a'
```
