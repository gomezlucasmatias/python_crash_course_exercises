users = ['andre', 'lucas', 'admin', 'ada', 'atena']

for user in users:
    if user == 'admin':
        print(f'Hello {user.title()}, would you like to see a status report?')
    else:
        print(f'Hello {user.title()}')
