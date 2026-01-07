import random


n_groups = int(input("Entrez le nombre de groupes souhaité : "))

n_teams = n_groups * 4


teams = []
print(f"Veuillez saisir les noms de {n_teams} équipes :")
for i in range(n_teams):
    team = input(f"Équipe {i+1} : ")
    teams.append(team)


random.shuffle(teams)
pots = [teams[i::4] for i in range(4)]  

groups = [[] for _ in range(n_groups)]

for pot in pots:
    random.shuffle(pot)  
    for i in range(n_groups):
        groups[i].append(pot[i])  


print("\nRésultats du tirage au sort :")
for i, group in enumerate(groups, start=1):
    print(f"Groupe {i} : {', '.join(group)}")