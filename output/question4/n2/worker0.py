```python 
def freeze_account(account):
    if account.frozen:
        return False
    else:
        account.frozen = True
        return True
```
