def dire_bonjour(n, p):
    """Prints a greeting message with the provided name and surname.

    Args:
        n (str): The name to be included in the greeting.
        p (str): The surname to be included in the greeting.
    """
    print(f"Bonjour {n.upper()} {p.capitalize()} !")

PI_value = 3.141592653589793

def get_pi():
    """Returns the value of PI with 2 decimal places."""
    return float(f"{PI_value:.2f}")

def ajouter(a: float, b: float) -> float:
    """Returns the sum of the two provided numbers.

    Args:
        a (int): The first number to be added.
        b (int): The second number to be added.
    """
    return a + b


def creer_tuple(a: int, b: int, c: int) -> tuple:
    """Creates a tuple with the provided values.

    Args:
        a (int): The first value to be included in the tuple.
        b (int): The second value to be included in the tuple.
        c (int): The third value to be included in the tuple.
    """
    return a, b, c