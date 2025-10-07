def find_account(name, pin):
    """Helper function to locate an account by name and PIN."""
    for acc in accounts:
        if acc["name"].lower() == name.lower() and acc["pin"] == pin:
            return acc
    return None
