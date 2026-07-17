# ==========================================
# Dashboard for Visualizing Relationships
# ==========================================

# Import Required Libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ------------------------------------------
# Create Sample Dataset
# ------------------------------------------

data = {
    "Employee_ID": [101, 102, 103, 104, 105, 106],
    "Department": ["IT", "HR", "IT", "Finance", "IT", "HR"],
    "Age": [25, 28, 27, 30, 27, 28],
    "Experience": [2, 4, 3, 6, 4, 5],
    "Salary": [45000, 40000, 52000, 45400, 48000, 42000]
}

df = pd.DataFrame(data)

# Display Dataset
print("Employee Dataset")
print(df)

# ------------------------------------------
# Dashboard Layout
# ------------------------------------------

plt.figure(figsize=(15, 10))

# ==========================================
# 1. Scatter Plot
# ==========================================
plt.subplot(2, 2, 1)
sns.scatterplot(
    data=df,
    x="Experience",
    y="Salary",
    hue="Department",
    s=120
)
plt.title("Experience vs Salary")
plt.xlabel("Experience (Years)")
plt.ylabel("Salary")

# ==========================================
# 2. Histogram
# ==========================================
plt.subplot(2, 2, 2)
sns.histplot(
    df["Age"],
    bins=5,
    kde=True,
    color="skyblue"
)
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Count")

# ==========================================
# 3. Box Plot
# ==========================================
plt.subplot(2, 2, 3)
sns.boxplot(
    data=df,
    x="Department",
    y="Salary"
)
plt.title("Salary Distribution by Department")
plt.xlabel("Department")
plt.ylabel("Salary")

# ==========================================
# 4. Correlation Heatmap
# ==========================================

# Select only numeric columns
correlation = df[["Age", "Experience", "Salary"]].corr()

plt.subplot(2, 2, 4)
sns.heatmap(
    correlation,
    annot=True,
    cmap="Blues",
    linewidths=0.5,
    fmt=".2f"
)
plt.title("Correlation Heatmap")

# ------------------------------------------
# Adjust Layout
# ------------------------------------------
plt.tight_layout()

# Show Dashboard
plt.show()