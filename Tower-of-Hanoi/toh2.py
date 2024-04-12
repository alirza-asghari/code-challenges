def print_towers(towers):
    for i in range(len(towers[0])-1, -1, -1):
        for j in range(3):
            if len(towers[j]) > i:
                print(towers[j][i], end="\t")
            else:
                print("|", end="\t")
        print()

def TowerOfHanoi(n , source, destination, auxiliary):
    if n==1:
        print(f"Move disk 1 from source {source} to destination {destination}")
        towers[source].pop()
        towers[destination].append(1)
        return
    TowerOfHanoi(n-1, source, auxiliary, destination)
    print(f"Move disk {n} from source {source} to destination {destination}")
    towers[source].pop()
    towers[destination].append(n)
    TowerOfHanoi(n-1, auxiliary, destination, source)

n = 4
towers = [[i for i in range(n, 0, -1)], [], []]
print_towers(towers)
TowerOfHanoi(n, 0, 2, 1)
