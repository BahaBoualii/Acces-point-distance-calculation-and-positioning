from discover_network import decouvrir_rizou
from distance_calculate import estimate_distance

# this function is for detecting the first 3 APs
# and calculate each one's distance to
# the mobile device

lista, autres = decouvrir_rizou()
print(lista)

def dist_multiple(liste):
    new_liste = []
    if len(liste) >= 3:
        new_liste.append(estimate_distance(liste[0]))
        new_liste.append(estimate_distance(liste[1]))
        new_liste.append(estimate_distance(liste[2]))
        return new_liste
    else:
        return 'not enough Access Points!'

print(dist_multiple(lista))