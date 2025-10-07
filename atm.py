# ============================================================
# ATM Machine Project – Step-by-Step Implementation
# ============================================================

# ---------- STEP 1: Setup ----------

# Predefined 10 user accounts: name, pin, balance, transactions
accounts = [
    {"name": "Alice", "pin": "1111", "balance": 5000.0, "transactions": []},
    {"name": "Bob", "pin": "2222", "balance": 3000.0, "transactions": []},
    {"name": "Charlie", "pin": "3333", "balance": 4500.0, "transactions": []},
    {"name": "David", "pin": "4444", "balance": 2500.0, "transactions": []},
    {"name": "Eva", "pin": "5555", "balance": 10000.0, "transactions": []},
    {"name": "Frank", "pin": "6666", "balance": 7500.0, "transactions": []},
    {"name": "Grace", "pin": "7777", "balance": 1200.0, "transactions": []},
    {"name": "Henry", "pin": "8888", "balance": 6700.0, "transactions": []},
    {"name": "Isla", "pin": "9999", "balance": 8900.0, "transactions": []},
    {"name": "Jack", "pin": "0000", "balance": 3500.0, "transactions": []}
]


# ---------- Empty Function Definitions ----------

def find_account(name, pin):
    """Helper function to locate an account by name and PIN."""
    for acc in accounts:
        if acc["name"].lower() == name.lower() and acc["pin"] == pin:
            return acc
    return None


def check_balance(name, pin):
    """Check and display account balance."""
    account = find_account(name, pin)
    if account:
        print(f"\n✅ {account['name']}, your current balance is ₹{account['balance']:.2f}")
    else:
        print("\n❌ Invalid name or PIN.")


def deposit(name, pin, amount):
    """Deposit money into account."""
    account = find_account(name, pin)
    if account:
        account["balance"] += amount
        account["transactions"].append(f"Deposited ₹{amount:.2f}")
        print(f"\n💰 Deposit successful! New balance: ₹{account['balance']:.2f}")
    else:
        print("\n❌ Invalid name or PIN.")


def withdraw(name, pin, amount):
    """Withdraw money from account."""
    account = find_account(name, pin)
    if account:
        if amount <= account["balance"]:
            account["balance"] -= amount
            account["transactions"].append(f"Withdrew ₹{amount:.2f}")
            print(f"\n✅ Withdrawal successful! New balance: ₹{account['balance']:.2f}")
        else:
            print("\n⚠️ Insufficient balance!")
    else:
        print("\n❌ Invalid name or PIN.")


def transaction_history(name, pin):
    """Show deposit and withdrawal history."""
    account = find_account(name, pin)
    if account:
        print(f"\n📜 Transaction history for {account['name']}:")
        if len(account["transactions"]) == 0:
            print("No transactions yet.")
        else:
            for t in account["transactions"]:
                print(" -", t)
    else:
        print("\n❌ Invalid name or PIN.")


# ---------- STEP 2–6: Main Program Loop ----------

def main():
    print("=======================================")
    print("💳 Welcome to Python ATM Machine")
    print("=======================================")

    while True:
        print("\n----------- MENU -----------")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Transaction History")
        print("5. Exit")
        print("-----------------------------")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            name = input("Enter your name: ")
            pin = input("Enter your 4-digit PIN: ")
            check_balance(name, pin)

        elif choice == "2":
            name = input("Enter your name: ")
            pin = input("Enter your 4-digit PIN: ")
            try:
                amount = float(input("Enter amount to deposit: ₹"))
                deposit(name, pin, amount)
            except ValueError:
                print("⚠️ Please enter a valid amount.")

        elif choice == "3":
            name = input("Enter your name: ")
            pin = input("Enter your 4-digit PIN: ")
            try:
                amount = float(input("Enter amount to withdraw: ₹"))
                withdraw(name, pin, amount)
            except ValueError:
                print("⚠️ Please enter a valid amount.")

        elif choice == "4":
            name = input("Enter your name: ")
            pin = input("Enter your 4-digit PIN: ")
            transaction_history(name, pin)

        elif choice == "5":
            print("\n🙏 Thank you for using Python ATM. Goodbye!")
            break

        else:
            print("❌ Invalid option. Please choose between 1–5.")


# ---------- STEP 7: Run the program ----------
if __name__ == "__main__":
    main()
