current_users = ['andre', 'admin', 'flavia', 'dino', 'gloria']

new_users = ['flavia', 'matias', 'admin', 'sofia', 'dino']

for user in new_users:
    if user in current_users:
        print('That username is already taken, please choose a new one')
    else:
        print('Your account has been created')

 
