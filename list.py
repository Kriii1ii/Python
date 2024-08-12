racers=["Max","Lewis","Charles","Carlos","Nico","Kevin"]
print(racers)

racers.append("Checo")
print(racers)

racers2=["Yuki","Zhou"]
racers.extend(racers2)
print(racers)

racers.insert(2,"George")
print(racers)

racers.remove("Checo")
print(racers)

racers.pop(0)
print(racers)

print(racers[2:5])



racers.reverse()
print(racers)

print(len(racers))

print(min(racers))

print(max(racers))

racers2 = racers.copy()
print(racers2)

index = racers.index("Lewis")
print(index)

print(racers.clear())




