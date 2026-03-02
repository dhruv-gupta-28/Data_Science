# CUSTOMIZATION GUIDE - Adapting the Project

## How to Modify the Script for Different Datasets

---

## QUICK CUSTOMIZATION CHECKLIST

- [ ] Change CSV filename
- [ ] Update column names
- [ ] Adjust groupby dimensions
- [ ] Create custom calculations
- [ ] Modify Excel export sheets
- [ ] Add filtering logic
- [ ] Change output formatting

---

## STEP-BY-STEP CUSTOMIZATION

### 1. Using a Different Dataset

#### File Path (Line 36)

**Default:**

```python
file_path = "LARGE_sales_dataset.csv"
```

**Custom:**

```python
# Option A: Different file name in same folder
file_path = "your_data.csv"

# Option B: Different folder
file_path = "../data_folder/your_data.csv"

# Option C: Absolute path (Windows)
file_path = "C:/Users/YourName/Documents/data.csv"
```

**Verification:**

```python
import os
if os.path.exists(file_path):
 print(" File found")
else:
 print(" File not found - check path")
```

---

### 2. Different Column Names

#### Current Column Expectations:

```
order_id, product, category, price, quantity, date, region
```

#### If Your Columns Have Different Names:

**Find and Replace These Values:**

| Current    | Your Column | Where to Change          |
| ---------- | ----------- | ------------------------ |
| `product`  | Your name   | Line 121, 156, 166, 179  |
| `category` | Your name   | Lines 117, 244, 249      |
| `region`   | Your name   | Lines 125, 160, 172, 298 |
| `price`    | Your name   | Line 103, 303            |
| `quantity` | Your name   | Line 103, 308            |
| `date`     | Your name   | Lines 90, 104-105        |

**Quick Replace Method:**

```python
# Option 1: Use Find and Replace in Editor (Ctrl+H)
# Find: 'category' Replace with: 'your_column_name'

# Option 2: Rename columns in code:
df = df.rename(columns={
 'old_name': 'product',
 'other_name': 'category'
})
```

---

### 3. Custom Calculations

#### Add New Calculated Columns

**Example 1: Calculate Profit Margin**

```python
# Add after line 103
df['cost_per_unit'] = 50 # You set based on your data
df['profit'] = (df['price'] - df['cost_per_unit']) * df['quantity']
df['profit_margin'] = (df['profit'] / df['total_sales'] * 100).round(2)
```

**Example 2: Customer Lifetime Value**

```python
# Create grouping first (need customer_id column)
customer_ltv = df.groupby('customer_id').agg({
 'total_sales': 'sum',
 'quantity': 'sum'
}).rename(columns={
 'total_sales': 'lifetime_value',
 'quantity': 'total_units'
})
```

**Example 3: Sales per Day**

```python
# Add after line 106
df['day_of_week'] = pd.to_datetime(df['date']).dt.day_name()
daily_sales = df.groupby('day_of_week')['total_sales'].sum()
```

---

### 4. Custom GroupBy Analysis

#### Add New Grouping Dimensions

**Current GroupBy:**

```python
df.groupby('category') # Single dimension
df.groupby('region') # Single dimension
```

**Multi-Dimensional GroupBy:**

```python
# By Region AND Category
region_category = df.groupby(['region', 'category'])['total_sales'].sum()

# By Region AND Product
region_product = df.groupby(['region', 'product'])['total_sales'].sum()

# By Month AND Region
monthly_region = df.groupby(['year_month', 'region'])['total_sales'].sum()
```

**Add Custom Aggregations:**

```python
# Multiple statistics at once
custom_agg = df.groupby('region').agg({
 'total_sales': ['sum', 'mean', 'max', 'min'],
 'quantity': 'sum',
 'product': 'nunique' # Count different products
})

print(custom_agg)
```

---

### 5. Filtering Data

#### Filter Before Analysis

**By Date Range:**

```python
# Add after line 108
start_date = '2024-01-01'
end_date = '2024-12-31'
df = df[(df['date'] >= start_date) & (df['date'] <= end_date)]
```

**By Region:**

```python
# Analyze only specific regions
regions_of_interest = ['North', 'South']
df_filtered = df[df['region'].isin(regions_of_interest)]
```

**By Category:**

```python
# Exclude low-performing categories
df_filtered = df[df['category'] != 'Electronics']
```

**By Price Range:**

```python
# Only high-value transactions
df_filtered = df[df['price'] > 100]
```

**By Transaction Value:**

```python
# Only significant sales
df_filtered = df[df['total_sales'] > df['total_sales'].median()]
```

**Combined Filters:**

```python
# Multiple conditions
df_filtered = df[
 (df['region'] == 'North') &
 (df['date'] >= '2024-01-01') &
 (df['total_sales'] > 1000)
]
```

---

### 6. Custom Excel Export

#### Add More Sheets

**Current (7 sheets):**

```python
# Existing sheets
summary_df.to_excel(writer, sheet_name='Summary')
category_sales.to_excel(writer, sheet_name='Category Analysis')
# ... etc
```

**Add New Sheets:**

```python
# Add custom analysis
customer_summary = df.groupby('customer_id').agg({
 'total_sales': 'sum',
 'orders': 'count'
}).nlargest(50, 'total_sales') # Top 50 customers

customer_summary.to_excel(writer, sheet_name='Top 50 Customers')
```

**Add Formatted Summary Sheet:**

```python
# Create summary with labels
summary_detailed = pd.DataFrame({
 'KPI': [
 'Total Revenue',
 'Average Order Value',
 'Total Orders',
 'Avg Order Size (units)',
 'Price Range'
 ],
 'Value': [
 f"${df['total_sales'].sum():,.2f}",
 f"${df['total_sales'].mean():,.2f}",
 f"{len(df):,}",
 f"{df['quantity'].mean():.1f}",
 f"${df['price'].min():.2f} - ${df['price'].max():.2f}"
 ]
})

summary_detailed.to_excel(writer, sheet_name='KPI Summary', index=False)
```

---

### 7. Custom Sorting and Filtering in Output

#### Sort Results Different Ways

**Ascending vs Descending:**

```python
# Current (descending - largest first)
category_sales.sort_values('Total_Sales', ascending=False)

# Ascending - smallest first
category_sales.sort_values('Total_Sales', ascending=True)
```

**Sort by Multiple Columns:**

```python
# Sort by total sales DESC, then by count ASC
category_sales.sort_values(
 by=['Total_Sales', 'Number_of_Orders'],
 ascending=[False, True]
)
```

**Top/Bottom N Items:**

```python
# Top 10 products
top_10 = df.groupby('product')['total_sales'].sum().nlargest(10)

# Bottom 5 products
bottom_5 = df.groupby('product')['total_sales'].sum().nsmallest(5)

# Top 25%
top_quartile = df.groupby('region')['total_sales'].sum().nlargest(
 int(df['region'].nunique() * 0.25)
)
```

---

### 8. Custom Formatting and Display

#### Change Number Formatting

**Current:**

```python
print(f"${sales:,.2f}") # $1,234.56
```

**Alternatives:**

```python
# No decimals (for units)
print(f"{quantity:,.0f} units") # 1,234 units

# Percentage
print(f"{percentage:.1f}%") # 45.5%

# Thousands (K) Format
print(f"${sales/1000:.1f}K") # $1.2K

# Scientific notation
print(f"{large_number:.2e}") # 1.23e+05
```

---

### 9. Conditional Logic and Alerts

#### Add Business Rules

**Example: Flag Low-Performing Categories**

```python
# After line 117
threshold = category_sales['Total_Sales'].mean()
for category in category_sales.index:
 sales = category_sales.loc[category, 'Total_Sales']
 if sales < threshold:
 print(f" {category} underperforming: ${sales:,.2f}")
```

**Example: Growth Alert**

```python
if monthly_sales.iloc[-1]['Total_Sales'] > monthly_sales.iloc[-2]['Total_Sales']:
 print(" Sales growing!")
else:
 print(" Sales declining")
```

**Example: Quality Check**

```python
if df.isnull().sum().sum() > 100:
 print(" WARNING: Many missing values detected!")
```

---

### 10. Save Results to CSV

#### Export Intermediate Results

```python
# Save category analysis
category_sales.to_csv('category_analysis.csv')

# Save pivot table
pivot_table.to_csv('region_category_pivot.csv')

# Save raw processed data
df.to_csv('processed_sales_data.csv', index=False)
```

---

## COMMON CUSTOMIZATION EXAMPLES

### Example 1: Customer-Focused Analysis

**Modify for customer data:**

```python
# Replace groupby dimensions
customer_sales = df.groupby('customer_name')['total_sales'].sum().nlargest(20) # Top 20 customers

customer_repeat = df.groupby('customer_name').size().nlargest(10) # Repeat customers

# Add customer metrics
customer_metrics = df.groupby('customer_id').agg({
 'total_sales': ['sum', 'count', 'mean'],
 'date': ['min', 'max'] # First and last purchase
})
```

### Example 2: Time Series Focus

**Emphasize temporal patterns:**

```python
# Group by day instead of month
df['day'] = pd.to_datetime(df['date']).dt.date
daily_sales = df.groupby('day')['total_sales'].sum()

# Calculate growth rates
daily_sales.pct_change() # Daily growth %

# Remove seasonal effects (example)
# monthly_detrended = monthly_sales - monthly_sales.rolling(12).mean()
```

### Example 3: Inventory Analysis

**Transform for inventory perspective:**

```python
# High-value, slow-moving items
inventory_metrics = df.groupby('product').agg({
 'total_sales': 'sum', # Total revenue
 'quantity': 'sum', # Units sold
 'date': 'count' # Number of transactions
}).assign(
 velocity = lambda x: x['quantity'] / x['date'] # Units per transaction
)

high_value_slow = inventory_metrics[
 (inventory_metrics['total_sales'] > inventory_metrics['total_sales'].quantile(0.75)) &
 (inventory_metrics['velocity'] < inventory_metrics['velocity'].quantile(0.25))
]
```

### Example 4: Profitability Analysis

**Add cost-based metrics:**

```python
# Assume different cost for each category
cost_map = {
 'Electronics': 500,
 'Clothing': 25,
 'Home': 40
}

df['cost'] = df['category'].map(cost_map)
df['profit'] = (df['price'] - df['cost']) * df['quantity']
df['margin'] = (df['profit'] / df['total_sales'] * 100).round(1)

# Find most profitable items
profitability = df.groupby('product').agg({
 'profit': 'sum',
 'margin': 'mean'
}).sort_values('profit', ascending=False)
```

---

## TESTING YOUR CHANGES

**Always verify these after customization:**

```python
# 1. Check no errors
# Run script - watch for exceptions

# 2. Verify data shape didn't change unexpectedly
print(df.shape)

# 3. Check new columns exist
print(df.columns.tolist())

# 4. Spot check values
print(df.head())

# 5. Verify Excel file created
import os
print(os.path.exists('Sales_Analysis_Report.xlsx'))
```

---

## TEMPLATE: MINIMAL CUSTOMIZATION

Use this template for quick customization:

```python
import pandas as pd
import numpy as np
from datetime import datetime
import os

# ===== STEP 1: CONFIGURE =====
FILE = "your_data.csv" # ← CHANGE THIS
PRODUCT_COL = "product" # ← CHANGE IF NEEDED
CATEGORY_COL = "category" # ← CHANGE IF NEEDED
REGION_COL = "region" # ← CHANGE IF NEEDED
PRICE_COL = "price" # ← CHANGE IF NEEDED
QUANTITY_COL = "quantity" # ← CHANGE IF NEEDED
DATE_COL = "date" # ← CHANGE IF NEEDED

# ===== STEP 2: LOAD DATA =====
df = pd.read_csv(FILE)

# ===== STEP 3: CLEAN DATA =====
df[PRICE_COL] = df[PRICE_COL].fillna(df[PRICE_COL].median())
df[QUANTITY_COL] = df[QUANTITY_COL].fillna(df[QUANTITY_COL].median())

# ===== STEP 4: CREATE CALCULATIONS =====
df['total_sales'] = df[PRICE_COL] * df[QUANTITY_COL]
df[DATE_COL] = pd.to_datetime(df[DATE_COL])
df['month'] = df[DATE_COL].dt.to_period('M')

# ===== STEP 5: ANALYZE =====
print(df.groupby(CATEGORY_COL)['total_sales'].sum())
print(df.groupby(REGION_COL)['total_sales'].sum())

# ===== STEP 6: EXPORT =====
with pd.ExcelWriter("output.xlsx", engine='openpyxl') as writer:
 df.groupby(CATEGORY_COL)['total_sales'].sum().to_excel(
 writer, sheet_name='By Category'
 )
 df.groupby(REGION_COL)['total_sales'].sum().to_excel(
 writer, sheet_name='By Region'
 )
```

---

## TROUBLESHOOTING CUSTOMIZATIONS

| Problem                                     | Solution                                             |
| ------------------------------------------- | ---------------------------------------------------- |
| **NameError: product not defined**          | Check column name matches exactly (case-sensitive)   |
| **KeyError: 'column name'**                 | Column doesn't exist - check CSV column names        |
| **AttributeError: object has no attribute** | Wrong data type - use correct dtype                  |
| **Empty results**                           | Check filter conditions - may be too restrictive     |
| **Excel not saving**                        | Check file not already open, check write permissions |

---

**Guide Version:** 1.0
**Last Updated:** 2026-03-02
