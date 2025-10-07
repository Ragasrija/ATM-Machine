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
