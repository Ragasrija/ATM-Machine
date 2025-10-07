def deposit(name, pin, amount):
    """Deposit money into account."""
    account = find_account(name, pin)
    if account:
        account["balance"] += amount
        account["transactions"].append(f"Deposited ₹{amount:.2f}")
        print(f"\n💰 Deposit successful! New balance: ₹{account['balance']:.2f}")
    else:
        print("\n❌ Invalid name or PIN.")