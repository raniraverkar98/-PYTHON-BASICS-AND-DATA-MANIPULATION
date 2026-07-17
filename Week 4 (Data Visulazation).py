import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Create Dataset
data = {
    "Employee_ID": [101,102,103,104,105,106],
    "Department": ["IT","HR","IT","Finance","IT","HR"],
    "Age": [25,28,27,30,27,28],
    "Salary": [45000,40000,52000,45400,48000,42000]
}

df = pd.DataFrame(data)

# 1. Average Salary by Department
avg_salary = df.groupby("Department")["Salary"].mean()
avg_salary.plot(kind='bar')
plt.title("Average Salary by Department")
plt.xlabel("Department")
plt.ylabel("Average Salary")
plt.show()

# 2. Age Distribution
sns.histplot(df["Age"], bins=5, kde=True)
plt.title("Age Distribution of Employees")
plt.show()

# 3. Salary Distribution
sns.boxplot(x=df["Salary"])
plt.title("Salary Distribution")
plt.show()

# 4. Employee Distribution by Department
dept_count = df["Department"].value_counts()
plt.pie(dept_count, labels=dept_count.index, autopct='%1.1f%%')
plt.title("Employee Distribution by Department")
plt.show()