from discover_network import decouvrir_rizou
from distance_multiple import dist_multiple



valeurs, noms = decouvrir_rizou()
print(valeurs, noms)
new_valeurs = dist_multiple(valeurs)
print(new_valeurs)

# cord1 = (x1,y1,new_valeurs[0])
# cord2 = (x2,y2,new_valeurs[1])
# cord3 = (x3,y3,new_valeurs[2])
#plot_schema(cord1,cord2,cord3, noms)

