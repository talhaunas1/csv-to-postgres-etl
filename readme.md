# CSV to PostgreSQL ETL Pipeline

A batch ETL pipeline in Python that extracts retail sales data from CSV, cleans it with pandas, and loads it into PostgreSQL.

## Tech stack
Python, pandas, SQLAlchemy, PostgreSQL, Jupyter

## Pipeline
- **Extract:** read 9,994 sales records from CSV
- **Transform:** standardised column names, removed duplicates, parsed day-first dates, preserved postal-code leading zeros
- **Load:** wrote to a PostgreSQL `sales` table
- **Validate:** row-count check between source and database

## Data quality issues found
- Dates were in DD-MM-YYYY format; default parsing would have silently swapped day and month.
- Postal codes were read as numbers, dropping leading zeros (e.g. 01453 → 1453). Fixed by storing them as text.

## How to run
1. Download the Superstore Sales dataset from Kaggle and save it as `data/superstore.csv`
2. `pip install -r requirements.txt`
3. Copy `.env.example` to `.env` and add your database details
4. `python etl.py`