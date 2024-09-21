# Commit history available: https://github.com/z3lx/poly-2024a-tp01

from utils import try_cast


def ex4() -> None:
    s = input("Pourcentage de batterie ? ")
    battery_level = try_cast(s, float)
    if battery_level is None:
        return

    if battery_level < 0 or battery_level > 100:
        print("Veuillez entrer un pourcentage entre 0 et 100")
        return

    if battery_level == 0:
        print("La batterie est vide")
        return

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


ex4()
