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

def login(name, pin):
    return name in accounts and accounts [name]["pin"]==pin