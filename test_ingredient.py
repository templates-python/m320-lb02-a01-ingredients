from additive import Additive
from fruit import Fruit
from grain import Grain
from ingredient import Ingredient


def test_ingredient():
    try:
        Ingredient()
        assert False
    except TypeError:
        assert True


def test_missing_name():
    try:
        Fruit(price=2.20, origin='DE')
        assert False
    except TypeError:
        assert True


def test_missing_price():
    try:
        Grain(name='Weed')
        assert False
    except TypeError:
        assert True


def test_negative_price():
    try:
        Additive(name='Sawdust', price=-0.1, origin='CD')
        assert False
    except ValueError:
        assert True


def test_fruit():
    fruit = Fruit(name='Apple', price=1.05, origin='CH')
    assert fruit.__str__() == "Fruit(name='Apple', price=1.05, origin='CH')"


def test_fruit_no_origin():
    try:
        fruit = Fruit(name='Apple', price=1.05, origin='CH')
        fruit.origin = ''
        assert False
    except ValueError:
        assert True


def test_grain():
    grain = Grain(name='Barley', price=0.76, allergen='Gluten')
    assert grain.__str__() == "Grain(name='Barley', price=0.76, allergen='Gluten')"


def test_grain_no_allergen():
    grain = Grain(name='Barley', price=0.76)
    assert grain.__str__() == "Grain(name='Barley', price=0.76, allergen='')"


def test_additive():
    additive = Additive(name='Sugar', price=0.07, origin='Cuba', allergen='Diabetes')
    assert additive.__str__() == "Additive(name='Sugar', price=0.07, allergen='Diabetes', origin='Cuba')"


def test_additive_no_allergen():
    additive = Additive(name='Sugar', price=0.07, origin='Cuba')
    assert additive.__str__() == "Additive(name='Sugar', price=0.07, allergen='', origin='Cuba')"

def test_additive_no_origin():
    try:
        additive = Additive(name='Sugar', price=0.07, allergen='Diabetes', origin='CH')
        additive.origin = ''
        assert False
    except ValueError:
        assert True
