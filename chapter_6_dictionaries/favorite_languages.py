favorite_lenguages = {
        'mati': 'python',
        'mauro': 'c#',
        'betti': 'html',
        'sabri': 'javascript',
        }

language = favorite_lenguages['mati'].title()

print(f"Mati's favorite language is {language}")

for key, value in favorite_lenguages.items():
    print(f"\n{key.title()}'s favorite language is {value}")
