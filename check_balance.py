def check_balance(name, pin):
    """Check and display account balance."""
    account = find_account(name, pin)
    if account:
        print(f"\n✅ {account['name']}, your current balance is ₹{account['balance']:.2f}")
    else:
        print("\n❌ Invalid name or PIN.")