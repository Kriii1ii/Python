Dict_value = {
    'drink': 'Americano', 
    'food': 'Pizza',   
    'color': 'yellow',
    'age': 20
}
print(Dict_value)

Dict_value["movie"] = "Terminator"
print(Dict_value)

Dict_value["food"] = "Tiramisu"
print(Dict_value)

del Dict_value["color"]
print(Dict_value)

key = "food"

if key in Dict_value:
    print("The key is present.")
else:
    print("The key is not present.")


Dict_value.clear()
print(Dict_value)