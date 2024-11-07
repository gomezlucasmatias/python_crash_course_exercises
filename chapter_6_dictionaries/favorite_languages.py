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

