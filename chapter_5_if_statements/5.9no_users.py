users = []

if users:
    for user in users:
        print(f'Hello {user.title()}, would you like to see a status report?')
else:
    print("We need to find some users!")

