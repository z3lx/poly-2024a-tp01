import re


def ex5() -> None:
    country = input("Pays concerné ? ")
    code_medals = input("Chaine représentant les médailles ? ")

    pattern = re.compile("[GBS]*")
    if not re.fullmatch(pattern, code_medals):
        print("Ceci est une chaine invalide.")
        return

    g = code_medals.count("G")
    s = code_medals.count("S")
    b = code_medals.count("B")
    print(f"{country}:\n- {g} Or\n- {s} Argent\n- {b} Bronze")


ex5()
