# Commit history available: https://github.com/z3lx/poly-2024a-tp01

def ex1() -> None:
    country = input("De quelle nationalité est l'athlète ? ")
    athlete = input("Quel est son nom ? ")
    date = input("Date du record ? ")
    sport = input("Dans quelle discipline ? ")
    category = input("Dans une catégorie spécifique ? ")
    record = input("Quel est le record ? ")

    message = (
        f"\nNouveau Record:\n--------------------\n"
        f"{date} - {sport} - {category}:\n"
        f"\t{athlete} ({country}) - {record}"
    )

    print(message)


ex1()
