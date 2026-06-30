# Relational Expense Tracker & Financial Management Utility

A structured, production-grade Python CLI backend ledger designed to track, categorize, and calculate transactional financial data. This project transitions standard flat-file data persistence (CSV) into a robust, relational database architecture using **SQLite**.

## 🚀 Engineered Enhancements
* **Relational Storage:** Migrated from volatile string-parsing file inputs (`.csv`) to a normalized database schema, ensuring data integrity across application lifetimes.
* **Algorithmic & Database Efficiency:** Delegated computational grouping and summing from application memory ($O(N)$ runtime) to the SQL engine using optimized `SUM` and `GROUP BY` data aggregations.
* **Security & Exploitation Prevention:** Implemented fully **parameterized queries** (`?` placeholders) to completely mitigate SQL Injection vulnerabilities from user console entries.
* **Defensive Input Validation:** Built robust `try-except` validation execution loops to handle malformed, out-of-bounds, or non-numeric entries gracefully, guaranteeing zero application crashes.
* **Centralized Data Layer:** Developed a modular query runner utilizing Python context managers (`with` statements) to securely handle database connections, cursor tracking, auto-committing, and resource teardown.

## 📊 Database Architecture (Schema)
The SQLite engine enforces a strict schema for transaction validation:

* `id` (INTEGER, Primary Key, Auto-Increment) - Unique row identifier.
* `name` (TEXT, Not Null) - The text description of the transaction.
* `amount` (REAL, Not Null) - Numeric floating-point transaction value.
* `category` (TEXT, Not Null) - Categorical string label.
* `date` (TEXT, Default CURRENT_TIMESTAMP) - Automated chronological log entry.

## 🛠️ Tech Stack & Concepts Applied
* **Language:** Python 3.11+
* **Database Engine:** SQLite 3
* **Core Concepts:** Parameterized Queries, Relational Schemas, Computational Aggregations, Context Managers, Defensive Programming.

## 🏃‍♂️ Core Features & Interface
The interactive command-line interface provides users with an entry menu to manage transactional workflows:
1. **➕ Add New Expense:** Instantiates a secure record transaction and dynamically tracks category metrics.
2. **📜 View Complete History:** Queries individual data records sequentially, descending by chronological timestamp.
3. **📊 View Metric Aggregations:** Evaluates real-time financial tracking statistics, including categorical overviews, absolute totals, and variable daily budget burn-rates based on the remaining calendar days in the month.

### How to Run Locally

1. Clone the repository:
   ```bash
   git clone [https://github.com/YOUR_USERNAME/Expense-app.git](https://github.com/YOUR_USERNAME/Expense-app.git)
   cd Expense-app

