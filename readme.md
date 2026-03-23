SQL Sales Data Automation with Python

🚀 Overview

This project automates the end-to-end process of transforming raw CSV sales data into actionable insights using Python and SQL.

It demonstrates how to build a simple data pipeline that:

Cleans and processes raw data
Stores it in a structured SQLite database
Executes analytical SQL queries
Generates a readable report automatically
🧠 Key Features
📂 CSV Ingestion – Reads raw data from a CSV file
🧹 Data Cleaning – Handles missing or inconsistent values
🗄️ SQLite Integration – Stores structured data in a relational database
🔍 SQL Analysis – Runs multiple queries for insights
📄 Automated Reporting – Outputs results to a .txt report
🛠️ Tech Stack
Python
SQLite
CSV module
Type Hints (for clean, maintainable code)

📁 Project Structure
├── amazonsale1.csv   # Input dataset
├── sales.db          # Generated SQLite database
├── report.txt        # Final analysis report
├── main.py           # Main automation script

⚙️ How It Works

1. Database Reset

Removes any existing database to ensure a clean run.

2. Database Creation

Creates a sales table with relevant fields:

Order ID
Date
Status
Fulfilment

3. Data Insertion
Reads CSV file
Cleans missing values
Inserts data into SQLite

4. SQL Queries

Executes analytical queries such as:

Total number of orders
Number of cancelled orders
Orders grouped by status
Orders grouped by fulfilment type

5. Report Generation

Creates a structured text report with all results.

▶️ How to Run
Clone the repository:
git clone https://github.com/your-username/your-repo.git
cd your-repo
Add your CSV file (or use the existing one)
Run the script:
python main.py
Check the output:
report.txt

📌 Example Output
=== SALES ANALYSIS REPORT ===

Total Orders:
  → 1250

Cancelled Orders:
  → 230

Orders by Status:
  → Shipped: 700
  → Cancelled: 230
  → Pending: 320

💡 What This Project Demonstrates
Building a simple ETL pipeline
Writing efficient SQL queries
Handling real-world messy data
Automating repetitive data workflows
Writing clean, structured Python code

🎯 Future Improvements
Add data visualization (e.g., dashboards)
Export reports in CSV or PDF
Use a more scalable database (PostgreSQL)
Build a web interface for interaction
📬 Contact

Feel free to connect or reach out if you want to discuss this project or opportunities.
