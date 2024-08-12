d = {} #d is khali dictionary

def insert_key_value(key, value):
    if key not in d:
        d[key] = value

insert_key_value("driver", "Max Verstappen") #driver vaneko key and Max Verstappen value
insert_key_value("age", 26)
insert_key_value("driver_number", 1)
insert_key_value("championships", 3)
insert_key_value("driver", "Lewis Hamilton")  # This will not overwrite the existing key
print(d)  