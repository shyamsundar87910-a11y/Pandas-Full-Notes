```python
# ===================== 09_PANDAS_MISSING_VALUES.py =====================


import pandas as pd
import numpy as np


# .........................Create DataFrame.........................#

data = {
    "Name": ["Aman", "Rahul", "Rohit", "Vikas", "Ankit"],
    "Age": [20, np.nan, 19, 22, np.nan],
    "Marks": [75, 82, np.nan, 68, 88],
    "City": ["Jamshedpur", "Ranchi", np.nan, "Bokaro", "Ranchi"]
}

df = pd.DataFrame(data)

print("Original DataFrame:")

print(df)


# .........................Check Missing Values.........................#

print("\nCheck Missing Values:")

print(df.isnull())


# .........................Count Missing Values.........................#

print("\nMissing Values in Each Column:")

print(df.isnull().sum())


# .........................Check Total Missing Values.........................#

print("\nTotal Missing Values:")

print(df.isnull().sum().sum())


# .........................Check Not Missing Values.........................#

print("\nNot Missing Values:")

print(df.notnull())


# .........................Remove Rows with Missing Values.........................#

clean_df = df.dropna()

print("\nAfter Removing Rows:")

print(clean_df)


# .........................Remove Rows with Any Missing Value.........................#

df_any = df.dropna(how="any")

print("\nDrop Rows with Any Missing Value:")

print(df_any)


# .........................Remove Rows with All Missing Values.........................#

df_all = df.dropna(how="all")

print("\nDrop Rows with All Missing Values:")

print(df_all)


# .........................Fill Missing Values with Zero.........................#

df_zero = df.copy()

df_zero = df_zero.fillna(0)

print("\nMissing Values Filled with Zero:")

print(df_zero)


# .........................Fill Missing Age with Mean.........................#

df_mean = df.copy()

df_mean["Age"] = df_mean["Age"].fillna(
    df_mean["Age"].mean()
)

print("\nAge Missing Values Filled with Mean:")

print(df_mean)


# .........................Fill Missing Marks with Mean.........................#

df_mean["Marks"] = df_mean["Marks"].fillna(
    df_mean["Marks"].mean()
)

print("\nMarks Missing Values Filled with Mean:")

print(df_mean)


# .........................Fill Missing Age with Median.........................#

df_median = df.copy()

df_median["Age"] = df_median["Age"].fillna(
    df_median["Age"].median()
)

print("\nAge Missing Values Filled with Median:")

print(df_median)


# .........................Fill Missing City with Value.........................#

df_city = df.copy()

df_city["City"] = df_city["City"].fillna("Unknown")

print("\nCity Missing Values Filled:")

print(df_city)


# .........................Forward Fill.........................#

df_forward = df.copy()

df_forward = df_forward.ffill()

print("\nForward Fill:")

print(df_forward)


# .........................Backward Fill.........................#

df_backward = df.copy()

df_backward = df_backward.bfill()

print("\nBackward Fill:")

print(df_backward)


# .........................Replace Missing Values.........................#

df_replace = df.copy()

df_replace = df_replace.replace(
    np.nan,
    "Missing"
)

print("\nMissing Values Replaced:")

print(df_replace)


# .........................Final Clean Data.........................#

final_df = df.copy()

final_df["Age"] = final_df["Age"].fillna(
    final_df["Age"].mean()
)

final_df["Marks"] = final_df["Marks"].fillna(
    final_df["Marks"].mean()
)

final_df["City"] = final_df["City"].fillna("Unknown")

print("\nFinal Clean Data:")

print(final_df)
```
