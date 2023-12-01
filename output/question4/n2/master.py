def freeze_account(account):
    if account.frozen or account.status == "frozen":
        return False
    else:
        account.frozen = True
        account.status = "frozen"
        return True