# PROJECT INDEX — Sales Data Analysis Dashboard

## Project Overview

**Capstone Project 1:** Sales Data Analysis Dashboard
**Goal:** Analyze company sales performance and generate business insights
**Difficulty:** Beginner to Intermediate
**Time to Complete:** 30-55 minutes

---

## PROJECT FILES

### CORE ANALYSIS SCRIPT

- **[sales_dashboard_analysis.py](sales_dashboard_analysis.py)** (458 lines)
- Main analysis script
- 9 complete sections
- Produces Excel report with 7 sheets
- Console output with all metrics
- **START HERE:** Run this file for complete analysis

### DATA

- **LARGE_sales_dataset.csv**
- Pre-loaded dataset with ~5000+ sales records
- Columns: order_id, product, category, price, quantity, date, region
- Ready to analyze

### DOCUMENTATION

#### Quick Start

- **[QUICKSTART.py](QUICKSTART.py)** (52 lines)
- One-minute setup guide
- System requirements check
- Installation instructions
- Pre-flight diagnostics
- **USE IF:** Just getting started

#### Main Documentation

- **[README.md](README.md)**
- Project goals and background
- Task descriptions (8 tasks)
- How to run the script
- Excel report explanation
- Key metrics and insights you'll find
- **READ THIS FIRST**

#### Detailed Guides

- **[TASK_CHECKLIST.md](TASK_CHECKLIST.md)**
- Checkbox format - track progress
- Success criteria
- Expected results samples
- Estimated timing
- Learning objectives

- **[CODE_EXPLANATION.md](CODE_EXPLANATION.md)**
- Line-by-line code breakdown
- pandas concept explanations
- Common patterns
- Mistakes to avoid
- Extension ideas

- **[CUSTOMIZATION_GUIDE.md](CUSTOMIZATION_GUIDE.md)**
- How to adapt for different data
- Change column names
- Add custom calculations
- Modify Excel export
- Common examples
- Troubleshooting

### REQUIREMENTS

- **[requirements.txt](requirements.txt)**
- Package dependencies
- Installation command: `pip install -r requirements.txt`
- pandas, numpy, openpyxl

---

## GETTING STARTED (3 STEPS)

### Step 1: Install Dependencies

```bash
pip install -r requirements.txt
```

See: [requirements.txt](requirements.txt)

### Step 2: Run Analysis

```bash
python sales_dashboard_analysis.py
```

See: [sales_dashboard_analysis.py](sales_dashboard_analysis.py)

### Step 3: Review Results

- Check console output for all metrics
- Open `Sales_Analysis_Report.xlsx` for detailed report
- 7 sheets with analysis, charts, and raw data

See: [README.md](README.md)

---

## WHAT YOU'LL LEARN

### Python Skills

- Data loading with pandas
- Data cleaning and validation
- DateTime handling
- GroupBy aggregations
- Pivot tables
- Excel export
- Error handling

### Data Analysis Skills

- Exploratory Data Analysis (EDA)
- Multi-dimensional analysis
- Key metric identification
- Business insight generation
- Report creation
- Decision-making with data

### Business Skills

- Revenue analysis
- Category performance
- Regional trends
- Product rankings
- KPI reporting
- Executive summaries

---

## PROJECT STRUCTURE

```
Sales Dashboard Analysis
 Data Processing
 Load CSV
 Handle missing values
 Convert dates
 Create calculated columns

 Analysis
 Category breakdown
 Regional breakdown
 Time series (monthly)
 Top/worst performers

 Cross-Analysis
 Pivot table (region vs category)

 Output
 Console metrics
 Excel report (7 sheets)
```

---

## PROJECT TASKS

| #   | Task                      | Status | Section |
| --- | ------------------------- | ------ | ------- |
| 1   | Load and inspect dataset  |        | Sec 1   |
| 2   | Handle missing values     |        | Sec 2   |
| 3   | Convert date to datetime  |        | Sec 3   |
| 4   | Create total_sales column |        | Sec 4   |
| 5   | Group by category         |        | Sec 5   |
| 6   | Group by region           |        | Sec 5   |
| 7   | Group by month            |        | Sec 5   |
| 8   | Find top 5 products       |        | Sec 6   |
| 9   | Find worst category       |        | Sec 6   |
| 10  | Create pivot table        |        | Sec 7   |
| 11  | Export to Excel           |        | Sec 8   |

**Status:** All 11 tasks completed

---

## KEY DELIVERABLES

### Console Output

```
 Dataset overview (shape, columns, stats)
 Missing value analysis
 3 GroupBy analyses (category, region, month)
 7 Key insights (top products, worst category, best region, etc.)
 Pivot table preview
 Additional metadata (price, quantity, product distribution)
```

### Excel Report: Sales_Analysis_Report.xlsx

```
Sheet 1: Summary
 - Total Revenue
 - Total Orders
 - Average Order Value
 - Best Region, Worst Category
 - Date Range

Sheet 2: Category Analysis
 - Sales by category
 - Order counts
 - Average values

Sheet 3: Region Analysis
 - Sales by region
 - Order counts
 - Average values

Sheet 4: Top 5 Products
 - Product rankings
 - Revenue per product

Sheet 5: Pivot Table
 - Region × Category matrix
 - Row and column totals

Sheet 6: Monthly Trend
 - Sales over time
 - Seasonal patterns

Sheet 7: Raw Data Sample
 - First 1000 processed rows
 - All columns for verification
```

---

## RECOMMENDED LEARNING PATH

### For Beginners

1. Read [README.md](README.md) - Understand what the project does
2. Check [QUICKSTART.py](QUICKSTART.py) - Verify your environment
3. Run [sales_dashboard_analysis.py](sales_dashboard_analysis.py) - See results
4. Read [CODE_EXPLANATION.md](CODE_EXPLANATION.md) - Understand the code
5. Use [TASK_CHECKLIST.md](TASK_CHECKLIST.md) - Track what you learned

### For Intermediate Users

1. Skim [README.md](README.md)
2. Run main script
3. Review [CUSTOMIZATION_GUIDE.md](CUSTOMIZATION_GUIDE.md)
4. Modify script for your data
5. Add custom analyses

### For Advanced Users

1. Run script on your own dataset
2. Extend with visualizations
3. Add statistical analysis
4. Build predictive models
5. Automate report generation

---

## LEARNING OUTCOMES

After completing this project, you'll be able to:

**Data Handling**

- Load CSV files into pandas DataFrames
- Inspect data structure and quality
- Handle missing values appropriately
- Convert and manipulate date columns

**Data Analysis**

- Perform groupby aggregations
- Create pivot tables for cross-dimensional analysis
- Identify top and bottom performers
- Extract business metrics from raw data

**Reporting**

- Export results to Excel with multiple sheets
- Format numbers with currency symbols
- Create executive summaries
- Present findings professionally

**Problem Solving**

- Debug data pipeline issues
- Handle edge cases (missing data, invalid dates)
- Verify data integrity
- Customize analysis for different datasets

---

## TROUBLESHOOTING QUICK LINKS

### Installation Issues

→ See [QUICKSTART.py](QUICKSTART.py) diagnostic section

### Column Name Errors

→ See [CUSTOMIZATION_GUIDE.md](CUSTOMIZATION_GUIDE.md) - Customizing Column Names

### Understanding the Code

→ See [CODE_EXPLANATION.md](CODE_EXPLANATION.md) - Detailed Section Breakdown

### Adapting for Different Data

→ See [CUSTOMIZATION_GUIDE.md](CUSTOMIZATION_GUIDE.md) - Entire guide

### Tracking Progress

→ See [TASK_CHECKLIST.md](TASK_CHECKLIST.md) - Check off completed items

---

## ⏱ TIME BREAKDOWN

| Activity                  | Time          |
| ------------------------- | ------------- |
| Reading README            | 5 min         |
| Installing dependencies   | 2 min         |
| Running script            | 1-5 min       |
| Reviewing console output  | 5 min         |
| Reviewing Excel report    | 5 min         |
| Reading code explanations | 10 min        |
| Customizing for own data  | 15-30 min     |
| **TOTAL**                 | **43-62 min** |

---

## PANDAS CONCEPTS COVERED

- **Data Loading:** `pd.read_csv()`
- **Inspection:** `.head()`, `.info()`, `.describe()`, `.shape`
- **Cleaning:** `.isnull()`, `.fillna()`, `.dropna()`
- **DateTime:** `pd.to_datetime()`, `.dt` accessor
- **Transformation:** column creation, arithmetic operations
- **GroupBy:** `.groupby()`, `.agg()`, `.sum()`, `.mean()`, etc.
- **Pivot:** `.pivot_table()`, multi-dimensional analysis
- **Export:** `.to_excel()`, `.to_csv()`
- **Filtering:** boolean indexing, `.loc[]`, `.iloc[]`
- **Sorting:** `.sort_values()`, `.nlargest()`, `.nsmallest()`

---

## NAVIGATION GUIDE

| Question                   | Answer                                                     |
| -------------------------- | ---------------------------------------------------------- |
| Where do I start?          | [README.md](README.md)                                     |
| How do I run it?           | [QUICKSTART.py](QUICKSTART.py)                             |
| What's in each section?    | [CODE_EXPLANATION.md](CODE_EXPLANATION.md)                 |
| How do I customize it?     | [CUSTOMIZATION_GUIDE.md](CUSTOMIZATION_GUIDE.md)           |
| How do I track progress?   | [TASK_CHECKLIST.md](TASK_CHECKLIST.md)                     |
| What do I need to install? | [requirements.txt](requirements.txt)                       |
| Where's the main code?     | [sales_dashboard_analysis.py](sales_dashboard_analysis.py) |

---

## NEXT PROJECTS

After mastering this project, try:

1. **Sales Dashboard with Visualizations** (Matplotlib/Seaborn)

- Add charts to Excel report
- Create visual dashboards
- Build trend analysis plots

2. **Interactive Dashboard** (Plotly/Dash)

- Web-based interactive dashboard
- Real-time filters
- Dynamic charts

3. **Predictive Analytics**

- Forecast future sales
- Customer segmentation
- Anomaly detection

4. **Automated Reporting**

- Schedule daily/weekly reports
- Email auto-delivery
- Parameter-driven analysis

5. **Advanced Analytics**

- Statistical testing
- Correlation analysis
- A/B testing framework

---

## PROJECT COMPLETION CHECKLIST

- [ ] All files present in folder
- [ ] Dependencies installed (`pip install -r requirements.txt`)
- [ ] Script runs without errors (`python sales_dashboard_analysis.py`)
- [ ] Console output displays all metrics
- [ ] Excel report generated successfully
- [ ] README.md read and understood
- [ ] Code explanation reviewed for 2-3 sections
- [ ] Customization guide reviewed
- [ ] Attempted at least one customization
- [ ] Results understood and documented

---

**Project Version:** 1.0
**Created:** 2026-03-02
**Status:** Complete and Production-Ready
**Difficulty:** Beginner to Intermediate

---

## QUICK HELP

### I'm completely new to Python

**Start here:** [README.md](README.md) → [QUICKSTART.py](QUICKSTART.py) → Run main script

### I know Python but new to pandas

**Start here:** [CODE_EXPLANATION.md](CODE_EXPLANATION.md) - Read Sections 1-5 carefully

### I want to use my own data

**Start here:** [CUSTOMIZATION_GUIDE.md](CUSTOMIZATION_GUIDE.md) - Follow step-by-step

### Script has errors

**Check:**

1. All dependencies installed? → [QUICKSTART.py](QUICKSTART.py)
2. Column names correct? → [CUSTOMIZATION_GUIDE.md](CUSTOMIZATION_GUIDE.md)
3. CSV file present? → Check `LARGE_sales_dataset.csv` in folder

---

**You're ready to begin! Start with [README.md](README.md)**
