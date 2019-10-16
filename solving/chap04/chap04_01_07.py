account = input()
new_account = ''

for i in account:
    if i != '-':
        new_account += i

print(new_account)