# TODO: Calculer la distance qu'un poids peut atteindre en utilisant la formule de la portée d'un projectile.
# TODO: Importer les modules nécessaires.
from math import radians, sin

speed = float(input("Vitesse initiale (m/s): "))
angle = float(input("Angle de lancer (en degrés): "))
distance = ((speed ** 2) * sin(radians(2 * angle))) / 9.8

print(f"Distance parcourue: {distance:.2f}m")