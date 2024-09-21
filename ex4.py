# TODO: Écrire un programme qui demande le pourcentage de charge actuel de la batterie du bateau,
#        calcule la distance restante en km en fonction de ce pourcentage,
#        et affiche le résultat au format "XX km".
#        Assurez une gestion du pourcentage valide au cours de votre programme (% toujours dans [0 ; 100]).

battery_level = float(input("Pourcentage de batterie ? "))

if battery_level <= 0:
    print("La batterie est vide")
else:
    battery_multiplier_map = {
        50: 2,
        25: 0.5,
        10: 1,
        5: 2.5,
        0: 6
    }

    distance = 0
    for percentage, multiplier in battery_multiplier_map.items():
        if battery_level > percentage:
            distance += multiplier * (battery_level - percentage)
            battery_level = percentage

    print(f"{distance} km")
