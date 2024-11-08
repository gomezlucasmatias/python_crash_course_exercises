favorite_lenguages = {
        'mati': 'python',
        'mauro': 'c#',
        'betti': 'html',
        'sabri': 'javascript',
        }

friends = ['mati', 'mauro']
#language = favorite_lenguages['mati'].title()

#print(f"Mati's favorite language is {language}")

#for key, value in favorite_lenguages.items():
#    print(f"\n{key.title()}'s favorite language is {value}")

for name in favorite_lenguages:
    print(f'\nHi {name.title()}')
     
    if name in friends:
        lenguage = favorite_lenguages[name].title()
        print(f'\tI see that you really love {lenguage}')

for name in sorted(favorite_lenguages.keys()):
    print(f'\n{name.title()}, thank you for taking the poll.')

print('\nThe following language have been mentioned:')

for value in favorite_lenguages.values():
    print(f'{value.title()}')

