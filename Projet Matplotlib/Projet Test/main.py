
import matplotlib.pyplot as plt


# je fais une programme pour crée un graphique

# premier jour de vente
annees = ["1er", "2eme", "3eme"]
# Switch
# 1: 15 |2: 32.30 |3: 52,20
# PS5
# 1: 4.5| 2: 22| 3: 24
y = ["4.5", "10", "15", "22", "24", "32.5", "40", "52"]


plt.title("Les ventes de la switch et de la Ps5 ses trois premieres années")
plt.ylabel("Années")
plt.xlabel("Nombre de vente des consoles (en millions)")
plt.plot(range(0, 8), y)
# plt.plot(3, y, "r-+")
plt.show()