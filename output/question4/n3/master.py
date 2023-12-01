def freeze_account(account):
    if account.balance != 0:
        return False
    elif account.status == 'frozen':
        return False
    else:
        account.status = 'frozen'
        return True