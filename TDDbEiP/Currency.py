class Currency:
    def __init__(self, amount, currency=None):
        self.amount = amount
        self.currency = currency

    def __eq__(self, other):
        #Override the ==
        return self.amount == other.amount and self.currency == other.currency

    def times(self, multiplier):
        return Currency(self.amount * multiplier, self.currency)

    def plus(self, new_money):
        return Sum(self, new_money)

    def reduce(self, bank, to):
        return Currency(self.amount / bank.rate(self.currency, to), to)


class Sum:
    def __init__(self, augend, addend):
        self.augend = augend
        self.addend = addend

    def reduce(self, bank, to):
        augend = self.augend.reduce(bank, to).amount
        addend = self.addend.reduce(bank, to).amount
        return Currency(augend + addend, to)


class Bank:
    def __init__(self):
        self.rates = {}

    def reduce(self, summed, to):
        return summed.reduce(self, to)

    def rate(self, from_currency, to_currency):
        if from_currency == to_currency:
            print("We are equal")
            return 1
        else:
            print(self.rates[(from_currency, to_currency)])
            return self.rates[(from_currency, to_currency)]

    def addRate(self, from_currency, to_currency, rate):
        self.rates.update({(from_currency, to_currency): rate})


