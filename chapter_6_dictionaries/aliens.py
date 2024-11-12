alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'red', 'points': 10}
alien_2 = {'color': 'yellow', 'points': 15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)

print('\n...')
print('\n')

aliens = []

for alien in range(0, 15):
    alien = {'color': 'green', 'point': 5, 'speed': 'low'}
    aliens.append(alien)

print(f'There are {len(aliens)} aliens')
print('\n\n')

for alien in aliens[0:5]:
    print(alien)

print('\n...')
print('\nChanging kinds of aliens')

for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['point'] = 10
        alien['speed'] = 'medium'

print('\n')

for alien in aliens[0:5]:
    print(alien)
 
