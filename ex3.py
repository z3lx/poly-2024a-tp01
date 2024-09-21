# Commit history available: https://github.com/z3lx/poly-2024a-tp01

from math import radians, sin
from utils import try_cast


def ex3() -> None:
    s = input("Vitesse initiale (m/s): ")
    speed = try_cast(s, float)
    if speed is None:
        return

    s = input("Angle de lancer (en degrés): ")
    angle = try_cast(s, float)
    if angle is None:
        return

    distance = ((speed ** 2) * sin(radians(2 * angle))) / 9.8

    print(f"Distance parcourue: {distance:.2f}m")


ex3()
