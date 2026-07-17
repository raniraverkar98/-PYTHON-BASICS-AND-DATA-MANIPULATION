import pandas as pd

# Create Dataset
data = {
    "Employee_ID": [101,102,103,104,105,106],
    "Name": ["Amit","Priya","Rahul ","Sneha","Karan","Neha"],
    "Age": [25,28,None,30,27,None],
    "Department": ["IT","HR","IT","Finance","IT","HR"],
    "Salary": [45000,40000,56000,None,48000,42000]
}

df = pd.DataFrame(data)

print("Original Dataset")
print(df)

print("\nMissing Values")
print(df.isnull().sum())

# Data Cleaning
df["Age"] = df["Age"].fillna(df["Age"].mean())
df["Salary"] = df["Salary"].fillna(df["Salary"].mean())

print("\nCleaned Dataset")
print(df)

# Aggregation
print("\nAverage Salary by Department")
print(df.groupby("Department")["Salary"].mean())

print("\nAverage Age")
print(df["Age"].mean())

print("\nAverage Salary")
print(df["Salary"].mean())