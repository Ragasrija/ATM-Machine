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