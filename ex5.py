#TODO: Analyser la chaîne de caractères saisie et compter le nombre de médailles.
#      Attention si la chaîne est invalide, un message d'erreur est attendu.
import re

country = input("Pays concerné ? ")
code_medals = input("Chaine représentant les médailles ? ")

valid_medal_codes = "GSB"
pattern = re.compile(f"[{valid_medal_codes}]*")
if not re.fullmatch(pattern, code_medals):
    print("Ceci est une chaine invalide.")
else:
    g = code_medals.count("G")
    s = code_medals.count("S")
    b = code_medals.count("B")
    print(f"{country}:\n- {g} Or\n- {s} Argent\n- {b} Bronze")
