dictionary1 = {"Max": 1, "Lewis": 44, "Checo": 11}
dictionary2 = {"Charles": 16, "Carlos": 55, "George": 63, "Daniel": 3}

keys_not_in_dictionary1 = [key for key in dictionary2 if key not in dictionary1]
print("Keys that are not in dictionary1:", keys_not_in_dictionary1)  