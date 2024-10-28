companions = ["Astarion", "Gale", "Karlach", "Lae'zel",
              "Shadowheart", "Wyll", "The Dark Urge", "Halsin",
              "Jaheira", "Minsc", "Minthara", "Alfira", "Losiir"]


list_1 = companions[1:4]
print(list_1)

list_2 = companions[1:7] + [companions[7]] + [companions[9]] + [companions[11]]
print(list_2)

list_3 = [companions[11]] + [companions[8]] + [companions[5]] + [companions[2]]
print(list_3)

list_4 = companions[0:1] + companions[-1:]
print(list_4)
