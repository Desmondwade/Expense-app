import sqlite3
import calendar
import datetime
from expense import Expense

DB_NAME = "expenses.db"

def run_query(query, params=()):
    #Helper function to get ride of repetitive connection and closing boilerplate.
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute(query, params)
        return cursor.fetchall()

def initialize_db():
    """Sets up the database table using the centralized query runner."""
    run_query("""
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            amount REAL NOT NULL,
            category TEXT NOT NULL,
            date TEXT DEFAULT CURRENT_TIMESTAMP
        )
    """)

def get_user_expense():
    #Prompts and validates user expense details cleanly.
    print("\n🎯 Getting User Expense")
    name = input("Enter expense name: ").strip()
    
    # input validation loops
    while True:
        try:
            amount = float(input("Enter expense amount: "))
            if amount >= 0: break
            print("Amount cannot be negative.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    categories = ["🍔 Food", "🏠 Home", "💼 Work", "🎮 Fun", "✨ Misc"]
    while True:
        print("\nSelect a category: ")
        for i, cat in enumerate(categories, 1):
            print(f"  {i}. {cat}")
        
        try:
            idx = int(input(f"Enter a category number [1 - {len(categories)}]: ")) - 1
            if idx in range(len(categories)):
                return Expense(name=name, category=categories[idx], amount=amount)
            print("Invalid choice. Try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def save_expense_to_db(expense: Expense):
    """Saves the record using a clean parameterized query."""
    run_query(
        "INSERT INTO expenses (name, amount, category) VALUES (?, ?, ?)",
        (expense.name, expense.amount, expense.category)
    )
    print(f"\n💾 Saved '{expense.name}' (${expense.amount:.2f}) to the SQL database!")

def summarize_expenses_from_db(budget: float):
    """Aggregates statistics directly through SQL metrics."""
    rows = run_query("SELECT category, SUM(amount) FROM expenses GROUP BY category")
    
    print("\n📊 Expenses By Category (Calculated via SQL Engine)")
    print("-" * 45)
    
    total_spent = sum(amount for _, amount in rows)
    for category, amount in rows:
        print(f"  🔹 {category}: ${amount:.2f}")
        
    print("-" * 45)
    print(f"💵 Total Spent: ${total_spent:.2f}\n📉 Budget Remaining: ${(budget - total_spent):.2f}")
    
    # Calculate daily timeline budget metrics cleanly
    now = datetime.datetime.now()
    remaining_days = calendar.monthrange(now.year, now.month)[1] - now.day
    daily = (budget - total_spent) / max(remaining_days, 1)
    print(f"\033[92m📅 Budget Per Day: ${daily:.2f}\033[0m")

def view_all_expenses():
    """Queries and displays every transactional record neatly formatted."""
    rows = run_query("SELECT id, name, amount, category, date FROM expenses ORDER BY date DESC")
    
    if not rows:
        return print("\n📜 No transactions found in the database.")

    print("\n📜 COMPLETE TRANSACTION HISTORY")
    print(f"{'ID':<5} | {'Name':<15} | {'Amount':<10} | {'Category':<12} | {'Date':<20}")
    print("-" * 70)
    for idx, name, amount, cat, date in rows:
        print(f"{idx:<5} | {name:<15} | ${amount:<9.2f} | {cat:<12} | {date:<20}")

def main():
    initialize_db()
    
    print("\n🏛  Expense Tracker API & Management Utility")
    print("=" * 45)
    print("  1. ➕ Add a new expense\n  2. 📜 View complete transaction history\n  3. 📊 View categorical metric summaries")
    print("=" * 45)
    
    choice = input("Enter choice (1, 2, or 3): ").strip()
    if choice == "1":
        save_expense_to_db(get_user_expense())
        summarize_expenses_from_db(budget=2000)
    elif choice == "2":
        view_all_expenses()
    elif choice == "3":
        summarize_expenses_from_db(budget=2000)
    else:
        print("Invalid choice. Exiting program.")

if __name__ == "__main__":
    main()

