alien_0 = {'color': 'green', 'points': 5}

#print(alien_0['color'])
#print(alien_0['points'])

alien_0['x_position'] = 0
alien_0['y_position'] = 25
alien_0['speed'] = 'medium'
#print(alien_0)
print(f'Original position: {alien_0["x_position"]}')
if alien_0['speed'] == 'slow':
    increase_x = 1
    alien_0['x_position'] = alien_0['x_position'] + increase_x
elif alien_0['speed'] == 'medium':
    increase_x = 2
    alien_0['x_position'] = alien_0['x_position'] + increase_x 
else:
    increase_x = 3
    alien_0['x_position'] = alien_0['x_position'] + increase_x 

print(f'New position: {alien_0["x_position"]}')
    
