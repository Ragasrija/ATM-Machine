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