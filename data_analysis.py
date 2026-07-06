import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("gadgets.csv")
print("\nFirst Five Rows")
print(df.head())
print("\nDataset Information")
print(df.info())
print("\nSummary Statistics")
print(df.describe())
print("\nShape of DataFrame:")
print(df.shape)
print("\nMissing Values")
print(df.isnull().sum())
print("\nTotal Sales")
print(df["Sales"].sum())
print("\nTotal Quantity Sold")
print(df["Quantity"].sum())
print("\nSales by Category")
category_sales = df.groupby("Category")["Sales"].sum()
print(category_sales)
print("\nSales by Region")
region_sales = df.groupby("Region")["Sales"].sum()
print(region_sales)
print("\nProduct Wise Sales")
product_sales = df.groupby("Product")["Sales"].sum()
print(product_sales)
print("\nAverage Sales by Category")
print(df.groupby("Category")["Sales"].mean())
print("\nMaximum Sale")
print(df["Sales"].max())
print("\nMinimum Sale")
print(df["Sales"].min())
print("\nHighest Selling Product")
print(product_sales.idxmax())
print("\nProducts with Sales > 20000")
print(df[df["Sales"] > 20000])
print("\nElectronics Products")
print(df[df["Category"] == "Electronics"])
print("\nSorted by Sales")
print(df.sort_values(by="Sales", ascending=False))
category_sales.plot(
    kind="bar",
    figsize=(7,5),
    color="skyblue"
)
plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Sales")
plt.xticks(rotation=0)
plt.show()
region_sales.plot(
    kind="pie",
    autopct="%1.1f%%",
    figsize=(6,6)
)
plt.title("Sales by Region")
plt.ylabel("")
plt.show()
product_sales.plot(
    kind="line",
    marker="o",
    figsize=(8,5)
)
plt.title("Product Wise Sales")
plt.xlabel("Product")
plt.ylabel("Sales")
plt.grid(True)
plt.show()
product_sales.plot(
    kind="barh",
    figsize=(8,5),
    color="orange"
)
plt.title("Product Wise Sales")
plt.xlabel("Sales")
plt.show()
print("\nData Analysis Completed Successfully.")