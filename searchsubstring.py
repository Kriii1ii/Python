def search_substring(string, substring):
    if substring in string:
        return True
    else:
        return False

string = "Americano, Latte, Cappuccino, Espresso, Doppio, Cortado"
substring = "Latte"
print(search_substring(string, substring))  # Output: True