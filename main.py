from typing import List, Tuple
import sqlite3
import csv
import os

DB_NAME: str = "sales.db"
FILE: str = "amazonsale1.csv"


def reset_database() -> None:
    if os.path.exists(DB_NAME):
        os.remove(DB_NAME)


def create_database() -> sqlite3.Connection:
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE sales (
        order_id TEXT,
        date TEXT,
        status TEXT,
        fulfilment TEXT
    )
    """)

    conn.commit()
    return conn


def clean_value(value: str) -> str:
    value = (value or "").strip()
    return value if value else "Unknown"


def insert_csv_to_db(conn: sqlite3.Connection, filename: str) -> None:
    cursor = conn.cursor()

    with open(filename, newline="", encoding="utf-8", errors="ignore") as f:
        reader = csv.DictReader(f, delimiter=";")

        for row in reader:
            try:
                cursor.execute("""
                INSERT INTO sales (order_id, date, status, fulfilment)
                VALUES (?, ?, ?, ?)
                """, (
                    clean_value(row.get("Order ID")),
                    clean_value(row.get("Date")),
                    clean_value(row.get("Status")),
                    clean_value(row.get("Fulfilment"))
                ))
            except Exception:
                continue

    conn.commit()


def run_queries(conn: sqlite3.Connection) -> List[Tuple[str, List[Tuple]]]:
    cursor = conn.cursor()

    queries = [
        ("Total Orders", "SELECT COUNT(*) FROM sales"),
        ("Cancelled Orders", "SELECT COUNT(*) FROM sales WHERE status = 'Cancelled'"),
        ("Orders by Status", """
            SELECT status, COUNT(*) 
            FROM sales
            WHERE status != 'Unknown'
            GROUP BY status
            ORDER BY COUNT(*) DESC
        """),
        ("Orders by Fulfilment", """
            SELECT fulfilment, COUNT(*) 
            FROM sales
            WHERE fulfilment != 'Unknown'
            GROUP BY fulfilment
            ORDER BY COUNT(*) DESC
        """)
    ]

    results: List[Tuple[str, List[Tuple]]] = []

    for title, query in queries:
        cursor.execute(query)
        data = cursor.fetchall()
        results.append((title, data))

    return results


def generate_report(results: List[Tuple[str, List[Tuple]]]) -> None:
    with open("report.txt", "w", encoding="utf-8") as f:
        f.write("=== SALES ANALYSIS REPORT ===\n\n")

        for title, data in results:
            f.write(f"{title}:\n")

            if not data:
                f.write("  No data available\n\n")
                continue

            for row in data:
                if len(row) == 1:
                    f.write(f"  → {row[0]}\n")
                else:
                    f.write(f"  → {row[0]}: {row[1]}\n")

            f.write("\n")


def main() -> None:
    print("Resetting database...")
    reset_database()

    print("Creating database...")
    conn = create_database()

    print(f"Inserting data from {FILE}...")
    insert_csv_to_db(conn, FILE)

    print("Running queries...")
    results = run_queries(conn)

    print("Generating report...")
    generate_report(results)

    conn.close()

    print("\nDone. Your report is ready → report.txt")


if __name__ == "__main__":
    main()
