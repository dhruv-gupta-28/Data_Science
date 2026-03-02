# Capstone Project 1 — Sales Data Analysis Dashboard

## Project Goal

Analyze a company's sales performance and generate actionable business insights using data analysis and visualization.

---

## Dataset Information

**File:** `LARGE_sales_dataset.csv`

**Expected Columns:**

- `order_id` - Unique identifier for each order
- `product` - Product name
- `category` - Product category
- `price` - Unit price ($)
- `quantity` - Number of units ordered
- `date` - Transaction date
- `region` - Geographic region/location

---

## Project Tasks Completed

### Task 1: Load and Inspect Dataset

- Load CSV file using pandas
- Display dataset shape and dimensions
- Show column names and data types
- Display first 5 rows and statistical summary
- **Output:** Console display of dataset structure

### Task 2: Handle Missing Values

- Check for missing/null values in all columns
- Fill numeric columns with median values
- Fill categorical columns with mode or "Unknown"
- **Output:** Clean dataset ready for analysis

### Task 3: Convert Date Column to Datetime

- Identify date column automatically
- Convert date column to datetime format
- Extract month and year-month for time series analysis
- Display date range (earliest to latest transaction)
- **Output:** Datetime-enabled columns for trend analysis

### Task 4: Create New Columns

- Create `total_sales` = price × quantity
- Create `month` column for monthly aggregation
- Create `year_month` column for better time filtering
- **Output:** Enhanced dataset with calculated fields

### Task 5: Group By Analysis

- **By Category:** Total sales, order count, average order value
- **By Region:** Total revenue, order count, average order value
- **By Month:** Monthly sales trends and order volume
- **Output:** Aggregated summaries sorted by performance

### Task 6: Key Insights Discovery

- **Top 5 Best Selling Products** (by total revenue)
- **Top 5 Products by Quantity** (volume leaders)
- **Worst Performing Category** (lowest revenue)
- **Best Performing Region** (highest revenue)
- **Average Order Value** across all transactions
- **Total Revenue** and **Total Orders**
- **Output:** Key metrics and insights displayed in console

### Task 7: Pivot Table Analysis

- **Region vs Category Sales Matrix**
- Provides cross-tabulation of sales by region and category
- Includes row and column totals (margins)
- **Output:** Excel-ready pivot table

### Task 8: Export Summary Report to Excel

Creates **Sales_Analysis_Report.xlsx** with 7 sheets:

1. **Summary** - Key metrics and overview
2. **Category Analysis** - Sales performance by product category
3. **Region Analysis** - Sales performance by geographic region
4. **Top 5 Products** - Best performing products
5. **Pivot Table** - Region vs Category cross-analysis
6. **Monthly Trend** - Sales trends over time
7. **Raw Data Sample** - First 1000 rows of processed data

---

## How to Run

### Prerequisites

You may use your system Python or any virtual environment (venv, myenv, etc.).
No special env name is needed – run the commands with the interpreter you prefer.

```bash
# Install required packages
pip install pandas openpyxl numpy
```

### Execution

```bash
# Navigate to project directory
cd 04_Projects_Capstone

# Run the analysis script
python sales_dashboard_analysis.py
```

### Output

- **Console Output:** Detailed analysis with all metrics and insights
- **Excel File:** `Sales_Analysis_Report.xlsx` (multi-sheet report)

---

## Key Metrics Generated

### Business Metrics

- Total Revenue
- Total Number of Orders
- Average Order Value
- Units Sold (Total Quantity)

### Category Performance

- Category ranking by revenue
- Order count per category
- Average order value by category

### Regional Performance

- Revenue by region
- Market share by region
- Regional trends

### Product Performance

- Top 5 revenue-generating products
- Top 5 best-selling products (by quantity)
- Product distribution by category

### Time-Based Analysis

- Monthly sales trends
- Order volume by month
- Seasonal patterns

---

## Insights You Can Derive

1. **Which products/categories drive revenue?**
2. **Which regions generate the most sales?**
3. **What is the seasonal trend in sales?**
4. **What is the average customer transaction value?**
5. **Which categories underperform and need attention?**
6. **Which regions have growth potential?**
7. **Product mix across different regions**

---

## Excel Report Sheets Explained

| Sheet Name            | Purpose                    | Key Info                               |
| --------------------- | -------------------------- | -------------------------------------- |
| **Summary**           | Executive overview         | Top metrics at a glance                |
| **Category Analysis** | Category performance       | Revenue, orders, averages per category |
| **Region Analysis**   | Regional breakdown         | Revenue distribution by location       |
| **Top 5 Products**    | Best performers            | Top revenue-generating products        |
| **Pivot Table**       | Cross-dimensional analysis | Region vs Category breakdown           |
| **Monthly Trend**     | Time series analysis       | Sales patterns over time               |
| **Raw Data Sample**   | Source data verification   | Sample of processed transactions       |

---

## Setup Options

You can modify the script to:

- Change sorting criteria (ascending vs descending)
- Filter by specific date ranges
- Add more analytical dimensions
- Create additional visualizations
- Export to different formats (CSV, JSON)

---

## Learning Outcomes

After completing this project, you'll understand:

- Data loading and exploration with pandas
- Data cleaning and handling missing values
- Working with datetime data
- Groupby operations and aggregations
- Pivot tables for cross-dimensional analysis
- Exporting data to Excel with multiple sheets
- Business analytics and insights generation
- Data-driven decision making

---

## Notes

- The script handles various data types automatically
- Date column is auto-detected (case-insensitive)
- Missing values are handled gracefully
- All currency values are formatted with commas and 2 decimal places
- Pivot table includes margins (totals) for complete picture

---

## Success Criteria

Dataset loads successfully
All missing values handled
Date column properly converted
New calculated columns created
All groupby analyses complete
Key insights identified and displayed
Pivot table generated
Excel report exported with multiple sheets

---

**Created:** 2026-03-02
**Status:** Complete and Ready for Analysis
