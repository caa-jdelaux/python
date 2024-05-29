import jde_mod as mod
import pytest


#Paramétrage de notre test
@pytest.mark.parametrize("a, b, expected", [
    (2, 3, 5),
    (2.5, 3.5, 6.0),
    (-2, 3, 1)
])

#Itération sur les paramètres
def test_ajouter(a, b, expected):
    assert mod.ajouter(a, b) == expected