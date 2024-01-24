"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item


def test_calculate_total_price():
    item1 = Item("Холодильник", 10500, 6)
    item2 = Item("Сковорода", 1600, 20)
    assert item1.calculate_total_price() == 63000
    assert item2.calculate_total_price() == 32000


def test_apply_discount():
    item1 = Item("Холодильник", 10500, 6)
    item2 = Item("Сковорода", 1600, 20)
    item1.pay_rate = 0.8
    item2.pay_rate = 0.6
    item1.apply_discount()
    item2.apply_discount()
    assert item1.price == 8400
    assert item2.price == 960
