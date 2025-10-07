import tkinter as tk
from tkinter import messagebox
import json
import os

DATA_FILE = "users.json"

# ---------- Data Handling ----------
def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    else:
        return {"1234": {"name": "Alice", "balance": 1000.0}}

def save_data(data):
    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)

# ---------- ATM GUI Class ----------
class ATMApp:
    def __init__(self, root):
        self.root = root
        self.root.title("🏦 Python Bank ATM")
        self.root.geometry("400x400")
        self.root.config(bg="#e3f2fd")

        self.data = load_data()
        self.current_user = None

        self.login_screen()

    # -------- Login Screen --------
    def login_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        tk.Label(self.root, text="Welcome to Python Bank ATM 💳",
                 font=("Arial", 14, "bold"), bg="#e3f2fd").pack(pady=20)

        tk.Label(self.root, text="Enter 4-digit PIN:", bg="#e3f2fd").pack()
        self.pin_entry = tk.Entry(self.root, show="*", justify="center")
        self.pin_entry.pack(pady=5)

        tk.Button(self.root, text="Login", command=self.login, width=15,
                  bg="#1976d2", fg="white").pack(pady=10)
        tk.Button(self.root, text="Create New Account", command=self.create_account_screen,
                  width=20, bg="#64b5f6").pack(pady=5)

    # -------- Create Account --------
    def create_account_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        tk.Label(self.root, text="Create a New Account 🧾",
                 font=("Arial", 14, "bold"), bg="#e3f2fd").pack(pady=20)

        tk.Label(self.root, text="Enter your Name:", bg="#e3f2fd").pack()
        self.name_entry = tk.Entry(self.root)
        self.name_entry.pack(pady=5)

        tk.Label(self.root, text="Choose a 4-digit PIN:", bg="#e3f2fd").pack()
        self.new_pin_entry = tk.Entry(self.root, show="*", justify="center")
        self.new_pin_entry.pack(pady=5)

        tk.Button(self.root, text="Create Account", command=self.create_account,
                  width=18, bg="#388e3c", fg="white").pack(pady=10)
        tk.Button(self.root, text="Back to Login", command=self.login_screen,
                  width=15, bg="#64b5f6").pack(pady=5)

    def create_account(self):
        name = self.name_entry.get()
        pin = self.new_pin_entry.get()
        if not pin.isdigit() or len(pin) != 4:
            messagebox.showerror("Error", "PIN must be 4 digits.")
            return
        data = load_data()
        if pin in data:
            messagebox.showerror("Error", "PIN already exists.")
            return
        data[pin] = {"name": name, "balance": 0.0}
        save_data(data)
        messagebox.showinfo("Success", f"Account created for {name}!")
        self.login_screen()

    # -------- Login Function --------
    def login(self):
        pin = self.pin_entry.get()
        if pin in self.data:
            self.current_user = pin
            self.dashboard()
        else:
            messagebox.showerror("Invalid PIN", "Account not found!")

    # -------- Dashboard --------
    def dashboard(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        user = self.data[self.current_user]

        tk.Label(self.root, text=f"Welcome, {user['name']} 👋",
                 font=("Arial", 14, "bold"), bg="#e3f2fd").pack(pady=20)

        self.balance_label = tk.Label(self.root, text=f"Balance: ₹{user['balance']}",
                                      font=("Arial", 12), bg="#e3f2fd")
        self.balance_label.pack(pady=10)

        tk.Button(self.root, text="Deposit", command=self.deposit_screen,
                  width=15, bg="#1976d2", fg="white").pack(pady=5)
        tk.Button(self.root, text="Withdraw", command=self.withdraw_screen,
                  width=15, bg="#0288d1", fg="white").pack(pady=5)
        tk.Button(self.root, text="Logout", command=self.logout,
                  width=15, bg="#f44336", fg="white").pack(pady=20)

    # -------- Deposit Screen --------
    def deposit_screen(self):
        amount = tk.simpledialog.askfloat("Deposit", "Enter amount to deposit:")
        if amount and amount > 0:
            self.data[self.current_user]["balance"] += amount
            save_data(self.data)
            self.balance_label.config(
                text=f"Balance: ₹{self.data[self.current_user]['balance']}")
            messagebox.showinfo("Success", f"₹{amount} deposited successfully!")

    # -------- Withdraw Screen --------
    def withdraw_screen(self):
        amount = tk.simpledialog.askfloat("Withdraw", "Enter amount to withdraw:")
        if amount and amount > 0:
            balance = self.data[self.current_user]["balance"]
            if amount <= balance:
                self.data[self.current_user]["balance"] -= amount
                save_data(self.data)
                self.balance_label.config(
                    text=f"Balance: ₹{self.data[self.current_user]['balance']}")
                messagebox.showinfo("Success", f"₹{amount} withdrawn successfully!")
            else:
                messagebox.showerror("Error", "Insufficient balance!")

    # -------- Logout --------
    def logout(self):
        self.current_user = None
        self.data = load_data()
        self.login_screen()


# ---------- Run App ----------
if __name__ == "__main__":
    root = tk.Tk()
    app = ATMApp(root)
    root.mainloop()
