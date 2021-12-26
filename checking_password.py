def checking_password(value):
    assert len(str(value)) >= 8, "Very weak."
    assert value[0-9], 'Weak.'

password = input()
print(checking_password(password))