# CODINGAN BERARAH

print("ini hasil dari graph berarah atau directed")
# MENAMPILAKAN HASIL GRAPH
graph={
    'a':['b','c'],
    'B':['C'],
    'C':['D']
}


for simpul in graph:
    print(simpul,"terhubung ke", graph[simpul])


print("===========================================")



 # MENAMPILAKAN HASIL GRAPH TAK BERARA
print("ini hasil dari grap tak berarah atau weighted graph")

graph={
    'a':['b','c'],
    'B':['a'],
    'C':['a']
}

for simpul in graph:
    print(simpul,"terhubung ke", graph[simpul])

print("===========================================")


print("ini hasil graph berbobot ")
# MENAMPILAKAN HASIL GRAPH berbobot
graph={
    'a': {'b':5,"c":2},
    'b':{'d':4,},
    'c':{'d':7},
    'd':{'c':7}
}

for node in graph:
    for neighbor in graph[node]:
        print(f"{node}->{neighbor} = {graph[node ][neighbor]} km")

print("===========================================")
