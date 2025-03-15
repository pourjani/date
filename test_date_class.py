import pytest
from date_class import Date

def test_is_leap_year():
    assert Date.is_leap_year(2020) == True
    assert Date.is_leap_year(2021) == False
    assert Date.is_leap_year(1900) == False
    assert Date.is_leap_year(2000) == True

def test_get_days_in_month():
    assert Date.get_days_in_month(1, 2024) == 31
    assert Date.get_days_in_month(2, 2024) == 29
    assert Date.get_days_in_month(2, 2023) == 28
    assert Date.get_days_in_month(4, 2024) == 30
    with pytest.raises(ValueError):
        Date.get_days_in_month(13, 2024)

def test_add_days():
    date = Date(1, 1, 2024)
    date.add_days(15)
    assert date.equals(Date(16, 1, 2024))
    date.add_days(-15)
    assert date.equals(Date(1, 1, 2024))


def test_compare_to():
    date1 = Date(1, 1, 2024)
    date2 = Date(1, 1, 2025)
    assert date1.compare_to(date2) < 0
    assert date2.compare_to(date1) > 0
    assert date1.compare_to(date1) == 0

def test_equals():
    date1 = Date(1, 1, 2024)
    date2 = Date(1, 1, 2024)
    date3 = Date(2, 1, 2024)
    assert date1.equals(date2)
    assert not date1.equals(date3)

def test_get_days_from():
    date1 = Date(1, 1, 2024)
    date2 = Date(1, 1, 2025)
    assert date1.get_days_from(date2) == 366  # Leap year
    assert date2.get_days_from(date1) == -366
    date3 = Date(1, 2, 2024)
    assert date1.get_days_from(date3) == 31
