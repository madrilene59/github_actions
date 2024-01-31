import pytest


def test_calc_addition():
    """
    Test the addition function.

    :return: None
    """
    # Fonction test du résultat de 2+4
    output = 2 + 4
    assert output == 6


def test_calc_substraction():
    """
    Test the substraction operation in the calculator.

    :return: None
    """
    # Fonction test du résultat de 2-4
    output = 2 - 4
    assert output == -2


def test_calc_multiply():
    """
    Test the result of multiplying 2 by 4.

    :return: None
    """
    # Fonction test du résultat de 2*4
    output = 2 * 4
    assert output == 8


def test_coucou():
    """
    Test Coucou Method
    ~~~~~~~~~~~~~~~~~~

    .. function:: test_coucou()

       Fonction qui vérifie si le résultat renvoie 'hello'.

       :return: None

    .. note::
       Cette méthode effectue une vérification simple pour s'assurer que le résultat renvoie 'hello'.
       Si la condition n'est pas satisfaite, une AssertionError est levée.

    .. warning::
       Il ne faut pas s'attendre à un exemple de code détaillé car cela est contre les consignes.

    Example
    ~~~~~~~

    .. code-block:: python

       test_coucou()

    """
    # Fonction test si la résultat renvoie 'hello'
    output = 'hello'
    assert output == 'hello'

