import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import seaborn as sns
import plotly.express as px

# ================================
# 1. Load Dataset
# ================================
df = pd.read_csv("employee_attrition.csv")   # Use your HR CSV file
print(df.head())


# ================================
# 2. Data Cleaning
# ================================
df = df.dropna()
df['Attrition'].replace({'Yes': 1, 'No': 0}, inplace=True)


# ================================
# 3. Basic Statistical Summary
# ================================
print(df.describe())


# ================================
# 4. MATPLOTLIB – 3D ATTRITION PLOT
# ================================
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

x = df['Age']
y = df['MonthlyIncome']
z = df['Attrition']

img = ax.scatter(x, y, z, c=z, cmap='coolwarm', s=50)

ax.set_xlabel('Age')
ax.set_ylabel('Monthly Income')
ax.set_zlabel('Attrition (1 = Yes)')

plt.title("3D Employee Attrition Visualization")
plt.colorbar(img)
plt.show()


# ================================
# 5. SEABORN – CORRELATION HEATMAP
# ================================
plt.figure(figsize=(12, 6))
sns.heatmap(df.corr(), cmap="coolwarm", annot=False)
plt.title("Correlation Heatmap – HR Dataset")
plt.show()


# ================================
# 6. SEABORN – ATTRITION vs DEPARTMENT
# ================================
plt.figure(figsize=(10, 5))
sns.countplot(x='Department', hue='Attrition', data=df, palette="coolwarm")
plt.title("Attrition by Department")
plt.xticks(rotation=20)
plt.show()


# ================================
# 7. MATPLOTLIB – PIE CHART ATTRITION
# ================================
labels = ["Stayed", "Left"]
sizes = df['Attrition'].value_counts()

plt.figure(figsize=(7, 7))
plt.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=True, explode=(0, 0.1))
plt.title("Employee Attrition Percentage")
plt.show()


# ================================
# 8. PLOTLY – INTERACTIVE DASHBOARD
# ================================
fig = px.scatter(
    df,
    x="Age",
    y="MonthlyIncome",
    color="Attrition",
    size="JobSatisfaction",
    hover_data=['Department', 'Education', 'Gender'],
    title="Interactive Attrition Dashboard"
)

fig.show()


# ================================
# 9. PLOTLY – INTERACTIVE BAR CHART
# ================================
fig2 = px.bar(
    df,
    x="Department",
    color="Attrition",
    title="Interactive Attrition by Department",
    barmode='group'
)
fig2.show()

