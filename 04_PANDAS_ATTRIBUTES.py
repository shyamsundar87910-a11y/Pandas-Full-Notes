```python
# ===================== 04_PANDAS_ATTRIBUTES.py =====================


import pandas as pd


# .........................Create DataFrame.........................#

data = {
    "Name": ["Aman", "Rahul", "Rohit", "Vikas"],
    "Age": [20, 21, 19, 22],
    "Marks": [75, 82, 91, 68]
}

df = pd.DataFrame(data)

print(df)


# .........................Shape.........................#

print("Shape:", df.shape)


# .........................Rows.........................#

print("Number of Rows:", df.shape[0])


# .........................Columns.........................#

print("Number of Columns:", df.shape[1])


# .........................Columns Names.........................#

print("Columns:", df.columns)


# .........................Index.........................#

print("Index:", df.index)


# .........................Data Types.........................#

print("Data Types:")

print(df.dtypes)


# .........................Size.........................#

print("Size:", df.size)


# .........................Values.........................#

print("Values:")

print(df.values)


# .........................Number of Dimensions.........................#

print("Dimensions:", df.ndim)


# .........................Information.........................#

print("Information:")

df.info()


# .........................Statistics.........................#

print("Statistics:")

print(df.describe())


# .........................Check Data Types.........................#

print("Name Data Type:", df["Name"].dtype)

print("Age Data Type:", df["Age"].dtype)

print("Marks Data Type:", df["Marks"].dtype)


# .........................First Rows.........................#

print("First Rows:")

print(df.head())


# .........................Last Rows.........................#

print("Last Rows:")

print(df.tail())
```
