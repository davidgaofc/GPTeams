```python
def freeze_account(account):
    if account.balance != 0:
        return False
    account.frozen = True
    return True
```