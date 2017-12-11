import money
from Currency import Currency
from Currency import Sum
from Currency import Bank

def test_that_testing_works():
    assert money.returns_true() == True

def test_multiplication():
    five = Currency(5)
    assert five.times(2) == Currency(10)
    assert five.times(3) == Currency(15)

def test_equality():
    five_dollars = Currency(5, "USD")
    assert five_dollars == Currency(5, "USD")
    assert five_dollars != Currency(6, "USD")
    five_euro = Currency(5, "EUR")
    assert five_dollars != five_euro

def test_simple_addition():
    summed = Currency(5, "USD").plus(Currency(1, "USD"))
    bank = Bank()
    reduced = bank.reduce(summed, "USD")
    assert reduced == Currency(6, "USD")

def testPlusReturnsSum():
    five = Currency(5, "USD")
    one = Currency(1, "USD")
    result = five.plus(one)
    assert result.augend == five
    assert result.addend == one

def test_reduce_sum():
    summed = Currency(5, "USD").plus(Currency(1, "USD"))
    bank = Bank()
    reduced = bank.reduce(summed, "USD")
    assert reduced == Currency(6, "USD")

def test_reduce(): 
    bank = Bank()
    result = bank.reduce(Currency(1, "USD"), "USD")
    assert result == Currency(1, "USD")

def test_reduce_different_currencies():
    bank = Bank()
    bank.addRate("EUR", "USD", 2)
    result = bank.reduce(Currency(2, "EUR"), "USD")
    assert result == Currency(1, "USD")

def test_same_currency_rates():
    assert Bank().rate("USD", "USD") == 1

def test_mixed_addition():
    five_dollars = Currency(5, "USD")
    ten_euro = Currency(10, "EUR")
    bank = Bank()
    bank.addRate("EUR", "USD", 2)
    result = bank.reduce(five_dollars.plus(ten_euro), "USD")
    assert result == Currency(10, "USD")
