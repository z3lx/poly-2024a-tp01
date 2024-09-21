import math
from utils import try_cast


def ex2() -> None:
    s = input("Quelle quantité d'eau faut-il assainir ? ")
    water_quantity = try_cast(s, float)
    if water_quantity is None:
        return

    n = water_quantity / 5
    n_filter = math.ceil(n)
    n_light = math.ceil(n * 3)
    kg_chlorine = n * 0.5

    formatted = (
        f"Voici les éléments requis pour assainir {water_quantity}L d'eau:\n"
        f"\t- Filtre(s) : {n_filter}\n"
        f"\t- Lampe(s) UV : {n_light}\n"
        f"\t- Chlore : {kg_chlorine}kg"
    )

    print(formatted)


ex2()
