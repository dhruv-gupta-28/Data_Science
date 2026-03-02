# CAPSTONE PROJECT 1 - TASK CHECKLIST

## Project: Sales Data Analysis Dashboard

---

## TASK COMPLETION CHECKLIST

### Core Requirements

#### Section 1: Load and Inspect Dataset

- [ ] Load CSV file using `pd.read_csv()`
- [ ] Display dataset shape (rows × columns)
- [ ] Show all column names
- [ ] Display first few rows (head)
- [ ] Show data types for each column
- [ ] Generate summary statistics (describe)
- [ ] Check data quality metrics

**Code Location:** Line 34-49
**Expected Output:** Dataset overview in console

---

#### Section 2: Handle Missing Values

- [ ] Check for missing/null values in all columns
- [ ] Count missing values per column
- [ ] Fill numeric columns with median
- [ ] Fill categorical columns with mode or 'Unknown'
- [ ] Verify all missing values are handled
- [ ] Document handling strategy

**Code Location:** Line 54-77
**Expected Output:** Clean dataset with 0 null values

---

#### Section 3: Convert Date Column to Datetime

- [ ] Identify the date column (auto-detect or manual)
- [ ] Convert column to datetime format
- [ ] Handle any parsing errors gracefully
- [ ] Extract month/year for time series analysis
- [ ] Create new time-based columns
- [ ] Display date range of data

**Code Location:** Line 82-92
**Expected Output:** datetime-formatted date column

---

#### Section 4: Create New Columns

- [ ] Calculate `total_sales = price × quantity`
- [ ] Create `month` column from date
- [ ] Create `year_month` column in YYYY-MM format
- [ ] Verify new columns appear in dataframe
- [ ] Display sample of new columns

**Code Location:** Line 97-108
**Expected Output:** 3 new calculated columns

---

#### Section 5: Group By Analysis

- [ ] **By Category:**
- [ ] Sum total sales per category
- [ ] Count number of orders per category
- [ ] Calculate average order value
- [ ] Sort by total sales (descending)

- [ ] **By Region:**
- [ ] Sum revenue per region
- [ ] Count orders per region
- [ ] Calculate average sale per region
- [ ] Sort by revenue (descending)

- [ ] **By Month:**
- [ ] Sum sales per month
- [ ] Count orders per month
- [ ] Show chronological order

**Code Location:** Line 113-138
**Expected Output:** 3 grouped dataframes

---

#### Section 6: Key Insights Discovery

- [ ] **Top 5 Best Selling Products**
- [ ] Ranked by total revenue
- [ ] Display with sales amounts
- [ ] Display with formatted currency

- [ ] **Top 5 Products by Quantity**
- [ ] Ranked by units sold
- [ ] Display quantity numbers

- [ ] **Worst Performing Category**
- [ ] Identify lowest revenue category
- [ ] Show category name and revenue

- [ ] **Best Performing Region**
- [ ] Identify highest revenue region
- [ ] Show region name and revenue

- [ ] **Additional Metrics:**
- [ ] Average order value
- [ ] Total revenue
- [ ] Total order count

**Code Location:** Line 143-189
**Expected Output:** 8+ key metrics displayed

---

#### Section 7: Pivot Table Analysis

- [ ] Create pivot table with:
- [ ] Index: Region
- [ ] Columns: Category
- [ ] Values: Total Sales (summed)
- [ ] Include margins (row/column totals)
- [ ] Round values to 2 decimal places
- [ ] Display complete pivot table

**Code Location:** Line 194-209
**Expected Output:** Region × Category matrix

---

#### Section 8: Export Summary Report to Excel

- [ ] Create Excel workbook with 7 sheets

**Sheet 1: Summary**

- [ ] Executive metrics
- [ ] Key performance indicators
- [ ] Date range

**Sheet 2: Category Analysis**

- [ ] Sales by category
- [ ] Order counts
- [ ] Average values

**Sheet 3: Region Analysis**

- [ ] Sales by region
- [ ] Order counts
- [ ] Average values

**Sheet 4: Top 5 Products**

- [ ] Product names
- [ ] Revenue amounts
- [ ] Ranked list

**Sheet 5: Pivot Table**

- [ ] Region vs Category matrix
- [ ] Include totals

**Sheet 6: Monthly Trend**

- [ ] Sales by month
- [ ] Order counts

**Sheet 7: Raw Data Sample**

- [ ] First 1000 rows of processed data
- [ ] All columns included

**Code Location:** Line 214-261
**Expected Output:** Sales_Analysis_Report.xlsx

---

### Advanced Features (Optional Enhancements)

- [ ] Add data visualization (charts/graphs)
- [ ] Generate PDF report
- [ ] Create interactive dashboard (Plotly/Dash)
- [ ] Add statistical analysis (correlation, trends)
- [ ] Implement forecasting model
- [ ] Add anomaly detection
- [ ] Create email report automation
- [ ] Build web interface

---

## DATA REQUIREMENTS

### Input Dataset: LARGE_sales_dataset.csv

**Required Columns:**

- [ ] `order_id` - Unique identifier (numeric)
- [ ] `product` - Product name (string)
- [ ] `category` - Product category (string)
- [ ] `price` - Unit price (numeric)
- [ ] `quantity` - Units ordered (numeric)
- [ ] `date` - Transaction date (date/datetime)
- [ ] `region` - Geographic region (string)

**Optional Columns:**

- [ ] Customer name
- [ ] Customer location
- [ ] Payment method
- [ ] Shipping details

---

## SUCCESS CRITERIA

For this project to be considered **complete**, verify:

1. **Dataset Loaded:** No errors loading CSV
2. **Data Cleaned:** 0 missing values
3. **Date Converted:** Proper datetime format
4. **Columns Created:** total_sales, month, year_month exist
5. **Analysis Complete:** All groupby results displayed
6. **Insights Found:** Top/worst performers identified
7. **Pivot Table:** Region vs Category matrix generated
8. **Excel Export:** 7-sheet report created and saved
9. **Clean Output:** All metrics formatted with proper currency/units
10. **No Errors:** Script runs without exceptions

---

## EXPECTED RESULTS SAMPLE

When you run the script, you should see:

**Console Output:**

```
================================================================================
SECTION 1: LOADING AND INSPECTING DATASET
================================================================================

 Dataset Shape: 5000 rows, 7 columns

 Column Names:
['order_id', 'product', 'category', 'price', 'quantity', 'date', 'region']

...

================================================================================
SECTION 6: KEY INSIGHTS
================================================================================

 TOP 5 BEST SELLING PRODUCTS (by total sales):
 1. Product A: $125,450.00
 2. Product B: $98,320.00
 ...
```

**Excel File:**

- 7 sheets with formatted tables
- Currency values with $ and commas
- Summary metrics visible at a glance

---

## IMPLEMENTATION NOTES

### Key Functions Used:

- `pd.read_csv()` - Load data
- `pd.isnull().sum()` - Check missing values
- `df.fillna()` - Fill missing values
- `pd.to_datetime()` - Convert to datetime
- `df.groupby()` - Group analysis
- `df.pivot_table()` - Create pivot table
- `df.to_excel()` - Export to Excel

### Data Types:

- Numeric: `int`, `float`
- String: `object` (in pandas)
- DateTime: `datetime64[ns]`

### Performance Notes:

- For large datasets (>100K rows), groupby operations may take a few seconds
- Excel export scales with dataset size
- Memory usage depends on number of unique values in groupby columns

---

## TROUBLESHOOTING GUIDE

| Issue                      | Solution                                           |
| -------------------------- | -------------------------------------------------- |
| **FileNotFoundError**      | Ensure CSV file in same directory                  |
| **ModuleNotFoundError**    | Run `pip install -r requirements.txt`              |
| **KeyError: column name**  | Check column names in CSV match expected names     |
| **ParserError with dates** | Verify date format in CSV (YYYY-MM-DD recommended) |
| **Empty pivot table**      | Verify region and category columns exist           |
| **Excel not created**      | Check write permissions in directory               |

---

## LEARNING OBJECTIVES

After completing this project, you should understand:

- Pandas DataFrame operations
- Data cleaning and validation
- DateTime handling and time series
- GroupBy aggregations
- Pivot tables for analysis
- Excel export workflows
- Business metrics calculation
- Data-driven insights generation

---

## ⏱ ESTIMATED TIME

- **Setup:** 5 minutes
- **Running Script:** 1-5 minutes (depends on dataset size)
- **Reviewing Results:** 10-15 minutes
- **Customization:** 15-30 minutes

**Total:** 30-55 minutes for complete analysis

---

## NEXT STEPS

After completing this project:

1. Try modifying filters and date ranges
2. Add custom calculations (profit margin, etc.)
3. Create visualizations (charts, graphs)
4. Build an interactive dashboard
5. Implement forecasting models
6. Present findings to stakeholders
7. Automate report generation (scheduled)

---

**Document Version:** 1.0
**Last Updated:** 2026-03-02
**Status:** Ready for Implementation
