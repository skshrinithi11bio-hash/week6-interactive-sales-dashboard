import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Load dataset
df = pd.read_csv("sales_data.csv")
df.fillna(0, inplace=True)

# Convert date column if present
if "Date" in df.columns:
    df["Date"] = pd.to_datetime(df["Date"])

# -----------------------------
# SEABORN & MATPLOTLIB PLOTS
# -----------------------------
plt.figure(figsize=(16,10))

# Box plot
plt.subplot(2,2,1)
sns.boxplot(x="Product", y="Price", data=df)
plt.title("Price Distribution by Product")
plt.xticks(rotation=45)

# Violin plot
plt.subplot(2,2,2)
sns.violinplot(x="Product", y="Price", data=df)
plt.title("Price Density by Product")
plt.xticks(rotation=45)

# Line plot
plt.subplot(2,2,3)
sns.lineplot(data=df, x="Date", y="Price")
plt.title("Sales Trend Over Time")

# Heatmap
plt.subplot(2,2,4)
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")

plt.tight_layout()
plt.show()

# -----------------------------
# PLOTLY INTERACTIVE CHARTS
# -----------------------------
fig1 = px.bar(df, x="Product", y="Price", color="Product",
              title="Interactive Sales by Product")
fig1.show()

fig2 = px.pie(df, names="Product", values="Price",
              title="Revenue Share by Product")
fig2.show()
