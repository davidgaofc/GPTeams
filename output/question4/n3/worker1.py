```python
def freeze_account(account):
    if not account.status == 'frozen':
        account.status = 'frozen'
        return True
    else:
        return False
```