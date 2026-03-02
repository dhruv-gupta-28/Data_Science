"""

CAPSTONE PROJECT 1 — Sales Data Analysis Dashboard
=========================================================
Goal: Analyze company's sales performance and generate business insights

Dataset: LARGE_sales_dataset.csv
Columns: order_id, product, category, price, quantity, date, region

Tasks:
1. Load and inspect dataset
2. Handle missing values
3. Convert date column to datetime
4. Create new column → total sales = price × quantity
5. Group by: category, region, month
6. Find: top 5 products, worst category, pivot table (region vs category)
7. Export summary to Excel
"""

import pandas as pd
import numpy as np
from datetime import datetime
import os

# ============================================================================
# SECTION 1: LOAD AND INSPECT DATASET
# ============================================================================
print("=" * 80)
print("SECTION 1: LOADING AND INSPECTING DATASET")
print("=" * 80)

# Load dataset
file_path = "LARGE_sales_dataset.csv"
df = pd.read_csv(file_path)

print(f"\nDataset Shape: {df.shape[0]} rows, {df.shape[1]} columns")
print(f"\nColumn Names:\n{df.columns.tolist()}")
print(f"\nFirst 5 Rows:")
print(df.head())
print(f"\nDataset Info:")
print(df.info())
print(f"\nStatistical Summary:")
print(df.describe())


# ============================================================================
# SECTION 2: HANDLE MISSING VALUES
# ============================================================================
print("\n" + "=" * 80)
print("SECTION 2: HANDLING MISSING VALUES")
print("=" * 80)

# Check for missing values
print(f"\nMissing Values Before Handling:")
missing_values = df.isnull().sum()
print(missing_values[missing_values > 0] if missing_values.sum() > 0 else "No missing values!")

# Handle missing values
if df.isnull().sum().sum() > 0:
    # Fill numeric columns with median
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].median())
    
    # Fill categorical columns with mode or 'Unknown'
    categorical_cols = df.select_dtypes(include=['object']).columns
    for col in categorical_cols:
        df[col] = df[col].fillna('Unknown')
    
    print(f"\nMissing Values After Handling:")
    print(df.isnull().sum().sum())


# ============================================================================
# SECTION 3: CONVERT DATE COLUMN TO DATETIME
# ============================================================================
print("\n" + "=" * 80)
print("SECTION 3: CONVERTING DATE COLUMN")
print("=" * 80)

# Find and convert date column
date_cols = [col for col in df.columns if 'date' in col.lower()]
if date_cols:
    date_col = date_cols[0]
    df[date_col] = pd.to_datetime(df[date_col], errors='coerce')
    print(f"\nConverted '{date_col}' to datetime")
    print(f"Date Range: {df[date_col].min()} to {df[date_col].max()}")
else:
    print("\nNo date column found. Skipping date conversion.")


# ============================================================================
# SECTION 4: CREATE NEW COLUMNS
# ============================================================================
print("\n" + "=" * 80)
print("SECTION 4: CREATING NEW COLUMNS")
print("=" * 80)

# Create total_sales column (price × quantity)
df['total_sales'] = df['price'] * df['quantity']
print(f"\nCreated 'total_sales' column (price × quantity)")

# Extract month from date for time series analysis
if date_cols:
    df['month'] = pd.to_datetime(df[date_col]).dt.to_period('M')
    df['year_month'] = pd.to_datetime(df[date_col]).dt.strftime('%Y-%m')
    print(f"Created 'month' and 'year_month' columns")

print(f"\nUpdated Dataset Columns:")
print(df.columns.tolist())
print(f"\nFirst 5 Rows with New Columns:")
print(df.head())


# ============================================================================
# SECTION 5: GROUP BY ANALYSIS
# ============================================================================
print("\n" + "=" * 80)
print("SECTION 5: GROUP BY ANALYSIS")
print("=" * 80)

# Group by Category → Total Sales
print("\nSALES BY CATEGORY:")
category_sales = df.groupby('category')['total_sales'].agg(['sum', 'count', 'mean']).round(2)
category_sales.columns = ['Total_Sales', 'Number_of_Orders', 'Average_Sale']
category_sales = category_sales.sort_values('Total_Sales', ascending=False)
print(category_sales)

# Group by Region → Revenue
print("\nSALES BY REGION:")
region_sales = df.groupby('region')['total_sales'].agg(['sum', 'count', 'mean']).round(2)
region_sales.columns = ['Total_Revenue', 'Number_of_Orders', 'Average_Sale']
region_sales = region_sales.sort_values('Total_Revenue', ascending=False)
print(region_sales)

# Group by Month → Sales Trend
if date_cols:
    print("\nSALES TREND BY MONTH:")
    monthly_sales = df.groupby('year_month')['total_sales'].agg(['sum', 'count']).round(2)
    monthly_sales.columns = ['Total_Sales', 'Number_of_Orders']
    print(monthly_sales)


# ============================================================================
# SECTION 6: KEY INSIGHTS
# ============================================================================
print("\n" + "=" * 80)
print("SECTION 6: KEY INSIGHTS")
print("=" * 80)

# Top 5 Best Selling Products
print("\nTOP 5 BEST SELLING PRODUCTS (by total sales):")
top_products = df.groupby('product')['total_sales'].sum().nlargest(5).round(2)
for idx, (product, sales) in enumerate(top_products.items(), 1):
    print(f"   {idx}. {product}: ${sales:,.2f}")

# Top 5 Products by Quantity
print("\nTOP 5 PRODUCTS (by quantity sold):")
top_qty = df.groupby('product')['quantity'].sum().nlargest(5)
for idx, (product, qty) in enumerate(top_qty.items(), 1):
    print(f"   {idx}. {product}: {qty:.0f} units")

# Worst Performing Category
print("\nWORST PERFORMING CATEGORY (by total sales):")
# compute using Total_Sales column only to avoid a Series result
worst_category = category_sales['Total_Sales'].idxmin()
worst_sales = category_sales.loc[worst_category, 'Total_Sales']
print(f"   Category: {worst_category}")
print(f"   Total Sales: ${worst_sales:,.2f}")

# Worst Performing Category (by order count)
print("\nWORST PERFORMING CATEGORY (by order count):")
worst_category_count = category_sales['Number_of_Orders'].idxmin()
worst_count = category_sales.loc[worst_category_count, 'Number_of_Orders']
print(f"   Category: {worst_category_count}")
print(f"   Number of Orders: {worst_count:.0f}")

# Best Performing Region
print("\nBEST PERFORMING REGION:")
# select using Total_Revenue column to avoid Series result
best_region = region_sales['Total_Revenue'].idxmax()
best_revenue = region_sales.loc[best_region, 'Total_Revenue']
print(f"   Region: {best_region}")
print(f"   Total Revenue: ${best_revenue:,.2f}")

# Average Order Value
avg_order = df['total_sales'].mean()
print(f"\nAVERAGE ORDER VALUE: ${avg_order:,.2f}")

# Total Revenue
total_revenue = df['total_sales'].sum()
print(f"TOTAL REVENUE: ${total_revenue:,.2f}")

# Total Orders
total_orders = len(df)
print(f"TOTAL ORDERS: {total_orders:,}")


# ============================================================================
# SECTION 7: PIVOT TABLE - REGION VS CATEGORY SALES
# ============================================================================
print("\n" + "=" * 80)
print("SECTION 7: PIVOT TABLE (REGION VS CATEGORY SALES)")
print("=" * 80)

pivot_table = pd.pivot_table(
    df,
    values='total_sales',
    index='region',
    columns='category',
    aggfunc='sum',
    margins=True,
    margins_name='TOTAL'
).round(2)

print("\nREGION vs CATEGORY SALES MATRIX:")
print(pivot_table)


# ============================================================================
# SECTION 8: EXPORT TO EXCEL
# ============================================================================
print("\n" + "=" * 80)
print("SECTION 8: EXPORTING SUMMARY REPORT TO EXCEL")
print("=" * 80)

output_file = "Sales_Analysis_Report.xlsx"

# Create Excel writer object
with pd.ExcelWriter(output_file, engine='openpyxl') as writer:
    # Sheet 1: Overview/Summary
    summary_data = {
        'Metric': [
            'Total Revenue',
            'Total Orders',
            'Average Order Value',
            'Best Performing Region',
            'Worst Performing Category',
            'Date Range Start',
            'Date Range End'
        ],
        'Value': [
            f"${total_revenue:,.2f}",
            f"{total_orders:,}",
            f"${avg_order:,.2f}",
            best_region,
            worst_category,
            str(df[date_col].min()) if date_cols else "N/A",
            str(df[date_col].max()) if date_cols else "N/A"
        ]
    }
    summary_df = pd.DataFrame(summary_data)
    summary_df.to_excel(writer, sheet_name='Summary', index=False)
    
    # Sheet 2: Sales by Category
    category_sales.to_excel(writer, sheet_name='Category Analysis')
    
    # Sheet 3: Sales by Region
    region_sales.to_excel(writer, sheet_name='Region Analysis')
    
    # Sheet 4: Top 5 Products
    top_products_df = pd.DataFrame({
        'Product': top_products.index,
        'Total_Sales': top_products.values
    })
    top_products_df.to_excel(writer, sheet_name='Top 5 Products', index=False)
    
    # Sheet 5: Pivot Table
    pivot_table.to_excel(writer, sheet_name='Pivot Table')
    
    # Sheet 6: Monthly Trend
    if date_cols:
        monthly_sales.to_excel(writer, sheet_name='Monthly Trend')
    
    # Sheet 7: Raw Data (first 1000 rows)
    df.head(1000).to_excel(writer, sheet_name='Raw Data Sample', index=False)

print(f"\nExcel report exported successfully: '{output_file}'")
print(f"Location: {os.path.abspath(output_file)}")


# ============================================================================
# SECTION 9: ADDITIONAL INSIGHTS
# ============================================================================
print("\n" + "=" * 80)
print("SECTION 9: ADDITIONAL INSIGHTS")
print("=" * 80)

# Price Statistics
print("\nPRICE ANALYSIS:")
print(f"   Average Price: ${df['price'].mean():,.2f}")
print(f"   Min Price: ${df['price'].min():,.2f}")
print(f"   Max Price: ${df['price'].max():,.2f}")
print(f"   Median Price: ${df['price'].median():,.2f}")

# Quantity Statistics
print("\nQUANTITY ANALYSIS:")
print(f"   Average Quantity per Order: {df['quantity'].mean():.2f}")
print(f"   Min Quantity: {df['quantity'].min()}")
print(f"   Max Quantity: {df['quantity'].max()}")
print(f"   Total Units Sold: {df['quantity'].sum():,.0f}")

# Products per Category
print("\nPRODUCTS PER CATEGORY:")
products_per_category = df.groupby('category')['product'].nunique().sort_values(ascending=False)
for category, count in products_per_category.items():
    print(f"   {category}: {count} products")

print("\n" + "=" * 80)
print("ANALYSIS COMPLETE!")
print("=" * 80)
