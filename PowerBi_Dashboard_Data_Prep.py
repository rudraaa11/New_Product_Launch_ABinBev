import pandas as pd
import matplotlib.pyplot as plt

# Sample data taken form the given PDF
data = {
    "Store Name": ["Store A", "Store A", "Store B", "Store C", "Store C"],
    "Product": ["Budweiser", "Stella Artois", "Competitor", "Budweiser", "Stella Artois"],
    "Packaging Type": ["Can", "Bottle", "Bottle", "Can", "Bottle"],
    "Pack Size": ["6-pack", "6-pack", "6-pack", "12-pack", "6-pack"],
    "Units Sold": [20, 108, 143, 74, 10],
    "Price per Unit": [100, 200, 220, 140, 230],
    "Revenue": [20 * 100, 108 * 200, 143 * 220, 74 * 140, 10 * 230],
}

# Made Datafram

df = pd.DataFrame(data)

# SAving the Excel File
output_file = "New_Product_Launch_Data.xlsx"
df.to_excel(output_file, index=False, sheet_name="Raw Data")

print(f"Excel file '{output_file}' successfully ban gaya!")

# Data Summarization For Power Bi
store_summary = df.groupby("Store Name").agg(
    Total_Units_Sold=("Units Sold", "sum"),
    Total_Revenue=("Revenue", "sum")
).reset_index()

# Put In Excel
with pd.ExcelWriter(output_file, mode="a", engine="openpyxl") as writer:
    store_summary.to_excel(writer, index=False, sheet_name="Store Summary")

print("Store summary data Excel me add kar diya.")

# Making A Bar Plot Visualisation
plt.figure(figsize=(8, 6))
plt.bar(store_summary["Store Name"], store_summary["Total_Revenue"], color="skyblue")
plt.title("Total Revenue by Store", fontsize=14)
plt.xlabel("Store Name", fontsize=12)
plt.ylabel("Total Revenue", fontsize=12)
plt.tight_layout()
plt.savefig("Revenue_by_Store.png")

print("Visualization 'Revenue_by_Store.png' me save ho gaya.")
