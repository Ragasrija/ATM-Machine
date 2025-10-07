# ATM-Machine
ATM Machine – Python Project

A simple, interactive ATM simulation system built using Python and SQLite3 for data storage.
This project allows users to check balances, deposit money, withdraw funds, and view transaction history — all through a user-friendly console (and optionally a Tkinter GUI).

🚀 Features

✅ 10 predefined user accounts
✅ Secure PIN-based login system
✅ Check account balance
✅ Deposit and withdraw money
✅ Transaction history (deposits & withdrawals)
✅ SQLite database integration (atm.db)
✅ Data persistence (balances saved even after restart)
✅ Optional GUI version using Tkinter

🧰 Tech Stack

Language: Python 3.x

Database: SQLite3

Libraries Used:

sqlite3 (for database)

tkinter (optional, for GUI version)

📁 Project Structure
ATM-Machine/
│
├── atm_machine.py        # Main console-based ATM program
├── database_setup.py     # Creates SQLite database and tables
├── atm.db                # SQLite database file (auto-created)
├── README.md             # Project documentation
└── (optional) atm_gui.py # Tkinter GUI version

⚙️ Setup Instructions
1️⃣ Clone the repository
git clone https://github.com/Ragasrija/ATM-Machine.git
cd ATM-Machine

2️⃣ Create the SQLite database

Run this once to create your tables:

python database_setup.py

3️⃣ (Optional) Add sample users
import sqlite3
conn = sqlite3.connect('atm.db')
cursor = conn.cursor()

users = [
    ("Alice", "1111", 5000.0),
    ("Bob", "2222", 3000.0),
    ("Charlie", "3333", 4000.0)
]
cursor.executemany("INSERT INTO users (name, pin, balance) VALUES (?, ?, ?)", users)
conn.commit()
conn.close()

4️⃣ Run the ATM
python atm_machine.py

5️⃣ (Optional) Run the GUI version
python atm_gui.py

🧑‍💻 How to Use

Run the ATM program.

Enter your Name and 4-digit PIN.

Choose an option:

1 → Check Balance

2 → Deposit Money

3 → Withdraw Money

4 → View Transaction History

5 → Exit

All data (balances and transactions) are saved automatically to atm.db.

🧠 Example Run
💳 Welcome to Python ATM Machine

----- MENU -----
1. Check Balance
2. Deposit Money
3. Withdraw Money
4. Transaction History
5. Exit

Enter choice (1–5): 1
Enter name: Alice
Enter PIN: 1111
✅ Alice, your current balance is ₹5000.00
