# Mutual Fund Analytics Project
Mutual Fund Data Analytics Project
Overview

This project focuses on data ingestion, exploration, validation, and analysis of Mutual Fund datasets. The objective is to build a structured data pipeline that loads historical mutual fund data, fetches live NAV information from public APIs, performs data quality checks, and prepares the foundation for further analytics and dashboard development.

Project Structure
mutual-fund-analysis/
│
├── data/
│   ├── raw/
│   │   ├── fund_master.csv
│   │   ├── nav_history.csv
│   │   ├── hdfc_top100_nav.csv
│   │   ├── 119551.csv
│   │   ├── 120503.csv
│   │   ├── 118632.csv
│   │   ├── 119092.csv
│   │   └── 120841.csv
│   │
│   └── processed/
│
├── notebooks/
├── sql/
├── dashboard/
├── reports/
│   └── data_quality_summary.txt
│
├── data_ingestion.py
├── live_nav_fetch.py
├── requirements.txt
├── README.md
└── .gitignore
Objectives
Load and inspect multiple mutual fund datasets.
Perform basic data quality assessment.
Fetch live NAV data using external APIs.
Store raw data in a structured format.
Validate AMFI scheme codes across datasets.
Maintain project version control using Git and GitHub.
Technologies Used
Python 3
Pandas
NumPy
Requests
SQLAlchemy
SciPy
Matplotlib
Seaborn
Plotly
Jupyter Notebook
Git
GitHub
Installation
Clone the Repository
git clone https://github.com/<your-username>/mutual-fund-analysis.git
cd mutual-fund-analysis
Create Virtual Environment
python3 -m venv venv

Activate virtual environment:

macOS / Linux
source venv/bin/activate
Windows
venv\Scripts\activate
Install Dependencies
pip install -r requirements.txt
Dataset Ingestion

The data_ingestion.py script loads all CSV files from the data/raw/ directory and performs basic exploration.

Features
Reads all CSV files automatically.
Displays:
Dataset shape
Column data types
First five records
Helps identify potential data issues.
Run
python3 data_ingestion.py
Live NAV Data Collection

The live_nav_fetch.py script fetches mutual fund NAV history from the MF API.

API Source

https://api.mfapi.in

Funds Covered
Fund Name	AMFI Code
HDFC Top 100 Direct	125497
SBI Bluechip Fund	119551
ICICI Prudential Bluechip Fund	120503
Nippon India Large Cap Fund	118632
Axis Bluechip Fund	119092
Kotak Bluechip Fund	120841
Run
python3 live_nav_fetch.py
Output

CSV files are saved in:

data/raw/
Data Quality Validation

The project includes validation checks to assess data quality.

Checks Performed
Missing value analysis
Duplicate record detection
Data type validation
AMFI scheme code verification
Dataset consistency checks
Output

Results are documented in:

reports/data_quality_summary.txt
AMFI Code Validation

Validation ensures that all scheme codes present in the master dataset are also available in the NAV history dataset.

Example validation:

missing_codes = master_codes - nav_codes

This helps identify incomplete historical NAV coverage.

Key Deliverables
Python Scripts
data_ingestion.py
live_nav_fetch.py
Documentation
README.md
data_quality_summary.txt
Configuration
requirements.txt
Version Control
Git repository
GitHub repository
Future Enhancements
Automated ETL pipeline
Database integration
NAV trend analysis
Risk-return analytics
Portfolio comparison dashboard
Interactive Plotly visualizations
Power BI / Tableau dashboard integration
Sample Commands

Run ingestion:

python3 data_ingestion.py

Run NAV collection:

python3 live_nav_fetch.py

Check Git status:

git status

Commit changes:

git add .
git commit -m "Day 1: Data ingestion complete"

Push to GitHub:

git push origin main
Learning Outcomes

Through this project, the following skills are demonstrated:

Python programming
Data ingestion techniques
API integration
Data quality assessment
Data exploration using Pandas
Git and GitHub workflows
Project structuring for analytics applications
