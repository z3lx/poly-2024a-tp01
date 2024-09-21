from typing import Any, Type


def try_cast(value: Any, cast: Type) -> Any:
    try:
        return cast(value)
    except ValueError:
        print("a")
        print(f"Veuillez entrer un {cast.__name__}")
        return None
