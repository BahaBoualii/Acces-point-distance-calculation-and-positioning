import matplotlib.pyplot as plt
from calc_mobile_pos import calc_mobile_pos

# this function is for plotting the schema for
# the position of the mobile device compared to the 3 APs

def plot_schema(cord1,cord2,cord3,noms):
    x, y = calc_mobile_pos(cord1,cord2,cord3)
    plt.axis([0, 50, -50, 50])
    plt.axis("equal")
    ax = plt.gca()
    plt.scatter(x, y)
    plt.margins(50, 50)
    c1 = plt.Circle((cord1[0], cord1[1]), radius=cord1[2], color='red', alpha=0.4)
    c2 = plt.Circle((cord2[0], cord2[1]), radius=cord2[2], color='blue', alpha=0.4)
    c3 = plt.Circle((cord3[0], cord3[1]), radius=cord3[2], color='yellow', alpha=0.4)
    ax.legend([c1,c2,c3], noms)
    ax.add_artist(c1)
    ax.add_artist(c2)
    ax.add_artist(c3)
    plt.show()

plot_schema((0,1,1),(0,-1,1),(1,0,1),["ap1","ap2","ap3"])
