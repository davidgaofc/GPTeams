```python
def freeze_account(account):
    if account.status == "frozen":
        return False
    else:
        account.status = "frozen"
        return True
```