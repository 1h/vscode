def account(name, number, balance):
    return {'name': name, 'number': number, 'balance': balance}


def deposit(acct, amount):
    if amount <= 0:
        raise ValueError('amount must be positive')
    acct['balance'] += amount


def withdraw(acct, amount):
    if amount > acct['balance']:
        raise RuntimeError('balance not enough')
    acct['balance'] -= amount


def to_str(acct):
    return 'Account:' + str(acct)
