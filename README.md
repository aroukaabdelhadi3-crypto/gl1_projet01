

import random


n_groups = int(input("Entrez le nombre de groupes souhaité : "))

n_teams = n_groups * 4

# Saisir les noms des équipes
teams = []
print(f"Veuillez saisir les noms de {n_teams} équipes :")
for i in range(n_teams):
    team = input(f"Équipe {i+1} : ")
    teams.append(team)

# Mélanger les équipes et les diviser en 4 pots (simplifié : mélange aléatoire)
random.shuffle(teams)
pots = [teams[i::4] for i in range(4)]  # 4 pots, chacun avec n_groups équipes

# Initialiser les groupes
groups = [[] for _ in range(n_groups)]

# Tirage au sort : pour chaque pot, mélanger et assigner une équipe par groupe
for pot in pots:
    random.shuffle(pot)  # Mélanger le pot
    for i in range(n_groups):
        groups[i].append(pot[i])  # Ajouter une équipe à chaque groupe

# Afficher les résultats
print("\nRésultats du tirage au sort :")
for i, group in enumerate(groups, start=1):
    print(f"Groupe {i} : {', '.join(group)}")
