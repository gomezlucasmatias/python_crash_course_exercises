favorite_languages = {
                     'sarah': ['go', 'c#'],
                     'mati': ['javascript, python'],
                     'mauro': ['c', 'rust'],
                     'bety': ['none', 'nothing'],
                     'damaris': ['html', 'css'],
                     }

for key, values in favorite_languages.items():
    print(f'\n{key.title()} really love programing in:\n')
    for value in values:
        print(f'\t\t\t\t\t\t{value.title()}')
