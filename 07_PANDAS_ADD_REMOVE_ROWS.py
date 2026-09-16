```python
# ===================== 07_PANDAS_ADD_REMOVE_ROWS.py =====================


import pandas as pd


# .........................Create DataFrame.........................#

data = {
    "Name": ["Aman", "Rahul", "Rohit", "Vikas"],
    "Age": [20, 21, 19, 22],
    "Marks": [75, 82, 91, 68]
}

df = pd.DataFrame(data)

print("Original DataFrame:")

print(df)


# .........................Add One Row Using loc.........................#

df.loc[4] = ["Ankit", 20, 88]

print("\nAfter Adding One Row:")

print(df)


# .........................Add Row at Specific Index.........................#

df.loc[5] = ["Priya", 21, 94]

print("\nAfter Adding Another Row:")

print(df)


# .........................Add Row Using Dictionary.........................#

new_student = {
    "Name": "Neha",
    "Age": 20,
    "Marks": 79
}

df.loc[6] = new_student

print("\nAfter Adding Student:")

print(df)


# .........................Remove One Row Using drop.........................#

df = df.drop(6)

print("\nAfter Removing Row 6:")

print(df)


# .........................Remove Multiple Rows.........................#

df = df.drop([4, 5])

print("\nAfter Removing Multiple Rows:")

print(df)


# .........................Remove Row Using Index Position.........................#

df = df.drop(df.index[1])

print("\nAfter Removing Second Row:")

print(df)


# .........................Reset Index.........................#

df = df.reset_index(drop=True)

print("\nAfter Resetting Index:")

print(df)


# .........................Remove First Row.........................#

df = df.drop(df.index[0])

print("\nAfter Removing First Row:")

print(df)


# .........................Remove Last Row.........................#

df = df.drop(df.index[-1])

print("\nAfter Removing Last Row:")

print(df)


# .........................Reset Index Again.........................#

df = df.reset_index(drop=True)

print("\nFinal DataFrame:")

print(df)
```
