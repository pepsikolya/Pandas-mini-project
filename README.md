# Employee Data Manager

A command line tool for loading, cleaning, and analyzing employee data from CSV file. Built with Python and basic pandas as part of ## learning data analysis fundamentals.

## Features

**Data cleaning** — removes duplicate records and handles missing values
**Statistics** — median salary/age, filtering by age and salary, mean salary grouped by position
**Employee search** — case insensitive name lookup
**Export** — saves cleaned data back to CSV

## Getting Started

### Requirements

```
pandas
```

Install with:

```bash
pip install -r requirements.txt
```

The script expects a `data.csv` file in the same directory with the following columns: `Name`, `Position`, `Salary`, `Age`.

You will be prompted with a menu:

```
--- MENU ---
1. Basic Statistics
2. Search Employee
3. Save and Exit
```

## What I Learned

- Using `pandas` for data cleaning (duplicates, NaN handling)
- Filtering and grouping DataFrames
- Structuring a Python project with functions
- Working with CSV files as input/output

## Tech Stack

![Python](https://img.shields.io/badge/Python-3.x-blue)
![pandas](https://img.shields.io/badge/pandas-data%20analysis-lightgrey)
