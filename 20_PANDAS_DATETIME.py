20_PANDAS_DATETIME.py
# ===================== 20_PANDAS_DATETIME.py =====================


import pandas as pd


# .........................Create Date Data.........................#

data = {
    "Name": ["Aman", "Rahul", "Rohit", "Priya", "Neha"],
    "Joining_Date": [
        "2026-01-10",
        "2026-02-15",
        "2026-03-20",
        "2026-04-05",
        "2026-05-12"
    ]
}

df = pd.DataFrame(data)

print("Original Data:")

print(df)


# .........................Convert to DateTime.........................#

df["Joining_Date"] = pd.to_datetime(
    df["Joining_Date"]
)

print("\nAfter Converting to DateTime:")

print(df)


# .........................Check Data Type.........................#

print("\nData Type:")

print(df["Joining_Date"].dtype)


# .........................Current Date.........................#

today = pd.Timestamp.today()

print("\nToday's Date:")

print(today)


# .........................Get Date Only.........................#

print("\nDate Only:")

print(today.date())


# .........................Get Year.........................#

df["Year"] = df["Joining_Date"].dt.year

print("\nYear:")

print(df)


# .........................Get Month.........................#

df["Month"] = df["Joining_Date"].dt.month

print("\nMonth:")

print(df)


# .........................Get Month Name.........................#

df["Month_Name"] = df["Joining_Date"].dt.month_name()

print("\nMonth Name:")

print(df)


# .........................Get Day.........................#

df["Day"] = df["Joining_Date"].dt.day

print("\nDay:")

print(df)


# .........................Day Name.........................#

df["Day_Name"] = df["Joining_Date"].dt.day_name()

print("\nDay Name:")

print(df)


# .........................Day of Week.........................#

df["Day_Of_Week"] = df["Joining_Date"].dt.dayofweek

print("\nDay of Week:")

print(df)


# .........................Quarter.........................#

df["Quarter"] = df["Joining_Date"].dt.quarter

print("\nQuarter:")

print(df)


# .........................Week Number.........................#

df["Week"] = df["Joining_Date"].dt.isocalendar().week

print("\nWeek Number:")

print(df)


# .........................Date Difference.........................#

df["Days_From_Today"] = (
    pd.Timestamp.today() - df["Joining_Date"]
).dt.days

print("\nDays From Today:")

print(df)


# .........................Add Days.........................#

df["After_10_Days"] = (
    df["Joining_Date"] + pd.Timedelta(days=10)
)

print("\nAfter 10 Days:")

print(df)


# .........................Subtract Days.........................#

df["Before_10_Days"] = (
    df["Joining_Date"] - pd.Timedelta(days=10)
)

print("\nBefore 10 Days:")

print(df)


# .........................Add Months.........................#

df["After_1_Month"] = (
    df["Joining_Date"] + pd.DateOffset(months=1)
)

print("\nAfter 1 Month:")

print(df)


# .........................Filter by Date.........................#

filtered_data = df[
    df["Joining_Date"] > "2026-03-01"
]

print("\nJoining After March 1:")

print(filtered_data)


# .........................Filter by Year.........................#

year_data = df[
    df["Joining_Date"].dt.year == 2026
]

print("\nJoining in 2026:")

print(year_data)


# .........................Sort by Date.........................#

sorted_data = df.sort_values(
    "Joining_Date"
)

print("\nSorted by Date:")

print(sorted_data)


# .........................Date Range.........................#

dates = pd.date_range(
    start="2026-01-01",
    end="2026-01-10"
)

print("\nDate Range:")

print(dates)


# .........................Date Range with Frequency.........................#

dates = pd.date_range(
    start="2026-01-01",
    periods=7,
    freq="D"
)

print("\n7 Days Date Range:")

print(dates)


# .........................Month End Dates.........................#

month_end = pd.date_range(
    start="2026-01-01",
    periods=6,
    freq="ME"
)

print("\nMonth End Dates:")

print(month_end)


# .........................Date Formatting.........................#

formatted_date = df["Joining_Date_]()_
