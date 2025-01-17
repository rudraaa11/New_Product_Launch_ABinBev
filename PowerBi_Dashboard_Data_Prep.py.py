import pandas as pd
import matplotlib.pyplot as plt

# Define sample data
data = {
    "Store Name": ["Store A", "Store A", "Store B", "Store C", "Store C"],
    "Product": ["Budweiser", "Stella Artois", "Competitor", "Budweiser", "Stella Artois"],
    "Packaging Type": ["Can", "Bottle", "Bottle", "Can", "Bottle"],
    "Pack Size": ["6-pack", "6-pack", "6-pack", "12-pack", "6-pack"],
    "Units Sold": [20, 108, 143, 74, 10],
    "Price per Unit": [8, 12, 10, 15, 12],
    "Revenue": [20 * 8, 108 * 12, 143 * 10, 74 * 15, 10 * 12],
}

# Create a DataFrame
df = pd.DataFrame(data)

# Save to Excel
output_file = "New_Product_Launch_Data.xlsx"
df.to_excel(output_file, index=False, sheet_name="Raw Data")

print(f"Excel file '{output_file}' has been created successfully!")

# Additional data transformations for Power BI
# Create summary data by store
store_summary = df.groupby("Store Name").agg(
    Total_Units_Sold=("Units Sold", "sum"),
    Total_Revenue=("Revenue", "sum")
).reset_index()

# Save the summary data to another sheet
with pd.ExcelWriter(output_file, mode="a", engine="openpyxl") as writer:
    store_summary.to_excel(writer, index=False, sheet_name="Store Summary")

print("Store summary data added to Excel file.")

# Create a simple bar plot for visualization
plt.figure(figsize=(8, 6))
plt.bar(store_summary["Store Name"], store_summary["Total_Revenue"], color="skyblue")
plt.title("Total Revenue by Store", fontsize=14)
plt.xlabel("Store Name", fontsize=12)
plt.ylabel("Total Revenue", fontsize=12)
plt.tight_layout()
plt.savefig("Revenue_by_Store.png")

print("Visualization saved as 'Revenue_by_Store.png'.")
