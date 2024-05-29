#from ..module.jde_mod import mod
import pytest

# mon script se trouve c:/Users/orsys/Documents/GitHub/python/Python.Bureautique-main/JDE/Test_pytest/mod_test.py
# mon module se trouve c:/Users/orsys/Documents/GitHub/python/Python.Bureautique-main/JDE/module/jde_mod.py
# importer le module jde_mod
import importlib
foobar = importlib.import_module("module.jde_mod")


# from Python.Bureautique-main.JDE.module import jde_mod




#Paramétrage de notre test
@pytest.mark.parametrize(a, b, [
    (2, 3, 5),
    (2.5, 3.5, 6.0),
    (-2, 3, 1)
])

#Itération sur les paramètres
def test_ajouter(a, b, expected):
    assert foobar.ajouter(a, b) == expected